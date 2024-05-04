栈
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

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTUxMDAwMDUwNl19
-->