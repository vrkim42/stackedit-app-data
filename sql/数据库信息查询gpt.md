好的,我来总结一下SELECT子句的使用方法,并补充一些遗漏的内容:

1. SELECT 子句基础语法:
   ```sql
   SELECT column1, column2, ...
   FROM table_name;
   ```
   - 用于指定要检索的列
   - 多个列用逗号分隔
   - 可以使用 * 选择所有列

2. FROM 子句基础语法:
   ```sql
   FROM table_name;
   ```
   - 指定要查询的表

3. 通配符:
   - * 表示选择所有列
   - 使用示例: `SELECT * FROM table_name;`

4. 在SELECT中使用算术运算符:
   - 可以进行加(+)、减(-)、乘(*)、除(/)运算
   - 例如: `SELECT column1, column2 * 100 / column3 FROM table_name;`

5. 算术运算符优先级:
   - 乘法和除法优先于加法和减法
   - 可以使用圆括号()改变运算顺序

6. AS 关键字设置别名:
   - 语法: `column_name AS alias_name`
   - AS 可以省略
   - 别名可以用单引号''或反引号``包围,特别是当别名中包含空格或与SQL关键字冲突时

7. 补充:计算字段
   - 可以在SELECT语句中创建新的计算字段
   - 计算字段可以是简单的算术运算,也可以是复杂的函数或表达式

8. 别名的其他用法:
   - 可以为表设置别名: `FROM table_name AS alias`
   - 表别名通常用于简化复杂查询或自连接查询

9. SELECT子句的顺序:
   通常的顺序是 SELECT ... FROM ... WHERE ... GROUP BY ... HAVING ... ORDER BY ...

10. 注释:
    - 单行注释: --
    - 多行注释: /* ... */

11. 大小写:
    - SQL关键字通常大写,但这不是必须的
    - 表名和列名的大小写敏感性依赖于数据库系统

这个总结涵盖了SELECT子句的基本用法,包括列选择、计算字段、别名设置等关键概念。在实际应用中,这些基础知识可以组合使用,以满足各种复杂的查询需求。
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDM0ODc3MjcwXX0=
-->