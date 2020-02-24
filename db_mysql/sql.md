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



候选键

关系中,能唯一标识一条元组的属性或属性集合,称为候选键。


PRIMARY KEY主键
表中一列或者多列组成唯一的key,也就是通过这一个或者多个列能唯一的标识一条记录。即被选择的候选键。
主键的列不能包含空值null。主键往往设置为整型、长整型,可以为自增AUTO_INCREMENT字段。
表中可以没有主键,但是,一般表设计中,往往都会有主键,以避免记录重复

Foreign KEY外键
严格来说,当一个关系中的某个属性或属性集合与另一个关系(也可以是自身)的候选键匹配时,就称作这个属性
或属性集合是外键。




索引Index
可以看做是一本字典的目录,为了快速检索用的。空间换时间,显著提高查询效率。
可以对一列或者多列字段设定索引。
主键索引,主键会自动建立主键索引,主键本身就是为了快速定位唯一记录的。
唯一索引,表中的索引列组成的索引必须唯一,但可以为空,非空值必须唯一
普通索引,没有唯一性的要求,就是建了一个字典的目录而已。
在MySQL中,InnoDB和MyISAM的索引数据结构可以使用Hash或BTree,默认是BTree



```
## **<font color=Red>实体间联系类型**



| 类型            |     描述|      解决方案|　
| :------------ |:---------------:|:---------------:|
| 一对多联系　１：ｎ     | 一个员工属于一个部门,一个部门有多个员工 |　员工外键;部门主键
|多对多联系ｍ：ｎ   | 一个员工属于多个部门,一个部门有多个员工  |建立第三表（联合主键）
| 一对一联系| 假设有实体管理者,一个管理者管理一个部门,一个部门只有一个管理者     |字段建在哪张表都行


## **<font color=Red>DML —— CRUD 增删改查**
## **<font color=Red> insert**
```
INSERT INTO table_name (col_name,...) VALUES (value1,...);
-- 向表中插入一行数据,自增字段、缺省值字段、可为空字段可以不写
INSERT INTO table_name SELECT ... ;
-- 将select查询的结果插入到表中
INSERT INTO table_name (col_name1,...) VALUES (value1,...) ON DUPLICATE KEY UPDATE　col_name1=value1,...;
-- 如果主键冲突、唯一键冲突就执行update后的设置。这条语句的意思,就是主键不在新增记录,主键在就更新部分字段。
INSERT IGNORE INTO table_name (col_name,...) VALUES (value1,...);
-- 如果主键冲突、唯一键冲突就忽略错误,返回一个警告。



INSERT INTO reg (loginname, `name`, `password`) VALUES ('tom', 'tom', 'tom');
INSERT INTO reg (id, loginname, `name`, `password`) VALUES (5, 'tom', 'tom', 'tom');
---插入并更新
INSERT INTO reg (id, loginname, `name`, `password`) VALUES (1, 'tom', 'tom', 'tom') ON DUPLICATE KEY UPDATE name = 'jerry';

NSERT IGNORE INTO table_name (col_name,...) VALUES (value1,...);
-- 如果主键冲突、唯一键冲突就忽略错误,返回一个警告。

```

## **<font color=Red> Update语句**

```

UPDATE [IGNORE] tbl_name SET col_name1=expr1 [, col_name2=expr2 ...] [WHERE where_definition]
-- IGNORE 意义同Insert语句
UPDATE reg SET name='张三' WHERE id=5;


-- 注意这一句非常危险,会更新所有数据
UPDATE reg SET name = 'ben';
-- 更新一定要加条件
UPDATE reg SET name = 'ben', password = 'benpwd' WHERE id = 1;



```


## **<font color=Red> Delete语句**

```

ELETE FROM tbl_name [WHERE where_definition]
-- 删除符合条件的记录

-- 删除一定要有条件
DELETE FROM reg WHERE id = 1;



```


## **<font color=Red> Select语句**

```


SELECT
[DISTINCT]
select_expr, ...
[FROM table_references
[WHERE where_definition]
[GROUP BY {col_name | expr | position}
[ASC | DESC], ... [WITH ROLLUP]]
[HAVING where_definition]
[ORDER BY {col_name | expr | position}
[ASC | DESC] , ...]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
[FOR UPDATE | LOCK IN SHARE MODE]]

FOR UPDATE会把行进行写锁定,这是排它锁。


SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp limit 10,5

SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp where emp_no > 10005 limit 10

－－－－－－－－－分页
SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp where emp_no > 10005 limit 5 OFFSET 5


SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp where emp_no > 10010 and emp_no < 10016 LIMIT 2 OFFSET 2

SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp  where  emp_no BETWEEN 10010 and 10015

----先选择后投影（1 from 2 where 3 select（投影） 先from（加载表　２　where（selction） 3 select (投影) ）

选择(selection):又称为限制,是从关系中选择出满足给定条件的元组。
投影(projection):在关系上投影就是从选择出若干属性列组成新的关系。
连接(join):将不同的两个关系连接成一个关系。

SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp  where  emp_no BETWEEN 10010 and 10015 and last_name LIKE 'Slu%';

SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp  where  emp_no BETWEEN 10010 and 10015 and name LIKE 'Slu%';

----------------------------------------------------------------
like 能不则不用，如果用　则利用左前缀　sl% 集合主键
EXPLAIN SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp  where  last_name LIKE '%u%';
-------------------------------------in
EXPLAIN SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp  where  emp_no in (10010,10005,10003)

------------------------------Order by子句


 SELECT emp_no,birth_date ,concat(first_name ,' ',last_name) as name from employees as emp  where  emp_no > 10005 ORDER BY name desc  LIMIT 5,5

SELECT emp_no,birth_date ,first_name ,last_name from employees as emp  where  emp_no > 10005 ORDER BY first_name,last_name DESC
-- 第一字段排序是一样的时候，last_name再去比较

-----------------------------DISTINCT -不返回重复记录
SELECT DISTINCT emp_no,gender from employees　相当于(emp_no ,gender)二元组去重

－－－－－－－－－－－－－－－－－－－－－分组聚合

函数　　　　　　　　　　　　　　　　　　　　　 描述
COUNT(expr) 　　　　　　　　　　　　返回记录中记录的数目,如果指定列,则返回非NULL值的行数
COUNT(DISTINCT expr,[expr...]) 返回不重复的非NULL值的行数
AVG([DISTINCT] expr) 　　　　　　返回平均值,返回不同值的平均值
MIN(expr), MAX(expr) 　　　　　　最小值,最大值
SUM([DISTINCT] expr) 　　　　　　求和,Distinct返回不同值求和


