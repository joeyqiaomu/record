### **<font color=Red>用户账号**
- mysql用户账号由两部分组成:
'USERNAME'@'HOST‘
- 说明:
HOST限制此用户可通过哪些远程主机连接mysql服务器
支持使用通配符:
 - % 匹配任意长度的任意字符
172.16.0.0/255.255.0.0 或 172.16.%.%
 - _ 匹配任意单个字符


 - MairaDB配置
 - 侦听3306/tcp端口可以在绑定有一个或全部接口IP上
 - vim /etc/my.cnf
[mysqld]
skip-networking=1
- 关闭网络连接,只侦听本地客户端, 所有和服务器的交互都通过一个socket实
现,socket的配置存放在/var/lib/mysql/mysql.sock) 可在/etc/my.cnf修改


### **<font color=Red>通用二进制格式安装过程**


```

 二进制格式安装过程
 (1) 准备用户
  groupadd -r -g 306 mysql
  useradd -r -g 306 -u 306 –d /data/mysql mysql
 (2) 准备数据目录,建议使用逻辑卷
  mkdir /data/mysql
  chown mysql:mysql /data/mysql
 (3) 准备二进制程序
  tar xf mariadb-VERSION-linux-x86_64.tar.gz -C /usr/local
  cd /usr/local
  ln -sv mariadb-VERSION mysql
  chown -R root:mysql /usr/local/mysql/
  (4) 准备配置文件
mkdir /etc/mysql/
cp support-files/my-large.cnf /etc/mysql/my.cnf
[mysqld]中添加三个选项:
datadir = /data/mysql
innodb_file_per_table = on
skip_name_resolve = on 禁止主机名解析,建议使用
(5)创建数据库文件
cd /usr/local/mysql/
./scripts/mysql_install_db --datadir=/data/mysql --user=mysql
 (6)准备服务脚本,并启动服务
cp ./support-files/mysql.server /etc/rc.d/init.d/mysqld
chkconfig --add mysqld
service mysqld start
 (7)PATH路径
echo ‘PATH=/user/local/mysql/bin:$PATH’ > /etc/profile.d/mysql
 (8)安全初始化
/user/local/mysql/bin/mysql_secure_installation


```
# **<font color=Red>源码编译安装mariadb**


```

```


## **<font color=Red> SQL语句构成**



- SQL语句构成:
Keyword组成clause
多条clause组成语句
 示例:
SELECT *
SELECT子句
FROM products
FROM子句
WHERE price>400
WHERE子句
说明:一组SQL语句,由三个子句构成,SELECT,FROM和WHERE是关键字
## **<font color=Red> SQL语句分类:**
- DDL: Data Defination Language 数据定义语言
CREATE,DROP,ALTER
- DML: Data Manipulation Language 数据操纵语言
INSERT,DELETE,UPDATE
- DCL:Data Control Language 数据控制语言
GRANT,REVOKE,COMMIT,ROLLBACK
- DQL:Data Query Language 数据查询语言
SELECT


### **<font color=Red> 创建database**

```
创建数据库:
CREATE DATABASE|SCHEMA [IF NOT EXISTS] 'DB_NAME';
CHARACTER SET 'character set name’COLLATE 'collate name'
- 修改数据库:
ALTER DATABASE DB_NAME character set utf8;
 删除数据库
DROP DATABASE|SCHEMA [IF EXISTS] 'DB_NAME';
 查看支持所有字符集:SHOW CHARACTER SET;
 查看支持所有排序规则:SHOW COLLATION;
获取命令使用帮助:
mysql> HELP KEYWORD;
查看数据库列表:
mysql> SHOW DATABASES;
```
### **<font color=Red> 创建table -hlep create table;**

```

MySql支持多种列类型:
　数值类型
　日期/时间类型
　字符串(字符)类型
https://dev.mysql.com/doc/refman/8.0/en/data-types.html

修饰符
　 所有类型:　
• NULL　数据列可包含NULL值
• NOT NULL　数据列不允许包含NULL值
• DEFAULT　默认值
• PRIMARY KEY　主键
• UNIQUE KEY　唯一键
• CHARACTER SET name　　指定一个字符集
　数值型
• AUTO_INCREMENT　自动递增,适用于整数类型
• UNSIGNED　无符号

－－－－－－－－－－－－－－－－－－－－－－－－－添加表

MariaDB [test1]> create table  student(id int unsigned auto_increment primary key ,name varchAR(20) not null,gender ENUM('m','f') default 'm',mobile char(11) );
Query OK, 0 rows affected (0.11 sec)

MariaDB [test1]> desc student；
+--------+------------------+------+-----+---------+----------------+
| Field  | Type             | Null | Key | Default | Extra          |
+--------+------------------+------+-----+---------+----------------+
| id     | int(10) unsigned | NO   | PRI | NULL    | auto_increment |
| name   | varchar(20)      | NO   |     | NULL    |                |
| gender | enum('m','f')    | YES  |     | m       |                |
| mobile | char(11)         | YES  |     | NULL    |                |
+--------+------------------+------+-----+---------+----------------+
4 rows in set (0.00 sec)

MariaDB [test1]>

MariaDB [test1]> show create table student;
+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table   | Create Table                                                                                                                                                                                                                                 |
+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| student | CREATE TABLE `student` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `gender` enum('m','f') DEFAULT 'm',
  `mobile` char(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)

MariaDB [test1]>

MariaDB [test1]>  show index from student;
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table   | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| student |          0 | PRIMARY  |            1 | id          | A         |           0 |     NULL | NULL   |      | BTREE      |         |               |
+---------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
1 row in set (0.00 sec)

修改表示例
 ALTER TABLE students RENAME s1;
 ALTER TABLE s1 ADD phone varchar(11) AFTER name;
 ALTER TABLE s1 MODIFY phone int;
 ALTER TABLE s1 CHANGE COLUMN phone mobile char(11);
 ALTER TABLE s1 DROP COLUMN mobile;
 ALTER TABLE s1 character set utf8;
 ALTER TABLE s1 change name name varchar(20) character set utf8;
 Help ALTER TABLE 查看帮助


MariaDB [test1]> insert student(name,mobile,gender)values('tom','13498855456','f')
    -> ;
Query OK, 1 row affected (0.00 sec)

MariaDB [test1]> select * from student;
+----+----------+--------+-------------+
| id | name     | gender | mobile      |
+----+----------+--------+-------------+
|  1 | joey     | m      | 13492039456 |
|  2 | jerry    | m      | 13492055456 |
|  3 | xiaoming | m      | 123456677   |
|  4 | tom      | f      | 13498855456 |
+----+----------+--------+-------------+
4 rows in set (0.00 sec)

------------查看变量信息

MariaDB [(none)]> show variables like "%chara%";
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8                       |
| character_set_connection | utf8                       |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | utf8                       |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)

MariaDB [(none)]>



查看所有的引擎:SHOW ENGINES
　　查看表:SHOW TABLES [FROM db_name]
　　查看表结构:DESC [db_name.]tb_name
　　SHOW COLUMNS FROM [db_name.]tb_name
　　删除表:DROP TABLE [IF EXISTS] tb_name
　　查看表创建命令:SHOW CREATE TABLE tbl_name
　　查看表状态:SHOW TABLE STATUS LIKE 'tbl_name’
　　查看库中所有表状态:SHOW TABLE STATUS FROM db_name


ＤＭＬ　语句DML: INSERT, DELETE, UPDATE




```


## **<font color=Red> SQL语句构成－select**


