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
```
### 创建链表结构
```c
for(int i = 1; i <= n; i++){
p = (struct Student*)malloc(sizeof(struct Student));//为p申请内存
scanf("%s", p->name); // 修正：移除了&，因为数组名本身就是地址
scanf("%d", &p -> id);//赋值给id
tail -> next = p;//将next指向p的地址
tail = p;//将原先tail的位置更新到申请的p的地址
tail -> next = NULL;//将此链表的next指针指向空，以便下一次插入链表
}
```
### 链表的访问
```c
p = head -> next//这样做跳过了第一个节点，因为第一个节点没有元素，也可以直接 p = head 使p的位置更新到头节点访问第一个链表元素。
while(p != NULL){
//我们每次最后将p的位置更新到结构体的next，当读取到最后时，next指向NULL，即p = NULL，循环结束。
printf("%s\t", p -> name);//输出姓名
printf("%d\n", p -> id);// 输出id
p = p -> next;//将p的位置更新到next以便于下次链表数据的读取，或者判断循环是否结束。
}
```
### 链表的插入
```c
STU *q;//新建节点
scanf("%s", &q -> name);
scanf("%d",&q -> id);
p = head;//从头节点开始遍历查找位置
while(p -> next != NULL){
	if(p -> next -> id > q -> id){// 插入条件
		q -> next = p -> next;// 将q的next指针位置更新到p的next指针位置
		p -> next = q;//将q接入到链表中
		break;
		}
		p = p -> next;//更新到next便于下一步操作
	}
```
### 链表的删除
```c
int x;
scanf("%d", & x);//根据id 删除对应链表
p -> head;
while(p -> next != NULL){
if(p -> id == x){
STU *t;//新建一个结构体指针存放对应指针位置
t = p -> next;//将t指向目标节点
p -> next = p ->next -> next;//将next节点略过对应的t节点
free(t);//释放t节点内存
break;
}
p = p -> next;
}

<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA4NTU2NTc1OCwxODE2MTc4MTIxLC0yOD
AzMDg0NzEsLTUwMTk2MjUyOF19
-->