### 库的引入
from bs4 import BeaufulSoup
soup = BeautifulSoup("mk","lxml")
soup = BeautifulSoup("<html>data</html>","html.parser")
soup = BeautifulSoup("mk","xml")
soup = BeautifulSoup("mk","html5lib")

### 基本元素
1. tag 标签，最基本的信息组织单元
2. name 名字 <p> xxx   </p>的名字是'p'
3. attributes 属性，字典形式组织 <tag>.attrs
4. navigablestring 标签内非属性字符串<<tag>.string
5. comment 注释

.parent 节点的父亲标签
.parents 节点先辈标签迭代类型，用于遍历先辈节点


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMzM3MzU5MSw3OTI4MDIwNjEsLTUxNT
Q1NTQ2NCwtMTE0MTgzODM1OCwtMjg0ODM5MjQzLDcwODYwNjA1
MV19
-->