```
SELECT
[ALL | DISTINCT | DISTINCTROW ]
[SQL_CACHE | SQL_NO_CACHE]
select_expr [, select_expr ...]
[FROM table_references
[WHERE where_condition]
[GROUP BY {col_name | expr | position}
[ASC | DESC], ... [WITH ROLLUP]]
[HAVING where_condition]
[ORDER BY {col_name | expr | position}
[ASC | DESC], ...]
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
[FOR UPDATE | LOCK IN SHARE MODE]

MariaDB [(none)]> select 'hello';
+-------+
| hello |
+-------+
| hello |
+-------+
1 row in set (0.000 sec)

MariaDB [(none)]> select 2*3;
+-----+
| 2*3 |
+-----+
|   6 |
+-----+
1 row in set (0.000 sec)

MariaDB [(none)]> show databases;
+--------------------+
| Database           |
+--------------------+
| hellodb            |
| information_schema |
| mysql              |
| performance_schema |
+--------------------+

字段显示可以使用别名:
col1 AS alias1, col2 AS alias2, ...
 WHERE子句:指明过滤条件以实现“选择”的功能:
过滤条件:布尔型表达式
算术操作符:+, -, *, /, %
比较操作符:=,<=>(相等或都为空), <>, !=(非标准SQL), >, >=, <, <=
BETWEEN min_num AND max_num
IN (element1, element2, ...)
IS NULL
IS NOT NULL

MariaDB [hellodb]> desc students;
+-----------+---------------------+------+-----+---------+----------------+
| Field     | Type                | Null | Key | Default | Extra          |
+-----------+---------------------+------+-----+---------+----------------+
| StuID     | int(10) unsigned    | NO   | PRI | NULL    | auto_increment |
| Name      | varchar(50)         | NO   |     | NULL    |                |
| Age       | tinyint(3) unsigned | NO   |     | NULL    |                |
| Gender    | enum('F','M')       | NO   |     | NULL    |                |
| ClassID   | tinyint(3) unsigned | YES  |     | NULL    |                |
| TeacherID | int(10) unsigned    | YES  |     | NULL    |                |
+-----------+---------------------+------+-----+---------+----------------+
6 rows in set (0.001 sec)


MariaDB [hellodb]>
MariaDB [hellodb]> select * from students;
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |
+-------+---------------+-----+--------+---------+-----------+
25 rows in set (0.125 sec)

MariaDB [hellodb]> select * from students where stuid >=20;
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |
+-------+---------------+-----+--------+---------+-----------+
6 rows in set (0.000 sec)

MariaDB [hellodb]> select * from students where stuid =20;
+-------+-----------+-----+--------+---------+-----------+
| StuID | Name      | Age | Gender | ClassID | TeacherID |
+-------+-----------+-----+--------+---------+-----------+
|    20 | Diao Chan |  19 | F      |       7 |      NULL |
+-------+-----------+-----+--------+---------+-----------+
1 row in set (0.000 sec)

MariaDB [hellodb]> select * from students where stuid !=20;
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |
+-------+---------------+-----+--------+---------+-----------+
24 rows in set (0.000 sec)

MariaDB [hellodb]> select * from students where name='xi ren';
+-------+--------+-----+--------+---------+-----------+
| StuID | Name   | Age | Gender | ClassID | TeacherID |
+-------+--------+-----+--------+---------+-----------+
|     7 | Xi Ren |  19 | F      |       3 |      NULL |
+-------+--------+-----+--------+---------+-----------+
1 row in set (0.000 sec)

MariaDB [hellodb]>


MariaDB [hellodb]> select * from students where age >= 10 and gender='f';
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
+-------+---------------+-----+--------+---------+-----------+
10 rows in set (0.000 sec)

MariaDB [hellodb]>

-----------------------------------------密码攻击


MariaDB [hellodb]> select * from user where username='admin' and password='' or '1'='1';
+------+----------+----------+
| id   | username | password |
+------+----------+----------+
|    1 | magedu   | magedu   |
|    1 | centos   | centos   |
+------+----------+----------+
2 rows in set (0.000 sec)

MariaDB [hellodb]>
MariaDB [hellodb]> select * from user where username='admin'--' and password=''';
+------+----------+----------+
| id   | username | password |
+------+----------+----------+
|    1 | magedu   | magedu   |
|    1 | centos   | centos   |
+------+----------+----------+
2 rows in set, 4 warnings (0.000 sec)

MariaDB [hellodb]>


MariaDB [hellodb]> select * from students where age between 20 and 30;
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |
+-------+---------------+-----+--------+---------+-----------+
12 rows in set (0.000 sec)


DISTINCT 去除重复列
SELECT DISTINCT gender FROM students;　－－－DISTINCT　
　LIKE:
%　任意长度的任意字符
_
任意单个字符
　　RLIKE:正则表达式,索引失效,不建议使用
　　 REGEXP:匹配字符串可用正则表达式书写模式,同上
逻辑操作符:
NOT　AND　OR　XOR

－－－－－－－－－－－－－－一般不用模糊查询，效率太低

12 rows in set (0.000 sec)

MariaDB [hellodb]> select * from students where name like '%yu%';
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
+-------+---------------+-----+--------+---------+-----------+
7 rows in set (0.000 sec)

MariaDB [hellodb]> select * from students where name like 's%';
+-------+-------------+-----+--------+---------+-----------+
| StuID | Name        | Age | Gender | ClassID | TeacherID |
+-------+-------------+-----+--------+---------+-----------+
|     1 | Shi Zhongyu |  22 | M      |       2 |         3 |
|     2 | Shi Potian  |  22 | M      |       1 |         7 |
|     6 | Shi Qing    |  46 | M      |       5 |      NULL |
|    25 | Sun Dasheng | 100 | M      |    NULL |      NULL |
+-------+-------------+-----+--------+---------+-----------+
4 rows in set (0.000 sec)

MariaDB [hellodb]>


－－－－－－－－－－－－－－－－－－－函数

1 row in set (0.000 sec)

MariaDB [hellodb]> select count(age) as AVG from students ;
+-----+
| AVG |
+-----+
|  25 |
+-----+
1 row in set (0.000 sec)

MariaDB [hellodb]> select count(classid) as AVG from students ;
+-----+
| AVG |
+-----+
|  23 |
+-----+
1 row in set (0.000 sec)


－－－－－－－－－－－－－－－－－－－－－－－－分组


MariaDB [hellodb]> select gender ,avg(age) from students group by gender ;
+--------+----------+
| gender | avg(age) |
+--------+----------+
| F      |  19.0000 |
| M      |  33.0000 |
+--------+----------+
2 rows in set (0.000 sec)

MariaDB [hellodb]>

--------分组:在select后面出现　只有　以　分组名(goup by)）和聚合函数


2 rows in set (0.000 sec)

MariaDB [hellodb]> select classid ,avg(age) from students group by classid ;
+---------+----------+
| classid | avg(age) |
+---------+----------+
|    NULL |  63.5000 |
|       1 |  20.5000 |
|       2 |  36.0000 |
|       3 |  20.2500 |
|       4 |  24.7500 |
|       5 |  46.0000 |
|       6 |  20.7500 |
|       7 |  19.6667 |
+---------+----------+
8 rows in set (0.000 sec)

MariaDB [hellodb]>

-----hanving 实在分组后的过滤，where　是分组前的过滤

MariaDB [hellodb]> select classid ,avg(age) from students group by classid having classid > 3 ;
+---------+----------+
| classid | avg(age) |
+---------+----------+
|       4 |  24.7500 |
|       5 |  46.0000 |
|       6 |  20.7500 |
|       7 |  19.6667 |
+---------+----------+
4 rows in set (0.000 sec)

MariaDB [hellodb]>

MariaDB [hellodb]> select classid ,avg(age) from students where classid > 3 group by classid having age > 30  ;
ERROR 1054 (42S22): Unknown column 'age' in 'having clause'
MariaDB [hellodb]> select classid ,avg(age) age from students where classid > 3 group by classid having age > 30  ;
+---------+---------+
| classid | age     |
+---------+---------+
|       5 | 46.0000 |
+---------+---------+
1 row in set (0.000 sec)

MariaDB [hellodb]> select classid ,gender,avg(age) from students group by classid ,gender ;
+---------+--------+----------+
| classid | gender | avg(age) |
+---------+--------+----------+
|    NULL | M      |  63.5000 |
|       1 | F      |  19.5000 |
|       1 | M      |  21.5000 |
|       2 | M      |  36.0000 |
|       3 | F      |  18.3333 |
|       3 | M      |  26.0000 |
|       4 | M      |  24.7500 |
|       5 | M      |  46.0000 |
|       6 | F      |  20.0000 |
|       6 | M      |  23.0000 |
|       7 | F      |  18.0000 |
|       7 | M      |  23.0000 |
+---------+--------+----------+
12 rows in set (0.000 sec)

MariaDB [hellodb]>


MariaDB [hellodb]> select * from students order by classid desc ;
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |
+-------+---------------+-----+--------+---------+-----------+
25 rows in set (0.000 sec)

MariaDB [hellodb]> select * from students order by -classid desc ;
+-------+---------------+-----+--------+---------+-----------+
| StuID | Name          | Age | Gender | ClassID | TeacherID |
+-------+---------------+-----+--------+---------+-----------+
|     2 | Shi Potian    |  22 | M      |       1 |         7 |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |
+-------+---------------+-----+--------+---------+-----------+
25 rows in set (0.000 sec)

MariaDB [hellodb]>


MariaDB [hellodb]> select classid,sum(age) from students group by classid having classid is not null order by classid ;
+---------+----------+
| classid | sum(age) |
+---------+----------+
|       1 |       82 |
|       2 |      108 |
|       3 |       81 |
|       4 |       99 |
|       5 |       46 |
|       6 |       83 |
|       7 |       59 |
+---------+----------+
7 rows in set (0.000 sec)

MariaDB [hellodb]>

------order by

MariaDB [hellodb]> select classid,sum(age) from students where classid is not null group by classid order by classid ;
+---------+----------+
| classid | sum(age) |
+---------+----------+
|       1 |       82 |
|       2 |      108 |
|       3 |       81 |
|       4 |       99 |
|       5 |       46 |
|       6 |       83 |
|       7 |       59 |
+---------+----------+
7 rows in set (0.000 sec)

MariaDB [hellodb]>

------ limit


MariaDB [hellodb]> select classid,sum(age) from students where classid is not null group by classid order by classid limit 3;
+---------+----------+
| classid | sum(age) |
+---------+----------+
|       1 |       82 |
|       2 |      108 |
|       3 |       81 |
+---------+----------+
3 rows in set (0.000 sec)

MariaDB [hellodb]>




示例
DESC students;
INSERT INTO students VALUES(1,'tom','m'),(2,'alice','f');
INSERT INTO students(id,name) VALUES(3,'jack'),(4,'allen');
SELECT * FROM students WHERE id < 3;
SELECT * FROM students WHERE gender='m';
SELECT * FROM students WHERE gender IS NULL;
SELECT * FROM students WHERE gender IS NOT NULL;
SELECT * FROM students ORDER BY name DESC LIMIT 2;
SELECT * FROM students ORDER BY name DESC LIMIT 1,2;
SELECT * FROM students WHERE id >=2 and id <=4
SELECT * FROM students WHERE BETWEEN 2 AND 4
SELECT * FROM students WHERE name LIKE ‘t%’
SELECT * FROM students WHERE name RLIKE '.*[lo].*';
SELECT id stuid,name as stuname FROM students

--id

MariaDB [hellodb]> select * from students where classid in (1,3,5);
+-------+--------------+-----+--------+---------+-----------+
| StuID | Name         | Age | Gender | ClassID | TeacherID |
+-------+--------------+-----+--------+---------+-----------+
|     2 | Shi Potian   |  22 | M      |       1 |         7 |
|     5 | Yu Yutong    |  26 | M      |       3 |         1 |
|     6 | Shi Qing     |  46 | M      |       5 |      NULL |
|     7 | Xi Ren       |  19 | F      |       3 |      NULL |
|    10 | Yue Lingshan |  19 | F      |       3 |      NULL |
|    12 | Wen Qingqing |  19 | F      |       1 |      NULL |
|    14 | Lu Wushuang  |  17 | F      |       3 |      NULL |
|    16 | Xu Zhu       |  21 | M      |       1 |      NULL |
|    22 | Xiao Qiao    |  20 | F      |       1 |      NULL |
+-------+--------------+-----+--------+---------+-----------+
9 rows in set (0.000 sec)

MariaDB [hellodb]>


```


