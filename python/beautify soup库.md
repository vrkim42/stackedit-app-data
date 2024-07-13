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
.contents 节点的子标签
.childrenn 节点的子标签
.descendants 所有后续子孙节点进行便利
.next_sibling 返回按照HTML文本顺序的下一个平行节点标签
.previous_sibling 返回按照HTML文本顺序的上一个平行节点标签
.previous_siblings 迭代类型，返回所有按照HTML文本顺序的前序平行标签
.next_siblings 迭代类型，返回所有按照HTML文本顺序的后序平行标签
平行标签不一定获得标签类型也可以是string类型
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjA5NjA2Njc4Niw3OTI4MDIwNjEsLTUxNT
Q1NTQ2NCwtMTE0MTgzODM1OCwtMjg0ODM5MjQzLDcwODYwNjA1
MV19
-->