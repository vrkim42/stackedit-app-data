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

### 节点的遍历
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

### 其他
1. prettify()将代码进行优化 eg:`soup.prettify()`和`soup.a.prettify()`
2. BeautifulSoup("<html>data</html>","html.parser")加载对应文档，然后进行识别，在上面引入部分有。
3. `find_all(name,attrs,recursive,string,**kwargs)`如：`soup.find_all('a')` 其中`name`是对标签名称的检索字符串，`attrs`对标签属性值的检索字符串，可标注属性检索。`recursive`是否对子孙全部检索，默认True。`(recursive = false)`  `string`<>...</>中字符串区域的检索字符串`(string = "Basic Python"]` `**kwargs`




### json xml yaml
所有类型的信息都可以使用这三种格式进行表示
`json`格式采用键值对，类似于字典 `“name”:["xxx", "sss"]` 套用`"name":{"newname":"中科大","oldname":"xxx"}`
`xml`与HTML语法类似
`yaml`无类型键值对，`name: - 北大 - 清华`以及 `text: xxxxxxxxxxxx`等，可以用#表示注释，-表示并列
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwODg0NjcyMjQsOTE4MjI2MDM1LC0xOD
k5NjQwNzYxLDQzMTEyOTk0NSwtMTQwNDg2MjQwNCwtMTI5ODE0
MzI2NiwyMDk2MDY2Nzg2LDc5MjgwMjA2MSwtNTE1NDU1NDY0LC
0xMTQxODM4MzU4LC0yODQ4MzkyNDMsNzA4NjA2MDUxXX0=
-->