## **<font color=Red> SQL语句构成－select 多表查询**

```

多表查询
 交叉连接:笛卡尔乘积
 内连接:
等值连接:让表之间的字段以“等值”建立连接关系;
不等值连接
自然连接:去掉重复列的等值连接
自连接
  外连接:
左外连接:
FROM tb1 LEFT JOIN tb2 ON tb1.col=tb2.col
右外连接
FROM tb1 RIGHT JOIN tb2 ON tb1.col=tb2.col


----------union　　多表纵向合合并　　　

MariaDB [hellodb]> select stuid,name,age,gender from students union select * from teachers;
+-------+---------------+-----+--------+
| stuid | name          | age | gender |
+-------+---------------+-----+--------+
|     1 | Shi Zhongyu   |  22 | M      |
|     2 | Shi Potian    |  22 | M      |
|     3 | Xie Yanke     |  53 | M      |
|     4 | Ding Dian     |  32 | M      |
|     5 | Yu Yutong     |  26 | M      |
|     6 | Shi Qing      |  46 | M      |
|     7 | Xi Ren        |  19 | F      |
|     8 | Lin Daiyu     |  17 | F      |
|     9 | Ren Yingying  |  20 | F      |
|    10 | Yue Lingshan  |  19 | F      |
|    11 | Yuan Chengzhi |  23 | M      |
|    12 | Wen Qingqing  |  19 | F      |
|    13 | Tian Boguang  |  33 | M      |
|    14 | Lu Wushuang   |  17 | F      |
|    15 | Duan Yu       |  19 | M      |
|    16 | Xu Zhu        |  21 | M      |
|    17 | Lin Chong     |  25 | M      |
|    18 | Hua Rong      |  23 | M      |
|    19 | Xue Baochai   |  18 | F      |
|    20 | Diao Chan     |  19 | F      |
|    21 | Huang Yueying |  22 | F      |
|    22 | Xiao Qiao     |  20 | F      |
|    23 | Ma Chao       |  23 | M      |
|    24 | Xu Xian       |  27 | M      |
|    25 | Sun Dasheng   | 100 | M      |
|     1 | Song Jiang    |  45 | M      |
|     2 | Zhang Sanfeng |  94 | M      |
|     3 | Miejue Shitai |  77 | F      |
|     4 | Lin Chaoying  |  93 | F      |
+-------+---------------+-----+--------+
29 rows in set (0.000 sec)

MariaDB [hellodb]>



－－－－－－－自己合并自己，去重　和　不去重　distinct

MariaDB [hellodb]> select * form teachers union select * from teachers;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'form teachers union select * from teachers' at line 1
MariaDB [hellodb]> select * from teachers union select * from teachers;
+-----+---------------+-----+--------+
| TID | Name          | Age | Gender |
+-----+---------------+-----+--------+
|   1 | Song Jiang    |  45 | M      |
|   2 | Zhang Sanfeng |  94 | M      |
|   3 | Miejue Shitai |  77 | F      |
|   4 | Lin Chaoying  |  93 | F      |
+-----+---------------+-----+--------+
4 rows in set (0.000 sec)

MariaDB [hellodb]> select * from teachers union all  select * from teachers;
+-----+---------------+-----+--------+
| TID | Name          | Age | Gender |
+-----+---------------+-----+--------+
|   1 | Song Jiang    |  45 | M      |
|   2 | Zhang Sanfeng |  94 | M      |
|   3 | Miejue Shitai |  77 | F      |
|   4 | Lin Chaoying  |  93 | F      |
|   1 | Song Jiang    |  45 | M      |
|   2 | Zhang Sanfeng |  94 | M      |
|   3 | Miejue Shitai |  77 | F      |
|   4 | Lin Chaoying  |  93 | F      |
+-----+---------------+-----+--------+
8 rows in set (0.000 sec)

MariaDB [hellodb]>


----------union　　多表横向合合并　　


第一张表每条记录和第二章表每一项做链接，　　交叉链连接笛卡尔乘积c cross join

ariaDB [hellodb]> select * from students cross join teachers;
+-------+---------------+-----+--------+---------+-----------+-----+---------------+-----+--------+
| StuID | Name          | Age | Gender | ClassID | TeacherID | TID | Name          | Age | Gender |
+-------+---------------+-----+--------+---------+-----------+-----+---------------+-----+--------+
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |   1 | Song Jiang    |  45 | M      |
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |   2 | Zhang Sanfeng |  94 | M      |
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |   3 | Miejue Shitai |  77 | F      |
|     1 | Shi Zhongyu   |  22 | M      |       2 |         3 |   4 | Lin Chaoying  |  93 | F      |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |   1 | Song Jiang    |  45 | M      |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |   2 | Zhang Sanfeng |  94 | M      |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |   3 | Miejue Shitai |  77 | F      |
|     2 | Shi Potian    |  22 | M      |       1 |         7 |   4 | Lin Chaoying  |  93 | F      |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |   1 | Song Jiang    |  45 | M      |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |   2 | Zhang Sanfeng |  94 | M      |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |   3 | Miejue Shitai |  77 | F      |
|     3 | Xie Yanke     |  53 | M      |       2 |        16 |   4 | Lin Chaoying  |  93 | F      |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |   1 | Song Jiang    |  45 | M      |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |   2 | Zhang Sanfeng |  94 | M      |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |   3 | Miejue Shitai |  77 | F      |
|     4 | Ding Dian     |  32 | M      |       4 |         4 |   4 | Lin Chaoying  |  93 | F      |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |   1 | Song Jiang    |  45 | M      |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |   2 | Zhang Sanfeng |  94 | M      |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |   3 | Miejue Shitai |  77 | F      |
|     5 | Yu Yutong     |  26 | M      |       3 |         1 |   4 | Lin Chaoying  |  93 | F      |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |   1 | Song Jiang    |  45 | M      |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |   3 | Miejue Shitai |  77 | F      |
|     6 | Shi Qing      |  46 | M      |       5 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |   1 | Song Jiang    |  45 | M      |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |   3 | Miejue Shitai |  77 | F      |
|     7 | Xi Ren        |  19 | F      |       3 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |   1 | Song Jiang    |  45 | M      |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |   3 | Miejue Shitai |  77 | F      |
|     8 | Lin Daiyu     |  17 | F      |       7 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |   1 | Song Jiang    |  45 | M      |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |   3 | Miejue Shitai |  77 | F      |
|     9 | Ren Yingying  |  20 | F      |       6 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |   1 | Song Jiang    |  45 | M      |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    10 | Yue Lingshan  |  19 | F      |       3 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |   1 | Song Jiang    |  45 | M      |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    11 | Yuan Chengzhi |  23 | M      |       6 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |   1 | Song Jiang    |  45 | M      |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    12 | Wen Qingqing  |  19 | F      |       1 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |   1 | Song Jiang    |  45 | M      |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    13 | Tian Boguang  |  33 | M      |       2 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |   1 | Song Jiang    |  45 | M      |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    14 | Lu Wushuang   |  17 | F      |       3 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |   1 | Song Jiang    |  45 | M      |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    15 | Duan Yu       |  19 | M      |       4 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |   1 | Song Jiang    |  45 | M      |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    16 | Xu Zhu        |  21 | M      |       1 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |   1 | Song Jiang    |  45 | M      |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    17 | Lin Chong     |  25 | M      |       4 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |   1 | Song Jiang    |  45 | M      |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    18 | Hua Rong      |  23 | M      |       7 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |   1 | Song Jiang    |  45 | M      |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    19 | Xue Baochai   |  18 | F      |       6 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |   1 | Song Jiang    |  45 | M      |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    20 | Diao Chan     |  19 | F      |       7 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |   1 | Song Jiang    |  45 | M      |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    21 | Huang Yueying |  22 | F      |       6 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |   1 | Song Jiang    |  45 | M      |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    22 | Xiao Qiao     |  20 | F      |       1 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |   1 | Song Jiang    |  45 | M      |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |   3 | Miejue Shitai |  77 | F      |
|    23 | Ma Chao       |  23 | M      |       4 |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |   1 | Song Jiang    |  45 | M      |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |   3 | Miejue Shitai |  77 | F      |
|    24 | Xu Xian       |  27 | M      |    NULL |      NULL |   4 | Lin Chaoying  |  93 | F      |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |   1 | Song Jiang    |  45 | M      |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |   2 | Zhang Sanfeng |  94 | M      |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |   3 | Miejue Shitai |  77 | F      |
|    25 | Sun Dasheng   | 100 | M      |    NULL |      NULL |   4 | Lin Chaoying  |  93 | F      |
+-------+---------------+-----+--------+---------+-----------+-----+---------------+-----+--------+
100 rows in set (0.000 sec)

MariaDB [hellodb]>

------------内连接　set交接


MariaDB [hellodb]> select * from students inner join teachers on students.teacherid = teachers.tid;
+-------+-------------+-----+--------+---------+-----------+-----+---------------+-----+--------+
| StuID | Name        | Age | Gender | ClassID | TeacherID | TID | Name          | Age | Gender |
+-------+-------------+-----+--------+---------+-----------+-----+---------------+-----+--------+
|     1 | Shi Zhongyu |  22 | M      |       2 |         3 |   3 | Miejue Shitai |  77 | F      |
|     4 | Ding Dian   |  32 | M      |       4 |         4 |   4 | Lin Chaoying  |  93 | F      |
|     5 | Yu Yutong   |  26 | M      |       3 |         1 |   1 | Song Jiang    |  45 | M      |
+-------+-------------+-----+--------+---------+-----------+-----+---------------+-----+--------+
3 rows in set (0.000 sec)

 -- 别名定义后，就必须要使用

MariaDB [hellodb]> select s.stuid,s.name,t.tid,t.name,t.age from students as s inner join teachers as t on students.teacherid = teachers.tid;　
ERROR 1054 (42S22): Unknown column 'students.teacherid' in 'on clause'
MariaDB [hellodb]> select s.stuid,s.name,t.tid,t.name,t.age from students as s inner join teachers as t on s.teacherid = t.tid;
+-------+-------------+-----+---------------+-----+
| stuid | name        | tid | name          | age |
+-------+-------------+-----+---------------+-----+
|     1 | Shi Zhongyu |   3 | Miejue Shitai |  77 |
|     4 | Ding Dian   |   4 | Lin Chaoying  |  93 |
|     5 | Yu Yutong   |   1 | Song Jiang    |  45 |
+-------+-------------+-----+---------------+-----+
3 rows in set (0.000 sec)

MariaDB [hellodb]>


－－－－－－－－－－－－－－－－－左外连接

MariaDB [hellodb]> select s.stuid,s.name,s.teachid,t.tid,t.name,t.age from students as s left outer join teachers as t on s.teacherid = t.tid;
ERROR 1054 (42S22): Unknown column 's.teachid' in 'field list'
MariaDB [hellodb]> select s.stuid,s.name,s.teacherid,t.tid,t.name,t.age from students as s left outer join teachers as t on s.teacherid = t.tid;
+-------+---------------+-----------+------+---------------+------+
| stuid | name          | teacherid | tid  | name          | age  |
+-------+---------------+-----------+------+---------------+------+
|     1 | Shi Zhongyu   |         3 |    3 | Miejue Shitai |   77 |
|     2 | Shi Potian    |         7 | NULL | NULL          | NULL |
|     3 | Xie Yanke     |        16 | NULL | NULL          | NULL |
|     4 | Ding Dian     |         4 |    4 | Lin Chaoying  |   93 |
|     5 | Yu Yutong     |         1 |    1 | Song Jiang    |   45 |
|     6 | Shi Qing      |      NULL | NULL | NULL          | NULL |
|     7 | Xi Ren        |      NULL | NULL | NULL          | NULL |
|     8 | Lin Daiyu     |      NULL | NULL | NULL          | NULL |
|     9 | Ren Yingying  |      NULL | NULL | NULL          | NULL |
|    10 | Yue Lingshan  |      NULL | NULL | NULL          | NULL |
|    11 | Yuan Chengzhi |      NULL | NULL | NULL          | NULL |
|    12 | Wen Qingqing  |      NULL | NULL | NULL          | NULL |
|    13 | Tian Boguang  |      NULL | NULL | NULL          | NULL |
|    14 | Lu Wushuang   |      NULL | NULL | NULL          | NULL |
|    15 | Duan Yu       |      NULL | NULL | NULL          | NULL |
|    16 | Xu Zhu        |      NULL | NULL | NULL          | NULL |
|    17 | Lin Chong     |      NULL | NULL | NULL          | NULL |
|    18 | Hua Rong      |      NULL | NULL | NULL          | NULL |
|    19 | Xue Baochai   |      NULL | NULL | NULL          | NULL |
|    20 | Diao Chan     |      NULL | NULL | NULL          | NULL |
|    21 | Huang Yueying |      NULL | NULL | NULL          | NULL |
|    22 | Xiao Qiao     |      NULL | NULL | NULL          | NULL |
|    23 | Ma Chao       |      NULL | NULL | NULL          | NULL |
|    24 | Xu Xian       |      NULL | NULL | NULL          | NULL |
|    25 | Sun Dasheng   |      NULL | NULL | NULL          | NULL |
+-------+---------------+-----------+------+---------------+------+
25 rows in set (0.000 sec)

MariaDB [hellodb]> select s.stuid,s.name as stuend_name,s.age as students_age,s.teacherid,t.tid,t.name as teacher_name,t.age as teacher_name from students as s left outer join teachers as t on s.teacherid = t.tid where t.tid is null;
+-------+---------------+--------------+-----------+------+--------------+--------------+
| stuid | stuend_name   | students_age | teacherid | tid  | teacher_name | teacher_name |
+-------+---------------+--------------+-----------+------+--------------+--------------+
|     2 | Shi Potian    |           22 |         7 | NULL | NULL         |         NULL |
|     3 | Xie Yanke     |           53 |        16 | NULL | NULL         |         NULL |
|     6 | Shi Qing      |           46 |      NULL | NULL | NULL         |         NULL |
|     7 | Xi Ren        |           19 |      NULL | NULL | NULL         |         NULL |
|     8 | Lin Daiyu     |           17 |      NULL | NULL | NULL         |         NULL |
|     9 | Ren Yingying  |           20 |      NULL | NULL | NULL         |         NULL |
|    10 | Yue Lingshan  |           19 |      NULL | NULL | NULL         |         NULL |
|    11 | Yuan Chengzhi |           23 |      NULL | NULL | NULL         |         NULL |
|    12 | Wen Qingqing  |           19 |      NULL | NULL | NULL         |         NULL |
|    13 | Tian Boguang  |           33 |      NULL | NULL | NULL         |         NULL |
|    14 | Lu Wushuang   |           17 |      NULL | NULL | NULL         |         NULL |
|    15 | Duan Yu       |           19 |      NULL | NULL | NULL         |         NULL |
|    16 | Xu Zhu        |           21 |      NULL | NULL | NULL         |         NULL |
|    17 | Lin Chong     |           25 |      NULL | NULL | NULL         |         NULL |
|    18 | Hua Rong      |           23 |      NULL | NULL | NULL         |         NULL |
|    19 | Xue Baochai   |           18 |      NULL | NULL | NULL         |         NULL |
|    20 | Diao Chan     |           19 |      NULL | NULL | NULL         |         NULL |
|    21 | Huang Yueying |           22 |      NULL | NULL | NULL         |         NULL |
|    22 | Xiao Qiao     |           20 |      NULL | NULL | NULL         |         NULL |
|    23 | Ma Chao       |           23 |      NULL | NULL | NULL         |         NULL |
|    24 | Xu Xian       |           27 |      NULL | NULL | NULL         |         NULL |
|    25 | Sun Dasheng   |          100 |      NULL | NULL | NULL         |         NULL |
+-------+---------------+--------------+-----------+------+--------------+--------------+
22 rows in set (0.000 sec)

MariaDB [hellodb]>

MariaDB [hellodb]> select s.stuid,s.name as stuend_name,s.age as students_age,s.teacherid,t.tid,t.name as teacher_name,t.age as teacher_name from students as s left outer join teachers as t on s.teacherid = t.tid having s.age > 30;
+-------+--------------+--------------+-----------+------+--------------+--------------+
| stuid | stuend_name  | students_age | teacherid | tid  | teacher_name | teacher_name |
+-------+--------------+--------------+-----------+------+--------------+--------------+
|     3 | Xie Yanke    |           53 |        16 | NULL | NULL         |         NULL |
|     4 | Ding Dian    |           32 |         4 |    4 | Lin Chaoying |           93 |
|     6 | Shi Qing     |           46 |      NULL | NULL | NULL         |         NULL |
|    13 | Tian Boguang |           33 |      NULL | NULL | NULL         |         NULL |
|    25 | Sun Dasheng  |          100 |      NULL | NULL | NULL         |         NULL |
+-------+--------------+--------------+-----------+------+--------------+--------------+
5 rows in set (0.000 sec)

MariaDB [hellodb]>




－－－－－－－－－－－－－－－－－右外连接

MariaDB [hellodb]> select s.stuid,s.name,s.teacherid,t.tid,t.name,t.age from students as s right outer join teachers as t on s.teacherid = t.tid;
+-------+-------------+-----------+-----+---------------+-----+
| stuid | name        | teacherid | tid | name          | age |
+-------+-------------+-----------+-----+---------------+-----+
|     1 | Shi Zhongyu |         3 |   3 | Miejue Shitai |  77 |
|     4 | Ding Dian   |         4 |   4 | Lin Chaoying  |  93 |
|     5 | Yu Yutong   |         1 |   1 | Song Jiang    |  45 |
|  NULL | NULL        |      NULL |   2 | Zhang Sanfeng |  94 |
+-------+-------------+-----------+-----+---------------+-----+
4 rows in set (0.000 sec)


MariaDB [hellodb]> select s.stuid,s.name as stuend_name,s.teacherid,t.tid,t.name as teacher_name,t.age from students as s full join teachers as t on s.teacherid = t.tid;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'full join teachers as t on s.teacherid = t.tid' at line 1
MariaDB [hellodb]> select s.stuid,s.name as stuend_name,s.teacherid,t.tid,t.name as teacher_name,t.age from students as s left outer join teachers as t on s.teacherid = t.tid
    -> union
    -> select s.stuid,s.name as stuend_name,s.teacherid,t.tid,t.name as teacher_name,t.age from students as s right outer join teachers as t on s.teacherid = t.tid;
+-------+---------------+-----------+------+---------------+------+
| stuid | stuend_name   | teacherid | tid  | teacher_name  | age  |
+-------+---------------+-----------+------+---------------+------+
|     1 | Shi Zhongyu   |         3 |    3 | Miejue Shitai |   77 |
|     2 | Shi Potian    |         7 | NULL | NULL          | NULL |
|     3 | Xie Yanke     |        16 | NULL | NULL          | NULL |
|     4 | Ding Dian     |         4 |    4 | Lin Chaoying  |   93 |
|     5 | Yu Yutong     |         1 |    1 | Song Jiang    |   45 |
|     6 | Shi Qing      |      NULL | NULL | NULL          | NULL |
|     7 | Xi Ren        |      NULL | NULL | NULL          | NULL |
|     8 | Lin Daiyu     |      NULL | NULL | NULL          | NULL |
|     9 | Ren Yingying  |      NULL | NULL | NULL          | NULL |
|    10 | Yue Lingshan  |      NULL | NULL | NULL          | NULL |
|    11 | Yuan Chengzhi |      NULL | NULL | NULL          | NULL |
|    12 | Wen Qingqing  |      NULL | NULL | NULL          | NULL |
|    13 | Tian Boguang  |      NU




－－－－－－－－－－－－－子查询



MariaDB [hellodb]>
MariaDB [hellodb]> select * from students where age >(select avg(age)from students);
+-------+--------------+-----+--------+---------+-----------+
| StuID | Name         | Age | Gender | ClassID | TeacherID |
+-------+--------------+-----+--------+---------+-----------+
|     3 | Xie Yanke    |  53 | M      |       2 |        16 |
|     4 | Ding Dian    |  32 | M      |       4 |         4 |
|     6 | Shi Qing     |  46 | M      |       5 |      NULL |
|    13 | Tian Boguang |  33 | M      |       2 |      NULL |
|    25 | Sun Dasheng  | 100 | M      |    NULL |      NULL |
+-------+--------------+-----+--------+---------+-----------+
5 rows in set (0.000 sec)

MariaDB [hellodb]>

－－－－－－－－－－－－自连接


MariaDB [hellodb]> select e.name,l.name from tmp as e left join tmp as l on e.leaderid =l.id;
+----------+----------+
| name     | name     |
+----------+----------+
| zhangsir | mage     |
| wang     | zhangsir |
| zhang    | wang     |
| mage     | NULL     |
+----------+----------+
4 rows in set (0.001 sec)

MariaDB [hellodb]> select * from tmp;
+------+----------+----------+
| id   | name     | leaderid |
+------+----------+----------+
|    1 | mage     |     NULL |
|    2 | zhangsir |        1 |
|    3 | wang     |        2 |
|    4 | zhang    |        3 |
+------+----------+----------+
4 rows in set (0.000 sec)

－－－－－－－－－－－－－－－－－－－－－－－－三张表操作

MariaDB [hellodb]>

MariaDB [hellodb]> select st.name,sc.courseid,sc.score,co.course from students as st inner join scores as sc on st.stuid=sc.stuid inner join courses co on sc.courseid = co.courseid;
+-------------+----------+-------+----------------+
| name        | courseid | score | course         |
+-------------+----------+-------+----------------+
| Shi Zhongyu |        2 |    77 | Kuihua Baodian |
| Shi Zhongyu |        6 |    93 | Weituo Zhang   |
| Shi Potian  |        2 |    47 | Kuihua Baodian |
| Shi Potian  |        5 |    97 | Daiyu Zanghua  |
| Xie Yanke   |        2 |    88 | Kuihua Baodian |
| Xie Yanke   |        6 |    75 | Weituo Zhang   |
| Ding Dian   |        5 |    71 | Daiyu Zanghua  |
| Ding Dian   |        2 |    89 | Kuihua Baodian |
| Yu Yutong   |        1 |    39 | Hamo Gong      |
| Yu Yutong   |        7 |    63 | Dagou Bangfa   |
| Shi Qing    |        1 |    96 | Hamo Gong      |
| Xi Ren      |        1 |    86 | Hamo Gong      |
| Xi Ren      |        7 |    83 | Dagou Bangfa   |
| Lin Daiyu   |        4 |    57 | Taiji Quan     |
| Lin Daiyu   |        3 |    93 | Jinshe Jianfa  |
+-------------+----------+-------+----------------+
15 rows in set (0.001 sec)

MariaDB [hellodb]>
```

