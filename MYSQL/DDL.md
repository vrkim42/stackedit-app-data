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
select database())
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcwMTY0MzcwN119
-->