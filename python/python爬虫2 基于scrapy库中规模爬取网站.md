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

## response类
![输入图片说明](/imgs/2024-07-14/Qx3E5W7Prk64Bf7t.png)

## item类



css selectorrr

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NjIwNTAwNTAsMTk2NDgzMzE5MywxMj
E5NTQyMTM3LC0yMDQxODcwODcyLDE3NzMzNTA1NDgsLTMzODg1
MTAzMywtMTI3MDQwMjk4OCwxNDk5NjgzNjUzLC0xMTQyMzUzMT
MsMTE1MzkzMzc4MiwtMjA4ODc0NjYxMl19
-->