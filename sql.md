# **数据库**
## **关系行数据库**




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