SELECT DISTINCT COUNT(emp_no),MAX(emp_no),MIN(emp_no),AVG(emp_no) from employees

SELECT COUNT(DISTINCT gender) from employees;

SELECT COUNT(DISTINCT emp_no) as counter from employees;

－－－－－－－－－－－－－－－－－－－－－－－－－ｇｒｏｕｐ　ｂｙ

SELECT DISTINCT COUNT(emp_no),MAX(emp_no),MIN(emp_no),AVG(emp_no) from employees
where  gender='M'
GROUP BY gender

ELECT emp_no, count(salary),sum(salary),avg(salary) FROM salaries  WHERE emp_no > 10001 GROUP BY  emp_no;


-- 聚合所有
SELECT emp_no, SUM(salary), AVG(salary), COUNT(emp_no) from salaries;
-- 聚合被选择的记录
SELECT emp_no, SUM(salary), AVG(salary), COUNT(emp_no) from salaries WHERE emp_no < 10003;
-- 分组
SELECT emp_no FROM salaries GROUP BY emp_no;
SELECT emp_no FROM salaries WHERE emp_no < 10003 GROUP BY emp_no;
-- 按照不同emp_no分组,每组分别聚合
SELECT emp_no, SUM(salary), AVG(salary), COUNT(emp_no) from salaries WHERE emp_no < 10003 GROUP
BY emp_no;

------------------haning
-- HAVING子句对分组结果过滤
SELECT emp_no, SUM(salary), AVG(salary), COUNT(emp_no) from salaries GROUP BY emp_no HAVING
AVG(salary) > 45000;
-- 使用别名
SELECT emp_no, SUM(salary), AVG(salary) AS sal_avg, COUNT(emp_no) from salaries GROUP BY emp_no
HAVING sal_avg > 60000;
-- 最后对分组过滤后的结果排序
SELECT emp_no, SUM(salary), AVG(salary) AS sal_avg, COUNT(emp_no) from salaries GROUP BY emp_no
HAVING sal_avg > 60000 ORDER BY sal_avg;
分组是将数据按照指定的字段分组,最终每组只能出来一条记录。这就带来了问题,每一组谁做代表,其实谁做代表都
不合适。
如果只投影分组字段、聚合数据,不会有问题,如果投影非分组字段,显示的时候不能确定是组内谁的数据。
-- 分组
SELECT emp_no, MAX(salary) FROM salaries; -- 10001 88958
SELECT emp_no, MIN(salary) FROM salaries; -- 10001 40006
上例很好的说明了使用了聚合函数,虽然没有显式使用Group By语句,但是其实就是把所有记录当做一组,每组只能出
一条,那么一组也只能出一条,所以结果就一条。
但是emp_no就是非分组字段,那么它就要开始覆盖,所以,显示为10001。当求最大值的时候,正好工资表中10001的工
资最高,感觉是对的。但是,求最小工资的时候,明明最小工资是10003的40006,由于emp_no不是分组字段,导致最后
被覆盖为10001。
SELECT emp_no, MIN(salary) FROM salaries GROUP BY emp_no;
上句才是正确的语义,按照不同员工emp_no工号分组,每一个人一组,每一个人有多个工资记录,按时每组只能按照人
头出一条记录

-------------------------HAVING
SELECT emp_no, count(salary),sum(salary),avg(salary) FROM salaries
WHERE emp_no > 10001
GROUP BY  emp_no
HAVING avg(salary) > 45000;
SELECT emp_no as id, count(salary),sum(salary),avg(salary) as sal_avg FROM salaries
WHERE emp_no > 10001
GROUP BY  id
HAVING sal_avg > 45000;

SELECT emp_no as id, count(salary),sum(salary),avg(salary) as sal_avg FROM salaries
WHERE emp_no > 10001
GROUP BY  id
HAVING sal_avg > 45000
ORDER BY salary
LIMIT 1;

SELECT emp_no as id, max(salary) as ss  FROM salaries
WHERE emp_no > 10001
GROUP BY  id
-- HAVING sal_avg > 45000
ORDER BY ss  DESC
LIMIT 1;






-- 单表较为复杂的语句
SELECT
emp_no,
avg(salary) AS avg_salary
FROM
salaries
WHERE
salary > 70000
GROUP BY
emp_no
HAVING
avg(salary) > 50000
ORDER BY
avg_salary DESC
LIMIT 1;


--------------- 子查询

SELECT * from employees where emp_no in (SELECT emp_no as id FROM salaries
WHERE salary > 70000
GROUP BY emp_no)

SELECT emp_no ,first_name as name  from (SELECT * from employees where emp_no > 10018) as emp


－－－－－－－－－－－－－－－连接

－－－－－－－　cross join  -employees 中每一个记录都和salaries进行乘积，Ｍ*Ｎ 笛卡尔乘积,全部交叉
SELECT * from employees CROSS JOIN salaries 　

SELECT * from employees  salaries

---------- inner join
inner join,省略为join。
等值连接,只选某些field相等的元组(行),使用On限定关联的结果
自然连接,特殊的等值连接,会去掉重复的列。用的少


-- 内连接,笛卡尔乘积 800行
SELECT * from employees JOIN salaries;
SELECT * from employees INNER JOIN salaries;


SELECT * from employees  inner JOIN salaries  ON employees.emp_no = salaries.emp_no


-- ON等值连接 40行
SELECT * from employees , salaries where employees.emp_no = salaries.emp_no


-- 自然连接,去掉了重复列,且自行使用employees.emp_no = salaries.emp_no的条件
SELECT * from employees NATURAL JOIN salaries

SELECT * from employees INNER JOIN salaries on employees.emp_no = salaries.emp_no
where salary > 70000


－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－－

外连接
outer join,可以省略为join
分为左外连接,即左连接;右外连接,即右连接;全外连接
--------- 外连接


SELECT * from employees LEFT OUTER JOIN salaries ON employees.emp_no = salaries.emp_no
SELECT * from employees RIGHT OUTER JOIN salaries ON employees.emp_no = salaries.emp_no


SELECT  employees.* from employees
LEFT OUTER JOIN salaries ON employees.emp_no = salaries.emp_no
WHERE salaries.emp_no is NULL


自连接
表,自己和自己连接

原子性
 事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切
) 相关的
隔离性 一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其
 他事务是隔离的,并发执行的各个事务之间不能互相干扰
持久性 持久性也称永久性(permanence),指一个事务一旦提交,它对数据库中数据的改变
 就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响

