# 数据库操作
## 1.1 数据库创建
### 创建数据库 
create (if not exits) 数据库名
create Name character set <> collate <>
默认：utf8mb4    utf8mb4_0900_ai_ci
### 显示创建信息
show variables like 'character_set_database'
show variables like 'collation_database'
### practice
create database if not exists ddl_d1 caracter set utf8 collate utf8mb4_0900_as_cs

## 1.2 数据库查看
查看所有库
show databases;

查看当前使用库
select database();

查看库下所有表
show tables from 库名

查看创建库的信息和语句
show create database 库名
	
## 1.3 数据库修改
修改字符集
alter database 数据库 character set 字符集
alter database 数据库 collate 排序方式

## 1.4 数据库删除
直接删除
drop database 数据库名
判断删除
drop database if exists 数据库名

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEyOTA4NzAwMTZdfQ==
-->