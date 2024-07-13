### 库的引入
from bs4 import BeaufulSoup
soup = BeautifulSoup("mk","lxml")
soup = BeautifulSoup("<html>data</html>","html.parser")
soup = BeautifulSoup("mk","xml")
soup = BeautifulSoup("mk","html5lib")

### 基本元素
1. tag 标签，最基本的信息组织单元
2. name 名字 <p><//p>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE4OTUxNzM4NzcsLTI4NDgzOTI0Myw3MD
g2MDYwNTFdfQ==
-->