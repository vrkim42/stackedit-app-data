# 区别
栈相当于一个弹匣，只能从入口放入和取出物品，所以正序放入倒叙取出，而队列相当于一个

## 栈
```c
#include<stdio.h>

int main(){
	int a[1000];//创建一个数组存储信息
	int top = -1;//栈的初始化
	for(int i = 0; i < 10; i++){
		a[++top] = i;
	} 
	for(int i = 0; i < 10; i++){
		printf("%d", a[top--]);
	}
} 
```
## 队列
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwNDgyMzAwOTVdfQ==
-->