## **<font color=Red>视图**


```


MariaDB [hellodb]> create view view_test as  select st.name,sc.courseid,sc.score,co.course from students as st inner join scores as sc on st.stuid=sc.stuid inner join courses co on sc.courseid = co.courseid;
Query OK, 0 rows affected (0.001 sec)

MariaDB [hellodb]>
MariaDB [hellodb]>
MariaDB [hellodb]>
MariaDB [hellodb]> select * from view_test;
+-------------+----------+-------+----------------+
| name        | courseid | score | course         |
+-------------+----------+-------+----------------+
| Shi Zhongyu |        2 |    77 | Kuihua Baodian |
| Shi Zhongyu |        6 |    93 | Weituo Zhang   |
| Shi Potian  |        2 |    47 | Kuihua Baodian |
| Shi Potian  |        5 |    97 | Daiyu Zanghua  |
| Xie Yanke   |        2 |    88 | Kuihua Baodian |
| Xie Yanke   |        6 |    75 | Weituo Zhang   |
| Ding Dian   |        5 |    71 | Daiyu Zanghua  |
| Ding Dian   |        2 |    89 | Kuihua Baodian |
| Yu Yutong   |        1 |    39 | Hamo Gong      |
| Yu Yutong   |        7 |    63 | Dagou Bangfa   |
| Shi Qing    |        1 |    96 | Hamo Gong      |
| Xi Ren      |        1 |    86 | Hamo Gong      |
| Xi Ren      |        7 |    83 | Dagou Bangfa   |
| Lin Daiyu   |        4 |    57 | Taiji Quan     |
| Lin Daiyu   |        3 |    93 | Jinshe Jianfa  |
+-------------+----------+-------+----------------+
15 rows in set (0.002 sec)

MariaDB [hellodb]>




1 row in set (0.001 sec)

MariaDB [hellodb]> show table status like 'view_test' \G;
*************************** 1. row ***************************
            Name: view_test
          Engine: NULL
         Version: NULL
      Row_format: NULL
            Rows: NULL
  Avg_row_length: NULL
     Data_length: NULL
 Max_data_length: NULL
    Index_length: NULL
       Data_free: NULL
  Auto_increment: NULL
     Create_time: NULL
     Update_time: NULL
      Check_time: NULL
       Collation: NULL
        Checksum: NULL
  Create_options: NULL
         Comment: VIEW
Max_index_length: NULL
       Temporary: NULL
1 row in set (0.000 sec)

ERROR: No query specified

MariaDB [hellodb]>




MariaDB [hellodb]> show table status like 'students' \G;
*************************** 1. row ***************************
            Name: students
          Engine: InnoDB
         Version: 10
      Row_format: Dynamic
            Rows: 25
  Avg_row_length: 655
     Data_length: 16384
 Max_data_length: 0
    Index_length: 0
       Data_free: 0
  Auto_increment: 26
     Create_time: 2020-02-20 00:33:04
     Update_time: NULL
      Check_time: NULL
       Collation: utf8_general_ci
        Checksum: NULL
  Create_options:
         Comment:
Max_index_length: 0
       Temporary: N
1 row in set (0.001 sec)

ERROR: No query specified

MariaDB [hellodb]>


MariaDB [hellodb]> create view old_v_stu  as  select * from students where age > 30;
Query OK, 0 rows affected (0.001 sec)

MariaDB [hellodb]> select * from old_v_stu;
+-------+--------------+-----+--------+---------+-----------+
| StuID | Name         | Age | Gender | ClassID | TeacherID |
+-------+--------------+-----+--------+---------+-----------+
|     3 | Xie Yanke    |  53 | M      |       2 |        16 |
|     4 | Ding Dian    |  32 | M      |       4 |         4 |
|     6 | Shi Qing     |  46 | M      |       5 |      NULL |
|    13 | Tian Boguang |  33 | M      |       2 |      NULL |
|    25 | Sun Dasheng  | 100 | M      |    NULL |      NULL |
+-------+--------------+-----+--------+---------+-----------+
5 rows in set (0.001 sec)

MariaDB [hellodb]> drop view vire_test;
ERROR 4092 (42S02): Unknown VIEW: 'hellodb.vire_test'
MariaDB [hellodb]> drop view view_test;
Query OK, 0 rows affected (0.000 sec)

MariaDB [hellodb]>
```


