# **<font color=Red> 索引**


```

索引:是特殊数据结构,定义在查找时作为查找条件的字段,在MySQL又称为键key,索引通过存储引擎实现
优点:
 索引可以降低服务需要扫描的数据量,减少了IO次数
 索引可以帮助服务器避免排序和使用临时表
 索引可以帮助将随机I/O转为顺序I/O
缺点:
 占用额外空间,影响插入速度



 索引类型:
  B + TREE、HASH、R TREE
  聚簇(集)索引、非聚簇索引:数据和索引是否存储在一起
  主键索引、二级(辅助)索引
  稠密索引、稀疏索引:是否索引了每一个数据项
  简单索引、组合索引
     左前缀索引:取前面的字符做索引
     覆盖索引:从索引中即可取出要查询的数据,性能高



管理索引
 创建索引:
CREATE INDEX [UNIQUE] index_name ON tbl_name (index_col_name[(length)],...);
ALTER TABLE tbl_name ADD INDEX index_name(index_col_name);
help CREATE INDEX;
 删除索引:
DROP INDEX index_name ON tbl_name;
ALTER TABLE tbl_name DROP INDEX index_name(index_col_name);
 查看索引:
SHOW INDEXES FROM [db_name.]tbl_name;
优化表空间:
OPTIMIZE TABLE tb_name;
 查看索引的使用
SET GLOBAL userstat=1;
SHOW INDEX_STATISTICS;



MariaDB [hellodb]> show indexes from students\G;
*************************** 1. row ***************************
        Table: students
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: StuID
    Collation: A
  Cardinality: 25
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
1 row in set (0.123 sec)

ERROR: No query specified

MariaDB [hellodb]>

MariaDB [hellodb]>
MariaDB [hellodb]>
MariaDB [hellodb]> select * from students where age =20;
+-------+--------------+-----+--------+---------+-----------+
| StuID | Name         | Age | Gender | ClassID | TeacherID |
+-------+--------------+-----+--------+---------+-----------+
|     9 | Ren Yingying |  20 | F      |       6 |      NULL |
|    22 | Xiao Qiao    |  20 | F      |       1 |      NULL |
+-------+--------------+-----+--------+---------+-----------+
2 rows in set (0.001 sec)

---------------------------------------explain

MariaDB [hellodb]> explain select * from students where age =20;
+------+-------------+----------+------+---------------+------+---------+------+------+-------------+
| id   | select_type | table    | type | possible_keys | key  | key_len | ref  | rows | Extra       |
+------+-------------+----------+------+---------------+------+---------+------+------+-------------+
|    1 | SIMPLE      | students | ALL  | NULL          | NULL | NULL    | NULL | 25   | Using where |
+------+-------------+----------+------+---------------+------+---------+------+------+-------------+
1 row in set (0.000 sec)

MariaDB [hellodb]>

--------------

MariaDB [hellodb]> create index idx_age on students(age);
Query OK, 0 rows affected (0.017 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [hellodb]> show indexes from students\G;
*************************** 1. row ***************************
        Table: students
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: StuID
    Collation: A
  Cardinality: 25
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
*************************** 2. row ***************************
        Table: students
   Non_unique: 1
     Key_name: idx_age
 Seq_in_index: 1
  Column_name: Age
    Collation: A
  Cardinality: 25
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
2 rows in set (0.000 sec)

ERROR: No query specified

MariaDB [hellodb]>
MariaDB [hellodb]> explain select * from students where age =20;
+------+-------------+----------+------+---------------+---------+---------+-------+------+-------+
| id   | select_type | table    | type | possible_keys | key     | key_len | ref   | rows | Extra |
+------+-------------+----------+------+---------------+---------+---------+-------+------+-------+
|    1 | SIMPLE      | students | ref  | idx_age       | idx_age | 1       | const | 2    |       |
+------+-------------+----------+------+---------------+---------+---------+-------+------+-------+
1 row in set (0.098 sec)

MariaDB [hellodb]>


MariaDB [hellodb]> create index idx_name_age on students(name,age)


MariaDB [hellodb]> create index idx_name_age on students(name,age);
Query OK, 0 rows affected (0.006 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [hellodb]> show indexes from students\G;
*************************** 1. row ***************************
        Table: students
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: StuID
    Collation: A
  Cardinality: 25
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
*************************** 2. row ***************************
        Table: students
   Non_unique: 1
     Key_name: idx_name_age
 Seq_in_index: 1
  Column_name: Name
    Collation: A
  Cardinality: 25
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
*************************** 3. row ***************************
        Table: students
   Non_unique: 1
     Key_name: idx_name_age
 Seq_in_index: 2
  Column_name: Age
    Collation: A
  Cardinality: 25
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
3 rows in set (0.000 sec)

ERROR: No query specified

MariaDB [hellodb]>


MariaDB [hellodb]> explain select * from students where name='%s';
+------+-------------+----------+------+---------------+--------------+---------+-------+------+-----------------------+
| id   | select_type | table    | type | possible_keys | key          | key_len | ref   | rows | Extra                 |
+------+-------------+----------+------+---------------+--------------+---------+-------+------+-----------------------+
|    1 | SIMPLE      | students | ref  | idx_name_age  | idx_name_age | 152     | const | 1    | Using index condition |
+------+-------------+----------+------+---------------+--------------+---------+-------+------+-----------------------+
1 row in set (0.000 sec)

MariaDB [hellodb]> explain select * from students where age=20;
+------+-------------+----------+------+---------------+------+---------+------+------+-------------+
| id   | select_type | table    | type | possible_keys | key  | key_len | ref  | rows | Extra       |
+------+-------------+----------+------+---------------+------+---------+------+------+-------------+
|    1 | SIMPLE      | students | ALL  | NULL          | NULL | NULL    | NULL | 25   | Using where |
+------+-------------+----------+------+---------------+------+---------+------+------+-------------+
1 row in set (0.000 sec)

MariaDB [hellodb]> explain select * from students where name='%s' and age = 2;
+------+-------------+----------+------+---------------+--------------+---------+-------------+------+-----------------------+
| id   | select_type | table    | type | possible_keys | key          | key_len | ref         | rows | Extra                 |
+------+-------------+----------+------+---------------+--------------+---------+-------------+------+-----------------------+
|    1 | SIMPLE      | students | ref  | idx_name_age  | idx_name_age | 153     | const,const | 1    | Using index condition |
+------+-------------+----------+------+---------------+--------------+---------+-------------+------+-----------------------+
1 row in set (0.001 sec)

MariaDB [hellodb]>

MariaDB [hellodb]>
MariaDB [hellodb]> select * from students where stuid=20;
+-------+-----------+-----+--------+---------+-----------+
| StuID | Name      | Age | Gender | ClassID | TeacherID |
+-------+-----------+-----+--------+---------+-----------+
|    20 | Diao Chan |  19 | F      |       7 |      NULL |
+-------+-----------+-----+--------+---------+-----------+
1 row in set (0.000 sec)

MariaDB [hellodb]> SHOW INDEX_STATISTICS;
+--------------+------------+------------+-----------+
| Table_schema | Table_name | Index_name | Rows_read |
+--------------+------------+------------+-----------+
| hellodb      | students   | PRIMARY    |         1 |
+--------------+------------+------------+-----------+
1 row in set (0.000 sec)

MariaDB [hellodb]>



MariaDB [hellodb]> select * from testlog where name='wang99999';
+-------+-----------+-------+
| id    | name      | age   |
+-------+-----------+-------+
| 99999 | wang99999 | 99999 |
+-------+-----------+-------+
1 row in set (0.018 sec)

MariaDB [hellodb]> explain select * from testlog where name='wang99999';
+------+-------------+---------+------+---------------+------+---------+------+--------+-------------+
| id   | select_type | table   | type | possible_keys | key  | key_len | ref  | rows   | Extra       |
+------+-------------+---------+------+---------------+------+---------+------+--------+-------------+
|    1 | SIMPLE      | testlog | ALL  | NULL          | NULL | NULL    | NULL | 100076 | Using where |
+------+-------------+---------+------+---------------+------+---------+------+--------+-------------+
1 row in set (0.000 sec)

MariaDB [hellodb]> create index idx_name on testlog(name);
Query OK, 0 rows affected (0.502 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [hellodb]> select * from testlog where name='wang99999';
+-------+-----------+-------+
| id    | name      | age   |
+-------+-----------+-------+
| 99999 | wang99999 | 99999 |
+-------+-----------+-------+
1 row in set (0.000 sec)

MariaDB [hellodb]>



1 row in set (0.000 sec)

MariaDB [hellodb]> explain select * from testlog where name='wang99999';
+------+-------------+---------+------+---------------+----------+---------+-------+------+-----------------------+
| id   | select_type | table   | type | possible_keys | key      | key_len | ref   | rows | Extra                 |
+------+-------------+---------+------+---------------+----------+---------+-------+------+-----------------------+
|    1 | SIMPLE      | testlog | ref  | idx_name      | idx_name | 31      | const | 1    | Using index condition |
+------+-------------+---------+------+---------------+----------+---------+-------+------+-----------------------+
1 row in set (0.000 sec)

MariaDB [hellodb]>





```

