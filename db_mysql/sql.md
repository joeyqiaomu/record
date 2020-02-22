#　**<font color=Red>数据库**
##  **<font color=Red>关系行数据库**

关系型数据库　             --oracle mysql mariadb sqlite
key-value 数据库          -- redis
elasticsearch ，solr       搜索引擎
mongoDB                   文档　document store
HBase                    --  Wide column store
hlive       数据仓库

```
关系数据库使用行、列组成的二维表来组织数据和关系,表中行(记录)即可以描述数据实体,也可以描述实体间关系。
关系模型比网状模型、层次模型更简单,不需要关系数存储的物理细节,专心于数据的逻辑构建,而且关系模型有
论文的严格的数学理论基础支撑

SQL是结构化查询语言Structured Query Language
DDL: Data Defination Language 数据定义语言 负责数据库定义、数据库对象定义
             CREATE，DROP，ALTER
DML: Data Manipulation Language 数据操纵语言 负责对数据库对象的操作,CRUD增删改查
             INSERT，DELETE，UPDATE
DCL：Data Control Language 数据控制语言 负责数据库权限访问控制
             GRANT，REVOKE，COMMIT，ROLLBACK(负责处理ACID事务)
DQL：Data Query Language 数据查询语言
             SELECT

--------------------------------------------------------------------------
DCL:
GRANT ALL ON employees.* TO 'wayne'@'%' IDENTIFIED by 'wayne';
REVOKE ALL ON *.* FROM wayne;

CREATE DATABASE IF NOT EXISTS test CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
CREATE DATABASE IF NOT EXISTS test CHARACTER SET utf8;


创建表
表分为行和列,MySQL是行存数据库。数据是一行行存的,列必须固定多少列。
行Row,也称为记录Record,元组。
列Column,也称为字段Field、属性


CREATE TABLE `employees` (
`emp_no` int(11) NOT NULL,
`birth_date` date NOT NULL,
`first_name` varchar(14) NOT NULL,
`last_name` varchar(16) NOT NULL,
`gender` enum('M','F') NOT NULL,
`hire_date` date NOT NULL,
PRIMARY KEY (`emp_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



DESC
查看列信息
{DESCRIBE | DESC} tbl_name [col_name | wild]


关系
在关系数据库中,关系就是二维表,由行和列组成。
行Row,也称为记录Record,元组。
列Column,也称为字段Field、属性。
字段的取值范围叫做 域Domain。例如gender字段的取值就是M或者F两个值。
维数:关系的维数指关系中属性的个数
基数:元组的个数


```


### **pymysql**
- 一般流程
 - 建立连接
 - 获取游标
 - 执行SQL
 - 提交事务
 - 释放资源


 | 参数名称                 |                             含义                              |
|:------------------------ |:-------------------------------------------------------------:|
| fetchone()         |                      进程id                            |
| wait(self, timeout=None) |                 进程的退出状态码                |
```python
import pymysql


IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306
conn = None
cursor = None #对结果集的操作
try:
    conn = pymysql.connect(IP,USERNAME,PASSWORD,DBNAME,PORT)
    cursor = conn.cursor()

    sql = "select * from IP"
    #sql = "insert INTO IP (IP,nexthop,mask) VALUES('10.202.110.123','10.0.0.13','32');"
    r = cursor.execute(sql) # 返回的值是int
    print(r)

    conn.commit()
except:
    conn.rollback()
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
finally:
    cursor.close()
    conn.close()

```
```python
import pymysql


IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306
conn = None
cursor = None #对结果集的操作
try:
    conn = pymysql.connect(IP,USERNAME,PASSWORD,DBNAME,PORT)
    cursor = conn.cursor()

    sql = "select * from IP"
    #sql = "insert INTO IP (IP,nexthop,mask) VALUES('10.202.110.123','10.0.0.13','32');"
    r = cursor.execute(sql) # 返回的值是int
    print(r)
    print(cursor.fetchone())
    print(cursor.rowcount,cursor.rownumber)
    print(cursor.fetchone())
    print(cursor.rowcount, cursor.rownumber)
    print("-------------------")
    print(cursor.fetchmany(3))
    print(cursor.rowcount, cursor.rownumber)
    print(cursor.fetchmany(3))
    print(cursor.rowcount, cursor.rownumber)
    print("-------------------")
    cursor.rownumber = 100
    print(cursor.fetchall())
    print(cursor.rowcount, cursor.rownumber)




    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