```

## **<font color=Red> 事务Transaction ACID**


| 特性               |       描述     |
|:------------------------ |:----------------:|
| 原子性    atomicity)          |      一个事务是一个不可分割的工作单位,事务中包括的所有操作要么全部做完,要么什么都不做
| 一致性 (consistency|事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的 |
|隔离性 (isolation)|一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的,并发执行的各个事务之间不能互相干扰 |
|     持久性     (durability)                |   持久性也称永久性(permanence),指一个事务一旦提交,它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响               |


```
原子性,要求事务中的所有操作,不可分割,不能做了一部分操作,还剩一部分操作;
一致性,多个事务并行执行的结果,应该和事务排队执行的结果一致。如果事务的并行执行和多线程读写共
享资源一样不可预期,就不能保证一致性。
隔离性,就是指多个事务访问共同的数据了,应该互不干扰。隔离性,指的是究竟在一个事务处理期间,其
他事务能不能访问的问题
持久性,比较好理解,就是事务提交后,数据不能丢失。


隔离性不好,事务的操作就会互相影响,带来不同严重程度的后果。
首先看看隔离性不好,带来哪些问题:
1. 更新丢失Lost Update
事务A和B,更新同一个数据,它们都读取了初始值100,A要减10,B要加100,A减去10后更新为90,B加
100更新为200,A的更新丢失了,就像从来没有减过10一样。
2. 脏读
事务A和B,事务B读取到了事务A未提交的数据(这个数据可能是一个中间值,也可能事务A后来回滚事
务)。事务A是否最后提交并不关心。只要读取到了这个被修改的数据就是脏读。
3. 不可重复读Unrepeatable read
事务A在事务执行中相同查询语句,得到了不同的结果,不能保证同一条查询语句重复读相同的结果就是不可
以重复读。
例如,事务A查询了一次后,事务B修改了数据,事务A又查询了一次,发现数据不一致了。
注意,脏读讲的是可以读到相同的数据的,但是读取的是一个未提交的数据,而不是提交的最终结果。
4. 幻读Phantom read
事务A中同一个查询要进行多次,事务B插入数据,导致A返回不同的结果集,如同幻觉,就是幻读。
数据集有记录增加了,可以看做是增加了记录的不可重复读。



```
## **<font color=Red> MySQL隔离级别**

| 隔离级别            |       描述     |
|:------------------------ |:----------------:|
| READ UNCOMMITTED         |      读取到未提交的数据
| READ COMMITTED|读已经提交的数据,ORACLE默认隔离级别 |
|REPEATABLE READ|可以重复读,MySQL的 默认隔离级别。 |
|    SERIALIZABLE              |  可串行化。事务间完全隔离,事务不能并发,只能串行执行        |



```
隔离级别越高,串行化越高,数据库执行效率低;隔离级别越低,并行度越高,性能越高。
隔离级别越高,当前事务处理的中间结果对其它事务不可见程度越高

-- 设置会话级或者全局隔离级别
SET [SESSION | GLOBAL] TRANSACTION ISOLATION LEVEL
{READ UNCOMMITTED | READ COMMITTED | REPEATABLE READ | SERIALIZABLE}
-- 查询隔离级别
SELECT @@global.tx_isolation;
SELECT @@tx_isolation;
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
-- 禁用自动提交
SET AUTOCOMMIT = 0



```
##  **<font color=Red>数据仓库和数据库**
```

数据仓库和数据库的区别本质上来说没有区别,都是存放数据的地方。
但是数据库关注数据的持久化、数据的关系,为业务系统提供支持,事务支持;
数据仓库存储数据的是为了分析或者发掘而设计的表结构,可以存储海量数据。
数据库存储在线交易数据OLTP(联机事务处理OLTP,On-line Transaction Processing);数据仓库存储历史数据
用于分析OLAP(联机分析处理OLAP,On-Line Analytical Processing)。
数据库支持在线业务,需要频繁增删改查;数据仓库一般囤积历史数据支持用于分析的SQL,一般不建议删改。

```
##  **<font color=Red>pymysql**


- 一般流程
 - 建立连接
 - 获取游标
 - 执行SQL
 - 提交事务
 - 释放资源


 | 参数名称                 |                             含义                              |
| :------------------------ | :-------------------------------------------------------------: |
| fetchone()                | 获取结果集的下一行                                              |
|fetchall()  | 返回剩余所有行,如果走到末尾,就返回空元组,否则返回一个元组,其元素是每一行的记录封装的一个元组                                           |
|         fetchmany(size=None)                  |      size指定返回的行数的行,None则返回组                                                           |
|     cursor.rownumber                      |                      返回当前行号。可以修改,支持负数                                           |
|         cursor.rowcount                  |                     返回的总行数                                            |


注意:fetch操作的是结果集,结果集是保存在客户端的,也就是说fetch的时候,查询已经结束了



```python
import pymysql
ip='192.168.6.2'
user= 'joey'
password = 'joey'
db = 'test'
port = 3306
cursor = None
conn = None
try:
    conn = pymysql.Connect(ip, user, password, db, port)
    cursor = conn.cursor()
    sql = "select * from reg"
    #sql ="insert into reg (id,logginname,name,passwrd) values ('11','ben','ben','ben')"
    r = cursor.execute(sql)
    #cursor = conn.query(sql)
    print(r)
    conn.commit()
except:
    conn.rollback()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

```
### 获取表格元素




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
### 更改

```python
import pymysql
ip='192.168.6.2'
user= 'joey'
password = 'joey'
db = 'test'
port = 3306
cursor = None
conn = None
try:
    conn = pymysql.Connect(ip, user, password, db, port)
    cursor = conn.cursor()
    #sql = "select * from reg"
    #sql ="insert into reg (id,logginname,name,passwrd) values ('11','ben','ben','ben')"
    sql = " select id from reg where logginname='{}'".format('joey')
    r = cursor.execute(sql)
    if r == 1:
        user = cursor.fetchone()
        print(user[0])
        sql = "update reg set name='ben5' where id = '{}'".format(user[0])
        rr = cursor.execute(sql)
        print(rr)
    #cursor = conn.query(sql)

    print(r)
    conn.commit()
except:
    conn.rollback()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~')
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

```
##  **<font color=Red>pymysqls参数化查询　ＳＱＬ注入攻击**

```python

'''
SQL注入攻击
猜测后台数据库的查询语句使用拼接字符串等方式,从而经过设计为服务端传参,令其拼接出特殊字符串的SQL语
句,返回攻击者想要的结果。
永远不要相信客户端传来的数据是规范及安全的!!!
如何解决注入攻击?
参数化查询,可以有效防止注入攻击,并提高查询的效率。
Cursor.execute(query, args=None)
args,必须是元组、列表或字典。如果查询字符串使用%(name)s,就必须使用字典。
'''

