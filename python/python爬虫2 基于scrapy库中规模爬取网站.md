## scrapy库
	爬虫框架
![输入图片说明](/imgs/2024-07-14/FlOKGdsmur9IBtXp.png)
## scrapy基恩框架
![输入图片说明](/imgs/2024-07-14/GDQH68vcjuvhgwvo.png)
![输入图片说明](/imgs/2024-07-14/pyR4PaoSc19ogOSB.png)


## 步骤
cd 到相应的文件夹
scrapy startproject + project名字
cd project名字
scrapy genspider + 爬虫名称 + 对应网址
更改demo.py到自己想要的类型
最后 scarpy crawl demo


## yield关键字 -》 生成器
- 生成器是一个不断产生的值
- 包含yield语句的函数是一个生成器
- 生成器产生一个只以后冻结，被唤醒以后再产生一个值

```
def gen(n):
	for i in range(n):
		yield i**2
```

![输入图片说明](/imgs/2024-07-14/oYtQ6CZbvGXg7SCs.png)
生成器灵活省空间速度快
![输入图片说明](/imgs/2024-07-14/ktnvG3dqJKeNKbjP.png)

## requests类                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
![输入图片说明](/imgs/2024-07-14/Ka8DZI8SYWD38blx.png)

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE0MjczNjk4MywxOTY0ODMzMTkzLDEyMT
k1NDIxMzcsLTIwNDE4NzA4NzIsMTc3MzM1MDU0OCwtMzM4ODUx
MDMzLC0xMjcwNDAyOTg4LDE0OTk2ODM2NTMsLTExNDIzNTMxMy
wxMTUzOTMzNzgyLC0yMDg4NzQ2NjEyXX0=
-->