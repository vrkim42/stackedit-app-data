### SQL建库语句的基础语法

1. **SQL代码的基本构成**：SQL代码由关键字、表名、列名和注释组成。关键字如`SELECT`、`CREATE`、`WHERE`等，注释用`--`表示，分号用于结束语句。SQL不区分大小写，缩进不严格。

2. **CREATE关键字的基础功能与语法结构**：
   ```sql
   CREATE DATABASE tshop CHARSET=utf8mb4;
   ```
   这里`tshop`是数据库名称，`CHARSET=utf8mb4`指定字符集以支持各种字符。

3. **数据库存储字符类型**：通过`CHARSET=utf8mb4`支持中、英、emoji等各种类型的字符。

### SQL建表语句的基础语法

1. **创建表格的基本要求**：表名、字段、字段类型与约束。表名唯一，字段名需遵循命名规则，数据类型如`INT`、`VARCHAR`等。

2. **CREATE TABLE的基础功能与语法结构**：
   ```sql
   CREATE TABLE tshop.commodity (
       id INT PRIMARY KEY AUTO_INCREMENT,
       name VARCHAR(255) NOT NULL UNIQUE,
       price DECIMAL(10, 2),
       create_time DATETIME DEFAULT NOW()
   );
   ```

3. **USE关键字指定操作数据库**：
   ```sql
   USE tshop;
   ```

### SQL插入语句的基础语法

1. **使用INSERT关键字插入数据**：
   ```sql
   INSERT INTO tshop.commodity VALUES (1, 'SHARK TEE BLACK', 699, '2023/1/12 12:22:32');
   ```

2. **插入数据的两种方法**：
   - **全列插入**：
     ```sql
     INSERT INTO tshop.commodity VALUES (1, 'SHARK TEE BLACK', 699, '2023/1/12 12:22:32');
     ```
   - **指定列插入**：
     ```sql
     INSERT INTO tshop.commodity (name, price) VALUES ('SHARK TEE BLACK', 699);
     ```

3. **关于未选择的字段**：
   - 若字段有`DEFAULT`或`AUTO_INCREMENT`，会自动填充。
   - 若无，字段则为`NULL`。

### 注意事项
插入数据时需确保数据类型与字段类型一致，并遵循约束规则。
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQ1OTk0MTM0NV19
-->