import pymysql
conn = None
cursor = None
try:
  conn = pymysql.connect('192.168.142.135', 'wayne', 'wayne', 'school')
  cursor = conn.cursor()
  sql = "insert into student (name, age) values(%s, %s)"
  cursor.executemany(sql, (
  ('jerry{}'.format(i), 30 + i) for i in range(5)))
  conn.commit()
except Exception as e:
  print(e)
  conn.rollback()
finally:
  if cursor:
    cursor.close()
  if conn:
    conn.close()



import pymysql
from pymysql.cursors import DictCursor



ip='192.168.6.2'
user= 'joey'
password = 'joey'
db = 'test'
port = 3306


conn = pymysql.Connect(ip, user, password, db, port)
cursor = conn.cursor(DictCursor)
id = '1 or 1=1'
sql = "select * from reg where id = %s"
print(sql)
r = cursor.execute(sql, (id,))
print(r)
#cursor = conn.query(sql)

#print(cursor.fetchall())

```

##  **<font color=Red>pymysqls上下文参数**
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

##  **<font color=Red>ORM Object Relational Mapping**

```
关系模型和Python对象之间的映射
table => class ,表映射为类
row => object ,行映射为实例
column => property
,字段映射为属性
```



##  **<font color=Red>OSQLAlchemy**

### **<font color=Red>创建连接**

```
dialect+driver://username:password@host:port/database
mysqldb的连接
mysql+mysqldb://<user>:<password>@<host>[:<port>]/<dbname>
engine = sqlalchemy.create_engine("mysql+mysqldb://wayne:wayne@127.0.0.1:3306/magedu")
pymysql的连接
mysql+pymysql://<username>:<password>@<host>/<dbname>[?<options>]
engine = sqlalchemy.create_engine("mysql+pymysql://wayne:wayne@127.0.0.1:3306/magedu")
engine = sqlalchemy.create_engine("mysql+pymysql://wayne:wayne@127.0.0.1:3306/magedu",
echo=True)
echo=True
引擎是否打印执行的语句,调试的时候打开很方便。
lazy connecting:懒连接。创建引擎并不会马上连接数据库,直到让数据库执行任务时才连接。

```

```python

import sqlalchemy
from sqlalchemy import  create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base

#ORM Mapping
Base = declarative_base()

# 创建实体类
class Student(Base):

  '''
  __tablename__ 指定表名
  Column类指定对应的字段,必须指定
  '''

   # 指定表名
    __tablename__ = 'student'
    # 定义类属性对应字段

    id = Column(Integer,primary_key=True,autoincrement=True)#定义字段类型和属性
    name =Column(String(64),nullable=False)
    age = Column(Integer)
    # 第一参数是字段名,如果和属性名不一致,一定要指定
    # age = Column('age', Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__,self.id,self.name,self.age
        )

# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306


engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME),
                                     echo=True) # lazy
print(engine)

#Base.metadata.drop_all(engine)# 从base下管理的表　进行删除操作
Base.metadata.create_all(engine)　＃

/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
Engine(mysql+pymysql://joey:***@192.168.6.2:3306/test)
2020-02-24 00:20:01,996 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2020-02-24 00:20:01,996 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:01,997 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2020-02-24 00:20:01,997 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:01,999 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
2020-02-24 00:20:01,999 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,000 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
2020-02-24 00:20:02,000 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,001 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
2020-02-24 00:20:02,001 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,003 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
2020-02-24 00:20:02,003 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,004 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
2020-02-24 00:20:02,004 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,007 INFO sqlalchemy.engine.base.Engine DESCRIBE `student`
2020-02-24 00:20:02,007 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,008 INFO sqlalchemy.engine.base.Engine
DROP TABLE student
2020-02-24 00:20:02,008 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,010 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 00:20:02,011 INFO sqlalchemy.engine.base.Engine DESCRIBE `student`
2020-02-24 00:20:02,011 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,012 INFO sqlalchemy.engine.base.Engine ROLLBACK
2020-02-24 00:20:02,012 INFO sqlalchemy.engine.base.Engine
CREATE TABLE student (
	id INTEGER NOT NULL AUTO_INCREMENT,
	name VARCHAR(64) NOT NULL,
	age INTEGER,
	PRIMARY KEY (id)
)


2020-02-24 00:20:02,012 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:20:02,014 INFO sqlalchemy.engine.base.Engine COMMIT

Process finished with exit code 0





```

### **<font color=Red>创建会话session**

https://docs.sqlalchemy.org/en/13/orm/tutorial.html

```python
from  sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
sesion = Session() #线程不安全，不能夸线程使用
```
### **<font color=Red>CURD**

```python
import sqlalchemy
from sqlalchemy import  create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

#"mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME),
                                     echo=True) # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
#Base.metadata.drop_all(engine)# 从base
#Base.metadata.create_all(engine)

##################################################################################

#ORM Mapping
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True,autoincrement=True)#定义字段类型和属性
    name =Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__,self.id,self.name,self.age
        )

###############################################
# CREATE SEESION
from sqlalchemy.orm.session import Session
session:Session= sessionmaker(bind=engine)()
#sesion = Session() #线程不安全，不能夸线程使用

print(session,type(session))

student = Student(id=1,name='jerry')
student.name = 'tom'
student.age = 20
print(student)

session.add(student)
session.commit()

try:
    session.add_all([student])
    print(student)
    session.commit() # 提交能成功吗?
    print(student)
    print("---------------------------------------------")
except:
    session.rollback()
    print('roll back')
    raise



    /home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
Engine(mysql+pymysql://joey:***@192.168.6.2:3306/test)
<sqlalchemy.orm.session.Session object at 0x7f2386efa710> <class 'sqlalchemy.orm.session.Session'>
Student id =1,name=tom,age=20
2020-02-24 00:44:13,910 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2020-02-24 00:44:13,910 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,911 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2020-02-24 00:44:13,911 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,912 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
2020-02-24 00:44:13,912 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,913 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
2020-02-24 00:44:13,913 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,914 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
2020-02-24 00:44:13,914 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,915 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
2020-02-24 00:44:13,915 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,916 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
2020-02-24 00:44:13,916 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:44:13,918 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2020-02-24 00:44:13,918 INFO sqlalchemy.engine.base.Engine INSERT INTO student (id, name, age) VALUES (%(id)s, %(name)s, %(age)s)
2020-02-24 00:44:13,918 INFO sqlalchemy.engine.base.Engine {'id': 1, 'name': 'tom', 'age': 20}
2020-02-24 00:44:13,919 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 00:44:13,920 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2020-02-24 00:44:13,921 INFO sqlalchemy.engine.base.Engine SELECT student.id AS student_id, student.name AS student_name, student.age AS student_age
FROM student
WHERE student.id = %(param_1)s
2020-02-24 00:44:13,921 INFO sqlalchemy.engine.base.Engine {'param_1': 1}
Student id =1,name=tom,age=20
2020-02-24 00:44:13,922 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 00:44:13,922 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2020-02-24 00:44:13,923 INFO sqlalchemy.engine.base.Engine SELECT student.id AS student_id, student.name AS student_name, student.age AS student_age
FROM student
WHERE student.id = %(param_1)s
2020-02-24 00:44:13,923 INFO sqlalchemy.engine.base.Engine {'param_1': 1}
Student id =1,name=tom,age=20
---------------------------------------------

Process finished with exit code 0

import sqlalchemy
from sqlalchemy import  create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

#"mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME),
                                     echo=True) # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