## **<font color=Red>函数**

```
https://dev.mysql.com/doc/refman/5.7/en/func-op-summary-ref.html

自定义函数 (user-defined function UDF)
　保存在mysql.proc表中
 创建UDF
CREATE [AGGREGATE] FUNCTION function_name(parameter_name
type,[parameter_name type,...])
RETURNS {STRING|INTEGER|REAL}
runtime_body
 说明:
参数可以有多个,也可以没有参数
必须有且只有一个返回值

自定义函数
创建函数
示例:无参UDF
CREATE FUNCTION simpleFun() RETURNS VARCHAR(20) RETURN "HelloWorld!”;
　查看函数列表:
SHOW FUNCTION STATUS;
　查看函数定义
SHOW CREATE FUNCTION function_name
　 删除UDF:
DROP FUNCTION function_name
　调用自定义函数语法:
SELECT function_name(parameter_value,...)

MariaDB [hellodb]> CREATE FUNCTION simpleFun() RETURNS VARCHAR(20) RETURN "HelloWorld!";
Query OK, 0 rows affected (0.106 sec)

MariaDB [hellodb]> show function status
    -> ;
+---------+-----------+----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
| Db      | Name      | Type     | Definer        | Modified            | Created             | Security_type | Comment | character_set_client | collation_connection | Database Collation |
+---------+-----------+----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
| hellodb | simpleFun | FUNCTION | root@localhost | 2020-02-20 17:24:09 | 2020-02-20 17:24:09 | DEFINER       |         | utf8                 | utf8_general_ci      | utf8_general_ci    |
+---------+-----------+----------+----------------+---------------------+---------------------+---------------+---------+----------------------+----------------------+--------------------+
1 row in set (0.001 sec)

MariaDB [hellodb]> show function status \G;
*************************** 1. row ***************************
                  Db: hellodb
                Name: simpleFun
                Type: FUNCTION
             Definer: root@localhost
            Modified: 2020-02-20 17:24:09
             Created: 2020-02-20 17:24:09
       Security_type: DEFINER
             Comment:
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: utf8_general_ci
1 row in set (0.001 sec)

ERROR: No query specified

MariaDB [hellodb]> show create function status \G;
ERROR 1305 (42000): FUNCTION status does not exist
ERROR: No query specified

MariaDB [hellodb]> show create function simpleFun;
+-----------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------+--------------------+
| Function  | sql_mode                                                                                  | Create Function                                                                                                | character_set_client | collation_connection | Database Collation |
+-----------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------+--------------------+
| simpleFun | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION | CREATE DEFINER=`root`@`localhost` FUNCTION `simpleFun`() RETURNS varchar(20) CHARSET utf8
RETURN "HelloWorld!" | utf8                 | utf8_general_ci      | utf8_general_ci    |
+-----------+-------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+----------------------+----------------------+--------------------+
1 row in set (0.000 sec)

MariaDB [hellodb]> select * from mysql.proc;
+---------+--------------------+-----------+--------------------+----------+-----------------+------------------+---------------+-----------------------------------------------------------------------------------------------------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+---------------------+---------------------+-------------------------------------------------------------------------------------------+---------+----------------------+----------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| db      | name               | type      | specific_name      | language | sql_data_access | is_deterministic | security_type | param_list                                                                                                | returns                  | body                                                                                                                                                                                       | definer        | created             | modified            | sql_mode                                                                                  | comment | character_set_client | collation_connection | db_collation      | body_utf8                                                                                                                                                                                  | aggregate |
+---------+--------------------+-----------+--------------------+----------+-----------------+------------------+---------------+-----------------------------------------------------------------------------------------------------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+---------------------+---------------------+-------------------------------------------------------------------------------------------+---------+----------------------+----------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
| mysql   | AddGeometryColumn  | PROCEDURE | AddGeometryColumn  | SQL      | CONTAINS_SQL    | NO               | INVOKER       | catalog varchar(64), t_schema varchar(64),
   t_name varchar(64), geometry_column varchar(64), t_srid int |                          | begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' ADD ', geometry_column,' GEOMETRY REF_SYSTEM_ID=', t_srid); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end | root@localhost | 2020-02-19 23:02:00 | 2020-02-19 23:02:00 |                                                                                           |         | utf8                 | utf8_general_ci      | latin1_swedish_ci | begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' ADD ', geometry_column,' GEOMETRY REF_SYSTEM_ID=', t_srid); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end | NONE      |
| mysql   | DropGeometryColumn | PROCEDURE | DropGeometryColumn | SQL      | CONTAINS_SQL    | NO               | INVOKER       | catalog varchar(64), t_schema varchar(64),
   t_name varchar(64), geometry_column varchar(64)             |                          | begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' DROP ', geometry_column); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end                                   | root@localhost | 2020-02-19 23:02:00 | 2020-02-19 23:02:00 |                                                                                           |         | utf8                 | utf8_general_ci      | latin1_swedish_ci | begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' DROP ', geometry_column); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end                                   | NONE      |
| hellodb | simpleFun          | FUNCTION  | simpleFun          | SQL      | CONTAINS_SQL    | NO               | DEFINER       |                                                                                                           | varchar(20) CHARSET utf8 | RETURN "HelloWorld!"                                                                                                                                                                       | root@localhost | 2020-02-20 17:24:09 | 2020-02-20 17:24:09 | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |         | utf8                 | utf8_general_ci      | utf8_general_ci   | RETURN "HelloWorld!"                                                                                                                                                                       | NONE      |
+---------+--------------------+-----------+--------------------+----------+-----------------+------------------+---------------+-----------------------------------------------------------------------------------------------------------+--------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------+---------------------+---------------------+-------------------------------------------------------------------------------------------+---------+----------------------+----------------------+-------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------+
3 rows in set (0.000 sec)

－－－　函数存放的位置

MariaDB [hellodb]> select * from mysql.proc \G;
*************************** 1. row ***************************
                  db: mysql
                name: AddGeometryColumn
                type: PROCEDURE
       specific_name: AddGeometryColumn
            language: SQL
     sql_data_access: CONTAINS_SQL
    is_deterministic: NO
       security_type: INVOKER
          param_list: catalog varchar(64), t_schema varchar(64),
   t_name varchar(64), geometry_column varchar(64), t_srid int
             returns:
                body: begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' ADD ', geometry_column,' GEOMETRY REF_SYSTEM_ID=', t_srid); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end
             definer: root@localhost
             created: 2020-02-19 23:02:00
            modified: 2020-02-19 23:02:00
            sql_mode:
             comment:
character_set_client: utf8
collation_connection: utf8_general_ci
        db_collation: latin1_swedish_ci
           body_utf8: begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' ADD ', geometry_column,' GEOMETRY REF_SYSTEM_ID=', t_srid); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end
           aggregate: NONE
*************************** 2. row ***************************
                  db: mysql
                name: DropGeometryColumn
                type: PROCEDURE
       specific_name: DropGeometryColumn
            language: SQL
     sql_data_access: CONTAINS_SQL
    is_deterministic: NO
       security_type: INVOKER
          param_list: catalog varchar(64), t_schema varchar(64),
   t_name varchar(64), geometry_column varchar(64)
             returns:
                body: begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' DROP ', geometry_column); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end
             definer: root@localhost
             created: 2020-02-19 23:02:00
            modified: 2020-02-19 23:02:00
            sql_mode:
             comment:
character_set_client: utf8
collation_connection: utf8_general_ci
        db_collation: latin1_swedish_ci
           body_utf8: begin
  set @qwe= concat('ALTER TABLE ', t_schema, '.', t_name, ' DROP ', geometry_column); PREPARE ls from @qwe; execute ls; deallocate prepare ls; end
           aggregate: NONE
*************************** 3. row ***************************
                  db: hellodb
                name: simpleFun
                type: FUNCTION
       specific_name: simpleFun
            language: SQL
     sql_data_access: CONTAINS_SQL
    is_deterministic: NO
       security_type: DEFINER
          param_list:
             returns: varchar(20) CHARSET utf8
                body: RETURN "HelloWorld!"
             definer: root@localhost
             created: 2020-02-20 17:24:09
            modified: 2020-02-20 17:24:09
            sql_mode: STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
             comment:
character_set_client: utf8
collation_connection: utf8_general_ci
        db_collation: utf8_general_ci
           body_utf8: RETURN "HelloWorld!"
           aggregate: NONE
3 rows in set (0.000 sec)

ERROR: No query specified

MariaDB [hellodb]>


－－－－－－－－－－－－自定义函数

DELIMITER //
CREATE FUNCTION deleteById(uid SMALLINT UNSIGNED) RETURNS
VARCHAR(20)
BEGIN
DELETE FROM students WHERE stuid = uid;
RETURN (SELECT COUNT(stuid) FROM students);
END//
DELIMITER ;




DELIMITER //
CREATE FUNCTION addTwoNumber(x SMALLINT UNSIGNED, Y SMALLINT　UNSIGNED)
RETURNS SMALLINT
BEGIN
DECLARE a, b SMALLINT UNSIGNED;
SET a = x, b = y;
RETURN a+b;
END//
DELIMITER ;




```




