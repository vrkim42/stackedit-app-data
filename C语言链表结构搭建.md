### 创建链结构体
```c
typedef struct Student{
	int id;//Student的第一个属性id
	char name[21]; //Student的第二个属性name
	struct Student* next; //创建中间指针实现链表跳转
	} STU;//将结构体重命名为STU
```
### main函数内准备部分
```c
STU *p, *head, *tail;//创建头节点，尾节点，动态访问节点。
head = NULL;
tail = NULL;//首个节点不存储信息
int n;// 链表的个数
scanf("%d", &n);

### 创建链表结构
```c
for(int i = 1; i <= n; i++){
p = (struct Student*)malloc(sizeof(struct Studeent));
scanf("%s", &p -> name);
scanf(
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMzODA4MjM3NV19
-->