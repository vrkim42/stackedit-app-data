### 创建链结构体
```c
typedef struct Student{
	int id;//Student的第一个属性id
	char name[21]; //Student的第二个属性name
	Student* next; //创建中间指针实现链表跳转
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5ODk3Njg5NzhdfQ==
-->