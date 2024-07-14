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
生成器ling'hu


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzI2NTQ5MDIzLDE5NjQ4MzMxOTMsMTIxOT
U0MjEzNywtMjA0MTg3MDg3MiwxNzczMzUwNTQ4LC0zMzg4NTEw
MzMsLTEyNzA0MDI5ODgsMTQ5OTY4MzY1MywtMTE0MjM1MzEzLD
ExNTM5MzM3ODIsLTIwODg3NDY2MTJdfQ==
-->