#Base.metadata.drop_all(engine)# 从base
#Base.metadata.create_all(engine)

##################################################################################

#ORM Mapping
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True,autoincrement=True)#定义字段类型和属性
    name =Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__,self.id,self.name,self.age
        )

###############################################
# CREATE SEESION
from sqlalchemy.orm.session import Session
session:Session= sessionmaker(bind=engine)()
#sesion = Session() #线程不安全，不能夸线程使用

print(session,type(session))

student = Student()
student.name = 'ben'
student.age = 20
print(student)

session.add(student)
session.commit()

try:
    student.name='ben'
    session.add_all([student])
    print(student)
    session.commit() # 提交能成功吗?
    print(student)
    print("---------------------------------------------")
except:
    session.rollback()
    print('roll back')
    raise


/home/joey/python/code/venv/bin/python /home/joey/python/code/t1.py
Engine(mysql+pymysql://joey:***@192.168.6.2:3306/test)
<sqlalchemy.orm.session.Session object at 0x7f4230b15710> <class 'sqlalchemy.orm.session.Session'>
Student id =None,name=ben,age=20
2020-02-24 00:47:00,073 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'sql_mode'
2020-02-24 00:47:00,073 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,074 INFO sqlalchemy.engine.base.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2020-02-24 00:47:00,074 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,077 INFO sqlalchemy.engine.base.Engine SELECT DATABASE()
2020-02-24 00:47:00,077 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,078 INFO sqlalchemy.engine.base.Engine show collation where `Charset` = 'utf8mb4' and `Collation` = 'utf8mb4_bin'
2020-02-24 00:47:00,078 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,079 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS CHAR(60)) AS anon_1
2020-02-24 00:47:00,079 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,080 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS CHAR(60)) AS anon_1
2020-02-24 00:47:00,080 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,081 INFO sqlalchemy.engine.base.Engine SELECT CAST('test collated returns' AS CHAR CHARACTER SET utf8mb4) COLLATE utf8mb4_bin AS anon_1
2020-02-24 00:47:00,081 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 00:47:00,082 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2020-02-24 00:47:00,083 INFO sqlalchemy.engine.base.Engine INSERT INTO student (name, age) VALUES (%(name)s, %(age)s)
2020-02-24 00:47:00,083 INFO sqlalchemy.engine.base.Engine {'name': 'ben', 'age': 20}
2020-02-24 00:47:00,084 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 00:47:00,086 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2020-02-24 00:47:00,087 INFO sqlalchemy.engine.base.Engine SELECT student.id AS student_id, student.age AS student_age
FROM student
WHERE student.id = %(param_1)s
2020-02-24 00:47:00,087 INFO sqlalchemy.engine.base.Engine {'param_1': 2}
Student id =2,name=ben,age=20
2020-02-24 00:47:00,088 INFO sqlalchemy.engine.base.Engine UPDATE student SET name=%(name)s WHERE student.id = %(student_id)s
2020-02-24 00:47:00,088 INFO sqlalchemy.engine.base.Engine {'name': 'ben', 'student_id': 2}
2020-02-24 00:47:00,089 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 00:47:00,090 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2020-02-24 00:47:00,091 INFO sqlalchemy.engine.base.Engine SELECT student.id AS student_id, student.name AS student_name, student.age AS student_age
FROM student
WHERE student.id = %(param_1)s
2020-02-24 00:47:00,091 INFO sqlalchemy.engine.base.Engine {'param_1': 2}
Student id =2,name=ben,age=20
---------------------------------------------

Process finished with exit code 0




```


### **<font color=Red> 查**

```python
import sqlalchemy
from sqlalchemy import  create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

#"mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME),
                                     echo=True) # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
#Base.metadata.drop_all(engine)# 从base
#Base.metadata.create_all(engine)

##################################################################################

#ORM Mapping
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True,autoincrement=True)#定义字段类型和属性
    name =Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__,self.id,self.name,self.age
        )

###############################################
# CREATE SEESION
from sqlalchemy.orm.session import Session
session:Session= sessionmaker(bind=engine)()
#sesion = Session() #线程不安全，不能夸线程使用

print(session,type(session))

from sqlalchemy.ext.declarative.api import DeclarativeMeta
students:DeclarativeMeta = session.query(Student)#  全表查询
print(len(list(students)))
print(students.count()) #虽然查了，但是使用了查询，效率一般
# SELECT count(*) AS count_1
# FROM (SELECT student.id AS student_id, student.name AS student_name, student.age AS student_age
# FROM student) AS anon_1

# for student in students:
#     print(student)

```

### **<font color=Red> 改**

```python
import sqlalchemy
from sqlalchemy import  create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

#"mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME),
                                     echo=True) # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
#Base.metadata.drop_all(engine)# 从base
#Base.metadata.create_all(engine)

##################################################################################

#ORM Mapping
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True,autoincrement=True)#定义字段类型和属性
    name =Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__,self.id,self.name,self.age
        )

###############################################
# CREATE SEESION
from sqlalchemy.orm.session import Session
session:Session= sessionmaker(bind=engine)()
#sesion = Session() #线程不安全，不能夸线程使用

#student = Student(id=2,name='ben',age=20)
student= session.query(Student).get(2) #先查后改动
student.age = 18
student.name = 'jerry'

session.add(student)


try:
    session.commit()
    print("commit ok")
except:
    session.rollback()
    print("rollback ok")

```
### **<font color=Red> 删除**

```python
import sqlalchemy
from sqlalchemy import  create_engine,Column,String,Integer
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy.orm import sessionmaker

#"mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,IP,PORT,DBNAME),
                                     echo=True) # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
#Base.metadata.drop_all(engine)# 从base
#Base.metadata.create_all(engine)

