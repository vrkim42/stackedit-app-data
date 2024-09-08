```
file = open("newfile.txt", "r")
print("初始化读写内容")
print(file.read())
print("完成")
file.close()
 
file = open("newfile.txt", "w")
file.write("新的内容")
file.close()
 
file = open("newfile.txt", "r")
print("写入新的内容")
print(file.read())
print("结束")
file.close()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExODI4NTk3NThdfQ==
-->