finally:
    cursor.close()
    conn.close()

```

```python
import pymysql


IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306
conn = None
cursor = None #对结果集的操作
try:
    conn = pymysql.connect(IP,USERNAME,PASSWORD,DBNAME,PORT)
    cursor = conn.cursor()

    #sql = "select * from IP"
    sql = "select * from IP where IP='{}'".format('10.200.200.1')
    #sql = "insert INTO IP (IP,nexthop,mask) VALUES('10.202.110.123','10.0.0.13','32');"
    r = cursor.execute(sql) # 返回的值是int
    print(r)
    if r == 1 :
        ip = cursor.fetchone()
        print(ip,type(ip))
    # print(cursor.fetchone())
    # print(cursor.rowcount,cursor.rownumber)
    # print(cursor.fetchone())
    # print(cursor.rowcount, cursor.rownumber)
    # print("-------------------")
    # print(cursor.fetchmany(3))
    # print(cursor.rowcount, cursor.rownumber)
    # print(cursor.fetchmany(3))
    # print(cursor.rowcount, cursor.rownumber)
    # print("-------------------")
    # cursor.rownumber = 100
    # print(cursor.fetchall())
    # print(cursor.rowcount, cursor.rownumber)

    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
finally:
    cursor.close()
    conn.close()

```

#### 字典
```python
import pymysql
from pymysql.cursors import DictCursor


IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306
conn = None
cursor = None #对结果集的操作
try:
    conn = pymysql.connect(IP,USERNAME,PASSWORD,DBNAME,PORT)
    cursor = conn.cursor(DictCursor)

    #sql = "select * from IP"
    sql = "select * from IP where IP='{}'".format('10.200.200.1')
    #sql = "insert INTO IP (IP,nexthop,mask) VALUES('10.202.110.123','10.0.0.13','32');"
    r = cursor.execute(sql) # 返回的值是int
    print(r)
    if r == 1 :
        ip = cursor.fetchone()
        print(ip,type(ip))
    # print(cursor.fetchone())
    # print(cursor.rowcount,cursor.rownumber)
    # print(cursor.fetchone())
    # print(cursor.rowcount, cursor.rownumber)
    # print("-------------------")
    # print(cursor.fetchmany(3))
    # print(cursor.rowcount, cursor.rownumber)
    # print(cursor.fetchmany(3))
    # print(cursor.rowcount, cursor.rownumber)
    # print("-------------------")
    # cursor.rownumber = 100
    # print(cursor.fetchall())
    # print(cursor.rowcount, cursor.rownumber)

    conn.commit()
except Exception as e:
    conn.rollback()
    print(e)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
finally:
    cursor.close()
    conn.close()

```

```python
import pymysql
from pymysql.cursors import DictCursor


IP ='192.168.6.2'
USERNAME = 'joey'
PASSWORD ='joey'
DBNAME = 'test'
PORT = 3306


conn = None
try:
    conn = pymysql.connect(IP,USERNAME,PASSWORD,DBNAME,PORT)
    cursor = None  # 对结果集的操作
    try:
        with conn:
            with conn.cursor(DictCursor) as cursor:

            #sql = "select * from IP"
            sql = "select * from IP where IP='{}'".format('10.200.200.1')
            r = cursor.executemany(sql,(("ben{}".format(i),i+1)for i in range(10,15)))  # 返回的值是int
            print(r)
            with conn as cursor:
                cursor.execute("select * from IP")
                print(cursor.fetchone())
    except Exception as e:
        conn.rollback()
        print(e)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
finally:
    if conn:
        conn.close()

```