##################################################################################

#ORM Mapping
Base = declarative_base()


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer,primary_key=True,autoincrement=True)#定义字段类型和属性
    name =Column(String(64),nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__,self.id,self.name,self.age
        )

###############################################
# CREATE SEESION
from sqlalchemy.orm.session import Session
session:Session= sessionmaker(bind=engine)()
#sesion = Session() #线程不安全，不能夸线程使用

#student = Student(id=2,name='jerry',age=18)
student= session.query(Student).get(2) #先查后改动.
# student.age = 18
# student.name = 'jerry'

session.delete(student)


try:
    session.commit()
    print("commit ok")
except:
    session.rollback()
    print("rollback ok")

```



### **<font color=Red> 状态****



 | 状态                 |                             说明                            |
| :------------------------ | :-------------------------------------------------------------: |
| transient                | 实体类尚未加入到session中,同时并没有保存到数据库中                                            |
|pending | transient的实体被add()到session中,状态切换到pending,但它还没有flush到数据库中                                          |
| fetchmany(size=None) | size指定返回的行数的行,None则返回组                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| persister            | session中的实体对象对应着数据库中的真实记录。pending状态在提交成功后可以变成 persistent状态,或者查询成功返回的实体也是persistent状态 |
| deleted              | 实体被删除且已经flush但未commit完成。事务提交成功了,实体变成detached,事务失败返回persistent状态                                      |
| detacheddetached     | 删除成功的实体进入这个状态                                                                                                           |                     |                                                                                                                                      |

```python
新建一个实体,状态是transient临时的。
一旦add()后从transient变成pending状态。
成功commit()后从pending变成persistent状态。
成功查询返回的实体对象,也是persistent状态。
persistent状态的实体,修改依然是persistent状态。
persistent状态的实体,删除后,flush后但没有commit,就变成deteled状态,成功提交,变为detached状态,
提交失败,还原到persistent状态。flush方法,主动把改变应用到数据库中去。
删除、修改操作,需要对应一个真实的记录,所以要求实体对象是persistent状态。


import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
connstr = "{}://{}:{}@{}:{}/{}".format(
'mysql+pymysql', 'wayne', 'wayne',
'192.168.142.140', 3306, 'test'
)
engine = create_engine(connstr, echo=True)
Base = declarative_base()
# 创建实体类
class Student(Base):
    # 指定表名
    __tablename__ = 'student'
    # 定义属性对应字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer)
    # 第一参数是字段名,如果和属性名不一致,则一定要指定
    # age = Column('age', Integer)

    def __repr__(self):
        return "{} id={} name={} age={}".format(self.__class__.__name__, self.id, self.name, self.age)


Session = sessionmaker(bind=engine)
session = Session()
from sqlalchemy.orm.state import InstanceState
def getstate(instance, i):
    inp:InstanceState = sqlalchemy.inspect(student)
    states = "{}: key={}\nsid={}, attached={}, transient={}, " \
    "pending={}, \npersistent={}, deleted={}, detached={}".format(
    i, inp.key,
    inp.session_id, inp._attached, inp.transient,
    inp.pending, inp.persistent, inp.deleted, inp.detached
    )
    print(states, end='\n------------------------\n')


student = session.query(Student).get(2)
getstate(student, 1) # persistent

try:
    student = Student(id=2, name='sam', age=30)
    getstate(student, 2) # transit
    student = Student(name='sammy', age=30)
    getstate(student, 3) # transient
    session.add(student) # add后变成pending
    getstate(student, 4) # pending
    # session.delete(student) # 异常,删除的前提必须是persistent,也就是说先查后删
    # getstate(student, 5)
    session.commit() # 提交后,变成persistent
    getstate(student, 6) # persistent
except Exception as e:
    session.rollback()
    print(e, '~~~~~~~~~~~~~~~~')


# 运行结果
1: key=(<class '__main__.Student'>, (2,), None)
sid=1, attached=True, transient=False, pending=False,
persistent=True, deleted=False, detached=False
persistent就是key不为None,附加的,且不是删除的,有sessionid
------------------------
2: key=None
sid=None, attached=False, transient=True, pending=False,
persistent=False, deleted=False, detached=False
transient的key为None,且无附加
------------------------
3: key=None
sid=None, attached=False, transient=True, pending=False,
persistent=False, deleted=False, detached=False
同上
------------------------------
4: key=None
sid=1, attached=True, transient=False, pending=True,
persistent=False, deleted=False, detached=False
add后变成pending,已附加,但是没有key,有了sessionid
------------------------------
sqlalchemy.engine.base.Engine COMMIT
6: key=(<class '__main__.Student'>, (3,), None)
sid=1, attached=True, transient=False, pending=False,
persistent=True, deleted=False, detached=False
提交成功后,变成persistent,有了key
------------------------------
```
```python
每一个实体,都有一个状态属性_sa_instance_state,其类型是sqlalchemy.orm.state.InstanceState,可以使用
sqlalchemy.inspect(entity)函数查看状态。
常见的状态值有transient、pending、persistent、deleted、detached。

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
# Base.metadata.drop_all(engine)# 从base
# Base.metadata.create_all(engine)

##################################################################################

# ORM Mapping
Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__, self.id, self.name, self.age
        )


###############################################
# CREATE SEESION
from sqlalchemy.orm.session import Session

session: Session = sessionmaker(bind=engine)()
# sesion = Session() #线程不安全，不能夸线程使用

from sqlalchemy.orm.state import InstanceState


def getstate(instance, i):
    state: InstanceState = sqlalchemy.inspect(student)
    output = " {} :{}:{}\n" \
             "_attached={},transient={},pending={}\n" \
             "persistent={},deleted={},detached:{}\n".format(i, state.key, state.session_id,
             state._attached, state.transient, state.pending,
             state.persistent, state.deleted, state.detached

                                                             )
    print(output, end='----------------\n')


student = Student(id=2, name='ben', age=20) # 自定义的实例
print(student.__dict__)  # {'_sa_instance_state': <sqlalchemy.orm.state.InstanceState object at 0x00000260BCCDB948>, 'id': 2, 'name': 'ben', 'age': 20}
getstate(student, 0)

#  0 :None:None
# _attached=False,transient=True,pending=False
# persistent=False,deleted=False,detached:False

student = session.query(Student).get(1) #获取数据库的实例
getstate(student,1)

#  1 :(<class '__main__.Student'>, (1,), None):1
# _attached=True,transient=False,pending=False
# persistent=True,deleted=False,detached:False
```
### **<font color=Red> 复杂查询**
```python
#查询所有的ｒｅｃｏｒｄ
emps = session.query(Employee)