## **<font color=Red>　存储过程**
```
 存储过程:存储过程保存在mysql.proc表中
 创建存储过程
CREATE PROCEDURE sp_name ([ proc_parameter [,proc_parameter ...]])
routime_body
proc_parameter : [IN|OUT|INOUT] parameter_name type
其中IN表示输入参数,OUT表示输出参数,INOUT表示既可以输入也可以输出;
param_name表示参数名称;type表示参数的类型
 查看存储过程列表
SHOW PROCEDURE STATUS;


 查看存储过程定义
SHOW CREATE PROCEDURE sp_name
 调用存储过程
CALL sp_name ([ proc_parameter [,proc_parameter ...]])
CALL sp_name
说明:当无参时,可以省略"()",当有参数时,不可省略"()”
 存储过程修改
ALTER语句修改存储过程只能修改存储过程的注释等无关紧要的东西,不能修改
存储过程体,所以要修改存储过程,方法就是删除重建
 删除存储过程
DROP PROCEDURE [IF EXISTS] sp_name

存储过程示例
 创建无参存储过程
delimiter //
CREATE PROCEDURE showTime()
BEGIN
SELECT now();
END//
delimiter ;
CALL showTime;





delimiter //
CREATE PROCEDURE dorepeat(n INT)
BEGIN
SET @i = 0; ---全局变量
SET @sum = 0;
REPEAT SET @sum = @sum+@i; SET @i = @i + 1;
UNTIL @i > n END REPEAT;
END//
delimiter ;
CALL dorepeat(100);
SELECT @sum;


```



