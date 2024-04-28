### 创建链结构体
```c
typedef struct Student{
	int id;//Student的第一个属性id
	char name[21]; //Student的第二个属性name
	struct Student* next; //创建中间指针实现链表跳转
	} STU;//将结构体重命名为STU
```

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc3NzMxMTQxMF19
-->