SELECT
	employees.emp_no AS employees_emp_no,
	employees.birth_date AS employees_birth_date,
	employees.first_name AS employees_first_name,
	employees.last_name AS employees_last_name,
	employees.gender AS employees_gender,
	employees.hire_date AS employees_hire_date
FROM
	employees

## and
#1
emps = session.query(Employee).filter(Employee.emp_no > 10015,Employee.emp_no < 10018)
show(emps)
#2
emps = session.query(Employee).filter(Employee.emp_no > 10015).filter(Employee.emp_no < 10018)
show(emps)

#3
from sqlalchemy import and_,or_,not_
emps = session.query(Employee).filter(and_(Employee.emp_no > 10015,Employee.emp_no < 10018))
show(emps)

#4
emps = session.query(Employee).filter((Employee.emp_no > 10015) & (Employee.emp_no < 10018))
show(emps)

＃　或者
from sqlalchemy import and_,or_,not_
emps = session.query(Employee).filter(or_(Employee.emp_no == 10015,Employee.emp_no == 10018))
show(emps)

emps = session.query(Employee).filter((Employee.emp_no == 10015) | (Employee.emp_no == 10018))
show(emps)


＃　not
emps = session.query(Employee).filter(~(Employee.emp_no < 10015))
show(emps)

emps = session.query(Employee).filter(not_(Employee.emp_no < 10015))
show(emps)


import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
# Base.metadata.drop_all(engine)# 从base
# Base.metadata.create_all(engine)

##################################################################################

# ORM Mapping
Base = declarative_base()
import enum
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__, self.id, self.name, self.age
        )


class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<{} no ={},birth_date={},first_name={},last_name={},gender={},hird_date={}".format(
            __class__.__name__, self.emp_no, self.birth_date, self.first_name,self.last_name,self.gender.value,self.hire_date
        )

from sqlalchemy.orm.session import Session

session: Session = sessionmaker(bind=engine)()
# sesion = Session() #线程不安全，不能夸线程使用
def show(emps):
    for i in emps:
        print(i)
    print(end='\n\n')


from sqlalchemy import and_,or_,not_
emps = session.query(Employee).filter(~(Employee.emp_no < 10015))
show(emps)

emps = session.query(Employee).filter(not_(Employee.emp_no < 10015))
show(emps)

# or
#
# emps = session.query(Employee).filter(or_(Employee.emp_no == 10015,Employee.emp_no == 10018))
# show(emps)
#
# emps = session.query(Employee).filter((Employee.emp_no == 10015) | (Employee.emp_no == 10018))
# show(emps)


# emps = session.query(Employee)
# show(emps)

# emps = session.query(Employee).filter(Employee.emp_no > 10015)
# print(emps)
# show(emps)
#
# ## and
# #1
# emps = session.query(Employee).filter(Employee.emp_no > 10015,Employee.emp_no < 10018)
# show(emps)
# #2
# emps = session.query(Employee).filter(Employee.emp_no > 10015).filter(Employee.emp_no < 10018)
# show(emps)
#
# #3
# from sqlalchemy import and_,or_,not_
# emps = session.query(Employee).filter(and_(Employee.emp_no > 10015,Employee.emp_no < 10018))
# show(emps)
#
# #4
# emps = session.query(Employee).filter((Employee.emp_no > 10015) & (Employee.emp_no < 10018))
# show(emps)

```


```python
# in
emplist = [10010, 10015, 10018]
emps = session.query(Employee).filter(Employee.emp_no.in_(emplist))
show(emps)
# not in
emps = session.query(Employee).filter(~Employee.emp_no.in_(emplist))
emps = session.query(Employee).filter(Employee.emp_no.notin_(emplist))
show(emps)

# like
emps = session.query(Employee).filter(Employee.last_name.like('P%'))
show(emps)
# not like
emps = session.query(Employee).filter(Employee.last_name.notlike('P%'))
# ilike可以忽略大小写匹配

# 排序

def show(emps):
    for i in emps:
        print(i)
    print(end='\n\n')


emps = session.query(Employee).filter(Employee.last_name.like('%M%'))
show(emps.order_by(Employee.emp_no))
show(emps.order_by(Employee.emp_no.desc(),Employee.gender.desc()))
show(emps.order_by(Employee.emp_no.desc()).order_by(Employee.gender.desc()))

``


```python

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
# Base.metadata.drop_all(engine)# 从base
# Base.metadata.create_all(engine)

##################################################################################

# ORM Mapping
Base = declarative_base()
import enum
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__, self.id, self.name, self.age
        )


class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<{} no ={},birth_date={},first_name={},last_name={},gender={},hird_date={}>".format(
            __class__.__name__, self.emp_no, self.birth_date, self.first_name,self.last_name,self.gender.value,self.hire_date
        )

from sqlalchemy.orm.session import Session

session: Session = sessionmaker(bind=engine)()
# sesion = Session() #线程不安全，不能夸线程使用
def show(emps):
    for i in emps:
        print(i)
    print(end='\n\n')


emps = session.query(Employee).filter(Employee.last_name.like('%M%'))
print("--------------------------")
print(type(emps))
show(emps.order_by(Employee.emp_no))
show(emps.order_by(Employee.emp_no.desc(),Employee.gender.desc()))
emps = emps.order_by(Employee.emp_no.desc()).order_by(Employee.gender.desc())
emps = emps.limit(2).offset(2)
show(emps)
print(emps.all())#列表,没有查到返回空列表
print(emps.first()) #一个对象,没有查到返回none
print(emps.count())#0-n

#print(emps.one())#sqlalchemy.orm.exc.MultipleResultsFound: Multiple rows were found for one() 多余一个　抛异常, 少于一行　跑异常

#in
# emps = session.query(Employee).filter(Employee.emp_no.in_([10015,10018,10020]))
# show(emps)
#from sqlalchemy import and_,or_,not_
# emps = session.query(Employee).filter(~(Employee.emp_no < 10015))
# show(emps)
#
# emps = session.query(Employee).filter(not_(Employee.emp_no < 10015))
# show(emps)

# or
#
# emps = session.query(Employee).filter(or_(Employee.emp_no == 10015,Employee.emp_no == 10018))
# show(emps)
#
# emps = session.query(Employee).filter((Employee.emp_no == 10015) | (Employee.emp_no == 10018))
# show(emps)


# emps = session.query(Employee)
# show(emps)

# emps = session.query(Employee).filter(Employee.emp_no > 10015)
# print(emps)
# show(emps)
#
# ## and
# #1
# emps = session.query(Employee).filter(Employee.emp_no > 10015,Employee.emp_no < 10018)
# show(emps)
# #2
# emps = session.query(Employee).filter(Employee.emp_no > 10015).filter(Employee.emp_no < 10018)
# show(emps)
#
# #3
# from sqlalchemy import and_,or_,not_
# emps = session.query(Employee).filter(and_(Employee.emp_no > 10015,Employee.emp_no < 10018))
# show(emps)
#
# #4
# emps = session.query(Employee).filter((Employee.emp_no > 10015) & (Employee.emp_no < 10018))
# show(emps)

```