## **<font color=Red>　触发器**


## **<font color=Red>MySQL用户和权限管理**

```
https://dev.mysql.com/doc/refman/5.7/en/grant.html


用户管理
 创建用户:CREATE USER
CREATE USER 'USERNAME'@'HOST' [IDENTIFIED BY 'password'];
默认权限:USAGE
  用户重命名:RENAME USER
RENAME USER old_user_name TO new_user_name;
 删除用户:
DROP USER 'USERNAME'@'HOST‘
示例:删除默认的空用户
DROP USER ''@'localhost';


------------设置密码：


修改密码:
 mysql>SET PASSWORD FOR 'user'@'host' = PASSWORD(‘password');
 mysql>UPDATE mysql.user SET password=PASSWORD('password')
WHERE clause;
此方法需要执行下面指令才能生效:
mysql> FLUSH PRIVILEGES;
 #m　ysqladmin -u root -poldpass password ‘newpass’


记管理员密码的解决办法:
　启动mysqld进程时,为其使用如下选项:
　--skip-grant-tables　
　--skip-networking
使用UPDATE命令修改管理员密码
关闭mysqld进程,移除上述两个选项,重启mysqld

－－－－－－－－－－－－－反向解析
MariaDB [mysql]> show variables like 'skip%'
    -> ;
+---------------------------+-------+
| Variable_name             | Value |
+---------------------------+-------+
| skip_external_locking     | ON    |
| skip_name_resolve         | OFF   |
| skip_networking           | OFF   |
| skip_parallel_replication | OFF   |
| skip_replication          | OFF   |
| skip_show_database        | OFF   |
+---------------------------+-------+
6 rows in set (0.001 sec)

MariaDB [mysql]>



授权
 参考:https://dev.mysql.com/doc/refman/5.7/en/grant.html
　GRANT priv_type [(column_list)],... ON [object_type] priv_level TO 'user'@'host'
[IDENTIFIED BY 'password'] [WITH GRANT OPTION];
　　priv_type: ALL [PRIVILEGES]
　　object_type:TABLE | FUNCTION | PROCEDURE
　　priv_level: *(所有库) | *.* | db_name.* | db_name.tbl_name | tbl_name(当前库
的表) | db_name.routine_name(指定库的函数,存储过程,触发器)
 with_option: GRANT OPTION
| MAX_QUERIES_PER_HOUR count
| MAX_UPDATES_PER_HOUR count
| MAX_CONNECTIONS_PER_HOUR count
| MAX_USER_CONNECTIONS count
示例:GRANT SELECT (col1), INSERT (col1,col2) ON mydb.mytbl TO
'someuser'@'somehost‘;


MariaDB [mysql]> grant all on hellodb.* to test@'192.168.6.2' identified by 'centos';
Query OK, 0 rows affected (0.001 sec)

MariaDB [mysql]> show grants for test@'192.168.6.2'
    -> ;
+---------------------------------------------------------------------------------------------------------------+
| Grants for test@192.168.6.2                                                                                   |
+---------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'test'@'192.168.6.2' IDENTIFIED BY PASSWORD '*128977E278358FF80A246B5046F51043A2B1FCED' |
| GRANT ALL PRIVILEGES ON `hellodb`.* TO 'test'@'192.168.6.2'                                                   |
+---------------------------------------------------------------------------------------------------------------+
2 rows in set (0.000 sec)

MariaDB [hellodb]> show grants for test@'192.168.6.2'
    -> ;
+---------------------------------------------------------------------------------------------------------------+
| Grants for test@192.168.6.2                                                                                   |
+---------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'test'@'192.168.6.2' IDENTIFIED BY PASSWORD '*128977E278358FF80A246B5046F51043A2B1FCED' |
| GRANT ALL PRIVILEGES ON `hellodb`.* TO 'test'@'192.168.6.2'                                                   |
+---------------------------------------------------------------------------------------------------------------+
2 rows in set (0.000 sec)

MariaDB [hellodb]> show grants for test@'192.168.6.2';
+---------------------------------------------------------------------------------------------------------------+
| Grants for test@192.168.6.2                                                                                   |
+---------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'test'@'192.168.6.2' IDENTIFIED BY PASSWORD '*128977E278358FF80A246B5046F51043A2B1FCED' |
| GRANT ALL PRIVILEGES ON `hellodb`.* TO 'test'@'192.168.6.2'                                                   |
+---------------------------------------------------------------------------------------------------------------+
2 rows in set (0.000 sec)

MariaDB [hellodb]>
MariaDB [hellodb]>
MariaDB [hellodb]>
MariaDB [hellodb]>
MariaDB [hellodb]> revoke drop table on hellodb.* from test@'192.168.6.2';
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'table on hellodb.* from test@'192.168.6.2'' at line 1
MariaDB [hellodb]> revoke drop  on hellodb.* from test@'192.168.6.2';
Query OK, 0 rows affected (0.001 sec)

MariaDB [hellodb]> show grants for test@'192.168.6.2';
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Grants for test@192.168.6.2                                                                                                                                                                                                                         |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'test'@'192.168.6.2' IDENTIFIED BY PASSWORD '*128977E278358FF80A246B5046F51043A2B1FCED'                                                                                                                                       |
| GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, REFERENCES, INDEX, ALTER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, EVENT, TRIGGER, DELETE HISTORY ON `hellodb`.* TO 'test'@'192.168.6.2' |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
2 rows in set (0.000 sec)

MariaDB [hellodb]>
```