## **<font color=Red>通并发控制**



```


锁粒度:
   表级锁 -MYSYSAL
   行级锁  - InnoDB
锁:
  读锁:共享锁,只读不可写(包括当前事务) ,多个读互不阻塞
  写锁:独占锁,排它锁,写锁会阻塞其它事务(不包括当前事务)的读和它锁
实现
  存储引擎:自行实现其锁策略和锁粒度
  服务器级:实现了锁,表级锁,用户可显式请求
分类:
   隐式锁:由存储引擎自动



   显式使用锁
 LOCK TABLES 加锁
  tbl_name [[AS] alias] lock_type
[, tbl_name [[AS] alias] lock_type] ...
lock_type: READ , WRITE
UNLOCK TABLES 解锁
 FLUSH TABLES [tb_name[,...]] [WITH READ LOCK]
关闭正在打开的表(清除查询缓存),通常在备份前加全局读锁
 SELECT clause [FOR UPDATE | LOCK IN SHARE MODE]
查询时加写或读锁
```


## **<font color=Red> 事务**

```

事务Transactions:一组原子性的SQL语句,或一个独立工作单元
  事务日志:记录事务信息,实现undo,redo等故障恢复功能
   ACID特性:
 A:atomicity原子性;整个事务中的所有操作要么全部成功执行,要么全部失败后回滚
 C:consistency一致性;数据库总是从一个一致性状态转换为另一个一致性状态
 I:Isolation隔离性;一个事务所做出的操作在提交之前,是不能为其它事务所见;隔离有多种隔离级别,实现并发
 D:durability持久性;一旦事务提交,其所做的修改会永久保存于数据库中


----事务隔离性
MariaDB [hellodb]> show variables like 'autocommit';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| autocommit    | ON    |
+---------------+-------+
1 row in set (0.001 sec)

MariaDB [hellodb]>


事务隔离级别:从上至下更加严格（例如多窗口操作同一表或数据）
 READ UNCOMMITTED 可读取到未提交数据,产生脏读
 READ COMMITTED 可读取到提交数据,但未提交数据不可读,产生不可重复读,即可读取到多个提交数据,导致每次读取数据不一致
 REPEATABLE READ 可重复读,多次读取数据都一致,产生幻读,即读取过程中,即使有其它提交的事务修改数据,仍只能读取到未修改
前的旧数据。此为MySQL默认设置
 SERIALIZABILE 可串行化,未提交的读事务阻塞修改事务,或者未提交的修改事务阻塞读事务。导致并发性能差
 MVCC: 多版本并发控制,和事务级别相关



```