### **<font color=Red> 聚合**

```python

import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
# Base.metadata.drop_all(engine)# 从base
# Base.metadata.create_all(engine)

##################################################################################

# ORM Mapping
Base = declarative_base()
import enum
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__, self.id, self.name, self.age
        )


class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<{} no ={},birth_date={},first_name={},last_name={},gender={},hird_date={}>".format(
            __class__.__name__, self.emp_no, self.birth_date, self.first_name,self.last_name,self.gender.value,self.hire_date
        )

from sqlalchemy.orm.session import Session

session: Session = sessionmaker(bind=engine)()
# sesion = Session() #线程不安全，不能夸线程使用
def show(emps):
    for i in emps:
        print(i)
    print(end='\n\n')

from sqlalchemy import func

emps = session.query(func.count(Employee.emp_no),func.max(Employee.emp_no))

print(emps.all())
print(emps.first())
print(emps.one())
print(emps.scalar())


```

### **<font color=Red> 分组**

```python
import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Date,Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))
# Base.metadata.drop_all(engine)# 从base
# Base.metadata.create_all(engine)

##################################################################################

# ORM Mapping
Base = declarative_base()
import enum
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Student(Base):

    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{} id ={},name={},age={}".format(

            __class__.__name__, self.id, self.name, self.age
        )


class Employee(Base):

    __tablename__ = 'employees'

    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<{} no ={},birth_date={},first_name={},last_name={},gender={},hird_date={}>".format(
            __class__.__name__, self.emp_no, self.birth_date, self.first_name,self.last_name,self.gender.value,self.hire_date
        )

from sqlalchemy.orm.session import Session

session: Session = sessionmaker(bind=engine)()
# sesion = Session() #线程不安全，不能夸线程使用
def show(emps):
    for i in emps:
        print(i)
    print(end='\n\n')

from sqlalchemy import func

emps = session.query(Employee.gender,func.count(Employee.emp_no),func.max(Employee.emp_no))
emps = emps.group_by(Employee.emp_no)

print(emps.all())
print(emps.first())
#print(emps.one())
#print(emps.scalar())

```

### **<font color=Red> 关联查询*

```python
import sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer,Date,Enum,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# "mysql+pymysql://username:password@ip:port/dbname"

IP = '192.168.6.2'
USERNAME = 'joey'
PASSWORD = 'joey'
DBNAME = 'test'
PORT = 3306

engine = create_engine("mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME, PASSWORD, IP, PORT, DBNAME),
                       echo=True)  # lazy
print(engine)
# print(Student.__dict__)
# print(Student.__table__)
# print(repr(Student.__table__))


##################################################################################

# ORM Mapping
Base = declarative_base()
import enum
class GenderEnum(enum.Enum):
    M = 'M'
    F = 'F'


# class Student(Base):
#
#     __tablename__ = 'student'
#
#     id = Column(Integer, primary_key=True, autoincrement=True)  # 定义字段类型和属性
#     name = Column(String(64), nullable=False)
#     age = Column(Integer)
#
#     def __repr__(self):
#         return "{} id ={},name={},age={}".format(
#
#             __class__.__name__, self.id, self.name, self.age
#         )


class Employee(Base):

    __tablename__ = 'employees1'

    emp_no = Column(Integer,primary_key=True)
    birth_date = Column(Date,nullable=False)
    first_name = Column(String(14),nullable=False)
    last_name = Column(String(16),nullable=False)
    gender = Column(Enum(GenderEnum),nullable=False)
    hire_date = Column(Date,nullable=False)

    def __repr__(self):
        return "<{} no ={},birth_date={},first_name={},last_name={},gender={},hird_date={}>".format(
            __class__.__name__, self.emp_no, self.birth_date, self.first_name,self.last_name,self.gender.value,self.hire_date
        )

class Departments(Base):

    __tablename__ = 'departments1'

    dept_no = Column(String(4),primary_key=True)
    dept_name = Column(String(40),nullable=False,unique=True)

    def __repr__(self):
        return "<{} dept_no ={},dept_name={}>".format(
            __class__.__name__, self.dept_no, self.dept_name
        )


class Dept_emp(Base):
    __tablename__ = 'dept_emp1'

    emp_no = Column(Integer,ForeignKey('employees1.emp_no',ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String(4),ForeignKey('departments1.dept_no',ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "<{} emp_no ={},dept_no={},>".format(
            __class__.__name__, self.emp_no, self.dept_no
        )


Base.metadata.drop_all(engine)# 从base
Base.metadata.create_all(engine)
'''
CREATE TABLE employees1 (
	emp_no INTEGER NOT NULL AUTO_INCREMENT,
	birth_date DATE NOT NULL,
	first_name VARCHAR(14) NOT NULL,
	last_name VARCHAR(16) NOT NULL,
	gender ENUM('M','F') NOT NULL,
	hire_date DATE NOT NULL,
	PRIMARY KEY (emp_no)
)


2020-02-24 22:42:01,039 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 22:42:01,042 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 22:42:01,042 INFO sqlalchemy.engine.base.Engine
CREATE TABLE departments1 (
	dept_no VARCHAR(4) NOT NULL,
	dept_name VARCHAR(40) NOT NULL,
	PRIMARY KEY (dept_no),
	UNIQUE (dept_name)
)


2020-02-24 22:42:01,042 INFO sqlalchemy.engine.base.Engine {}
2020-02-24 22:42:01,044 INFO sqlalchemy.engine.base.Engine COMMIT
2020-02-24 22:42:01,045 INFO sqlalchemy.engine.base.Engine
CREATE TABLE dept_emp1 (
	emp_no INTEGER NOT NULL,
	dept_no VARCHAR(4) NOT NULL,
	from_date DATE NOT NULL,
	to_date DATE NOT NULL,
	PRIMARY KEY (emp_no, dept_no),
	FOREIGN KEY(emp_no) REFERENCES employees1 (emp_no) ON DELETE CASCADE,
	FOREIGN KEY(dept_no) REFERENCES departments1 (dept_no) ON DELETE CASCADE
)
'''

```