# **<font color=Red>高MySQL体系结构**
```
原子性：
　　　　　一个事务由多个小步骤组成，完全成　不全做
1、存储结构
每个MyISAM在磁盘上存储成三个文件。第一个文件的名字以表的名字开始，扩展名指出文件类型。
.frm文件存储表定义。
数据文件的扩展名为.MYD (MYData)。
索引文件的扩展名是.MYI (MYIndex)。

2、存储空间
MyISAM：可被压缩，存储空间较小。
InnoDB：需要更多的内存和存储，它会在主内存中建立其专用的缓冲池用于高速缓冲数据和索引。
MyISAM的索引和数据是分开的，并且索引是有压缩的，内存使用率就对应提高了不少。能加载更多索引，而Innodb是索引和数据是紧密捆绑的，没有使用压缩从而会造成Innodb比MyISAM体积庞大不小

3、事务处理
MyISAM类型的表强调的是性能，其执行数度比InnoDB类型更快，但是不支持外键、不提供事务支持。
InnoDB提供事务支持事务，外部键（foreign key）等高级数据库功能。

SELECT、UPDATE、INSERT、Delete操作
如果执行大量的SELECT，MyISAM是更好的选择。
如果你的数据执行大量的INSERT或UPDATE，出于性能方面的考虑，应该使用InnoDB表。
DELETE FROM table时，InnoDB不会重新建立表，而是一行一行的删除。而MyISAM则是重新建立表。在innodb上如果要清空保存有大量数据的表，最好使用truncate table这个命令。

AUTO_INCREMENT
MyISAM：可以和其他字段一起建立联合索引。引擎的自动增长列必须是索引，如果是组合索引，自动增长可以不是第一列，他可以根据前面几列进行排序后递增。
InnoDB：InnoDB中必须包含只有该字段的索引。引擎的自动增长列必须是索引，如果是组合索引也必须是组合索引的第一列。

4、表的具体行数
MyISAM：保存有表的总行数，如果select count(*) from table;会直接取出该值。
InnoDB：没有保存表的总行数，如果使用select count(*) from table；就会遍历整个表，消耗相当大，但是在加了where后，myisam和innodb处理的方式都一样。

5、全文索引
MyISAM：支持 FULLTEXT类型的全文索引。不支持中文。
InnoDB：不支持FULLTEXT类型的全文索引，但是innodb可以使用sphinx插件支持全文索引，并且效果更好。

6、表锁差异
MyISAM：只支持表级锁，只支持表级锁，用户在操作myisam表时，select，update，delete，insert语句都会给表自动加锁。
InnoDB：支持事务和行级锁，是innodb的最大特色。行锁大幅度提高了多用户并发操作的新能。但是InnoDB的行锁也不是绝对的，如果在执行一个SQL语句时MySQL不能确定要扫描的范围，InnoDB表同样会锁全表， 例如update table set num=1 where name like “%aaa%”

一般来说：
MyISAM适合：
(1)做很多count 的计算；
(2)插入不频繁，查询非常频繁；
(3)没有事务。
InnoDB适合：
(1)可靠性要求比较高，或者要求事务；
(2)表更新和查询都相当的频繁，并且表锁定的机会比较大的情况。




存储文件格式：

MyISAM引擎文件　
表格式定义　　tbl_name.frm
数据文件　tbl_name.MYD
索引文件　tbl_name.MYI

两类文件放在数据库独立目录中　
数据文件(存储数据和索引):tb_name.ibd
表格式定义:tb_name.frm


所有InnoDB表的数据和索引放置于同一个表空间中
表空间文件:datadir定义的目录下
数据文件:ibddata1, ibddata2, ...
 每个表单独使用一个表空间存储表的数据和索引
启用:innodb_file_per_table=ON
参看:https://mariadb.com/kb/en/library/xtradbinnodb-server-
system-variables/#innodb_file_per_table
ON (>= MariaDB 5.5)
两类文件放在数据库独立目录中
数据文件(存储数据和索引):tb_name.ibd
表格式定义:tb_name.frm

MariaDB [hellodb]> show variables like 'innodb_file_per_table';
+-----------------------+-------+
| Variable_name         | Value |
+-----------------------+-------+
| innodb_file_per_table | ON    |
+-----------------------+-------+
1 row in set (0.001 sec)

MariaDB [hellodb]>



```

#### **<font color=Red>管理存储引擎**

```
查看mysql支持的存储引擎 show engines;
查看当前默认的存储引擎 show variables like '%storage_engine%';

设置默认的存储引擎
vim /etc/my.conf
[mysqld]
default_storage_engine= InnoDB


查看库中所有表使用的存储引擎 show table status from db_name;
  查看库中指定表的存储引擎
show table status like ' tb_name ';
show create table tb_name;
  设置表的存储引擎:
CREATE TABLE tb_name(... ) ENGINE=InnoDB;
ALTER TABLE tb_name ENGINE=InnoDB;
```


#### **<font color=Red>服务器配置**

```
 1 mysqld选项,
 2 服务器系统变量
 3 服务器状态变量
https://dev.mysql.com/doc/refman/5.7/en/mysqld-option-tables.html
https://mariadb.com/kb/en/library/full-list-of-mariadb-options-system-and-status-variables/


服务器系统变量:分全局和会话两种
 获取系统变量
mysql> SHOW GLOBAL VARIABLES;
mysql> SHOW [SESSION] VARIABLES;
mysql> SELECT @@VARIABLES;
  修改服务器变量的值:
mysql> help SET
 修改全局变量:仅对修改后新创建的会话有效;对已经建立的会话无效
mysql> SET GLOBAL system_var_name=value;
mysql> SET @@global.system_var_name=value;
  修改会话变量:
mysql> SET [SESSION] system_var_name=value;
mysql> SET @@[session.]system_var_name=value;

*************************** 653. row ***************************
Variable_name: wsrep_sync_wait
        Value: 0
*************************** 654. row ***************************
Variable_name: wsrep_trx_fragment_size
        Value: 0
*************************** 655. row ***************************
Variable_name: wsrep_trx_fragment_unit
        Value: bytes
655 rows in set (0.152 sec)

ERROR: No query specified

MariaDB [hellodb]> show variables \G;


SQL_MODE:对其设置可以完成一些约束检查的工作,可分别进行全局的设置或当前会
话的设置,参看:https://mariadb.com/kb/en/library/sql-mode/
 常见MODE:
 NO_AUTO_CREATE_USER
禁止GRANT创建密码为空的用户
 NO_ZERO_DATE
在严格模式,不允许使用‘0000-00-00’的时间
 ONLY_FULL_GROUP_BY
对于GROUP BY聚合操作,如果在SELECT中的列,没有在GROUP BY中出现,那么
将认为这个SQL是不合法的
 NO_BACKSLASH_ESCAPES
反斜杠“\”作为普通字符而非转义字符
 PIPES_AS_CONCAT
将"||"视为连接操作符而非“或运算符



MariaDB [(none)]> show variables like 'sql_mode';
+---------------+-------------------------------------------------------------------------------------------+
| Variable_name | Value                                                                                     |
+---------------+-------------------------------------------------------------------------------------------+
| sql_mode      | STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION |
+---------------+-------------------------------------------------------------------------------------------+
1 row in set (0.001 sec)

MariaDB [(none)]>



```



## **<font color=Red>查询缓存**

```
 查询缓存( Query Cache )原理
 查询缓存( Query Cache )原理
 查询缓存( Query Cache )原理
缓存SELECT操作或预处理查询的结果集和SQL语句,当有新的SELECT语句或预
处理查询语句请求,先去查询缓存,判断是否存在可用的记录集,判断标准:与缓
存的SQL语句,是否完全一样,区分大小写
  优缺点
不需要对SQL语句做任何解析和执行,当然语法解析必须通过在先,直接从
Query Cache中获得查询结果,提高查询性能
查询缓存的判断规则,不够智能,也即提高了查询缓存的使用门槛,降低其效率;
查询缓存的使用,会增加检查和清理Query Cache中记录集的开销


MariaDB [(none)]> show variables like 'query%';
+------------------------------+---------+
| Variable_name                | Value   |
+------------------------------+---------+
| query_alloc_block_size       | 16384   |
| query_cache_limit            | 1048576 |
| query_cache_min_res_unit     | 4096    |
| query_cache_size             | 1048576 |
| query_cache_strip_comments   | OFF     |
| query_cache_type             | OFF     |
| query_cache_wlock_invalidate | OFF     |
| query_prealloc_size          | 24576   |
+------------------------------+---------+
8 rows in set (0.001 sec)



MariaDB [(none)]> SHOW GLOBAL STATUS LIKE 'Qcache%';
+-------------------------+---------+
| Variable_name           | Value   |
+-------------------------+---------+
| Qcache_free_blocks      | 1       |
| Qcache_free_memory      | 1031320 |
| Qcache_hits             | 0       |
| Qcache_inserts          | 0       |
| Qcache_lowmem_prunes    | 0       |
| Qcache_not_cached       | 0       |
| Qcache_queries_in_cache | 0       |
| Qcache_total_blocks     | 1       |
+-------------------------+---------+
8 rows in set (0.099 sec)

查询缓存相关的服务器变量
 query_cache_min_res_unit:查询缓存中内存块的最小分配单位,默认4k,较
小值会减少浪费,但会导致更频繁的内存分配操作,较大值会带来浪费,会导
致碎片过多,内存不足
 query_cache_limit:单个查询结果能缓存的最大值,默认为1M,对于查询结
果过大而无法缓存的语句,建议使用SQL_NO_CACHE
 query_cache_size:查询缓存总共可用的内存空间;单位字节,必须是1024
的整数倍,最小值40KB,低于此值有警报
 query_cache_wlock_invalidate:如果某表被其它的会话锁定,是否仍然可以
从查询缓存中返回结果,默认值为OFF,表示可以在表被其它会话锁定的场景
中继续从缓存返回数据;ON则表示不允许
 query_cache_type:是否开启缓存功能,取值为ON, OFF, DEMAND




查询缓存相关的状态变量:
MariaDB [(none)]>
Qcache_free_blocks:处于空闲状态 Query Cache中内存 Block 数
 Qcache_total_blocks:Query Cache 中总Block ,当Qcache_free_blocks
相对此值较大时,可能用内存碎片,执行FLUSH QUERY CACHE清理碎片
 Qcache_free_memory:处于空闲状态的 Query Cache 内存总量
 Qcache_hits:Query Cache 命中次数
 Qcache_inserts:向 Query Cache 中插入新的 Query Cache 的次数,即没
有命中的次数
 Qcache_lowmem_prunes:记录因为内存不足而被移除出查询缓存的查询数
 Qcache_not_cached:没有被 Cache 的 SQL 数,包括无法被 Cache 的 SQL
以及由于 query_cache_type 设置的不会被 Cache 的 SQL语句
 Qcache_queries_in_cache:在 Query Cache 中的 SQL 数量

```


## **<font color=Red> InnoDB存储引擎**

```
show global status like 'innodb%read%'\G
```