## **<font color=Red>日志**



```
日志
  事务日志 transaction log
  错误日志 error log
  通用日志 general log
  慢查询日志 slow query log

慢查询日志:记录执行查询时长超出指定时长的操作
slow_query_log=ON|OFF 开启或关闭慢查询
long_query_time=N 慢查询的阀值,单位秒
slow_query_log_file=HOSTNAME-slow.log 慢查询日志文件
log_slow_filter = admin,filesort,filesort_on_disk,full_join,full_scan,
query_cache,query_cache_miss,tmp_table,tmp_table_on_disk
上述查询类型且查询时长超过long_query_time,则记录日志
log_queries_not_using_indexes=ON 不使用索引或使用全索引扫描,不论
是否达到慢查询阀值的语句是否记录日志,默认OFF,即不记录
log_slow_rate_limit = 1 多少次查询才记录,mariadb特有
log_slow_verbosity= Query_plan,explain 记录内容
log_slow_queries = OFF 同slow_query_log 新版已废弃



 二进制日志 binary log
 中继日志 reley log





MariaDB [hellodb]> show variables like '%innodb_log%';
+-----------------------------+----------+
| Variable_name               | Value    |
+-----------------------------+----------+
| innodb_log_buffer_size      | 16777216 |
| innodb_log_checksums        | ON       |
| innodb_log_compressed_pages | ON       |
| innodb_log_file_size        | 50331648 |
| innodb_log_files_in_group   | 2        |
| innodb_log_group_home_dir   | ./       |
| innodb_log_optimize_ddl     | ON       |
| innodb_log_write_ahead_size | 8192     |
+-----------------------------+----------+
8 rows in set (0.001 sec)

MariaDB [hellodb]>



innodb_flush_log_at_trx_commit
 说明:设置为1,同时sync_binlog = 1表示最高级别的容错
innodb_use_global_flush_log_at_trx_commit的值确定是否可以使用SET语句
重置此变量
 1默认情况下,日志缓冲区将写入日志文件,并在每次事务后执行刷新到磁盘。
这是完全遵守ACID特性
 0提交时没有任何操作; 而是每秒执行一次日志缓冲区写入和刷新。 这样可以提
供更好的性能,但服务器崩溃可以清除最后一秒的事务
 2每次提交后都会写入日志缓冲区,但每秒都会进行一次刷新。 性能比0略好一
些,但操作系统或停电可能导致最后一秒的交易丢失
 3模拟MariaDB 5.5组提交(每组提交3个同步),此项MariaDB 10.0支持


--------------监控命令执行过程

 set profiling = on
MariaDB [hellodb]> show profiles;
+----------+-------------+-------------------------------+
| Query_ID | Duration    | Query                         |
+----------+-------------+-------------------------------+
|        1 | 25.09731933 | select sleep(1) from students |
+----------+-------------+-------------------------------+
1 row in set (0.000 sec)

MariaDB [hellodb]> show profile for query 1;
+------------------------+----------+
| Status                 | Duration |
+------------------------+----------+
| Starting               | 0.000046 |
| Checking permissions   | 0.000004 |
| Opening tables         | 0.000015 |
| After opening tables   | 0.000003 |
| System lock            | 0.000003 |
| Table lock             | 0.000004 |
| Init                   | 0.000010 |
| Optimizing             | 0.000006 |
| Statistics             | 0.000009 |
| Preparing              | 0.000017 |
| Executing              | 0.000004 |
| Sending data           | 0.000028 |
| User sleep             | 1.004334 |
| User sleep             | 1.004212 |
| User sleep             | 1.004386 |
| User sleep             | 1.004888 |
| User sleep             | 1.005286 |
| User sleep             | 1.002075 |
| User sleep             | 1.004982 |
| User sleep             | 1.002431 |
| User sleep             | 1.003356 |
| User sleep             | 1.003292 |
| User sleep             | 1.005042 |
| User sleep             | 1.004674 |
| User sleep             | 1.001518 |
| User sleep             | 1.006063 |
| User sleep             | 1.002675 |
| User sleep             | 1.005391 |
| User sleep             | 1.003839 |
| User sleep             | 1.000702 |
| User sleep             | 1.004551 |
| User sleep             | 1.001030 |
| User sleep             | 1.006329 |
| User sleep             | 1.002072 |
| User sleep             | 1.005643 |
| User sleep             | 1.002287 |
| User sleep             | 1.006025 |
| End of update loop     | 0.000016 |
| Query end              | 0.000002 |
| Commit                 | 0.000027 |
| Closing tables         | 0.000004 |
| Unlocking tables       | 0.000002 |
| Closing tables         | 0.000011 |
| Starting cleanup       | 0.000002 |
| Freeing items          | 0.000004 |
| Updating status        | 0.000017 |
| Reset for next command | 0.000002 |
+------------------------+----------+


```
