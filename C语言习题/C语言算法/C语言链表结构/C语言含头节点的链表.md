```c
#include<stdio.h>
#include<stdlib.h>

typedef struct Student{
	int id;
	char name[21];
	struct Student* next;//包含一个指向下一阶段的指针 
}STU;//创建学生对象 


int main(){
	STU *p, *tail, *head;
	p = (struct Student*)malloc(sizeof(struct Student));//创建头节点 
	head = p;//修改头指针的位置到p节点 
	tail = p;//同理 
	p -> next = NULL;//指针悬空 
	int n;
	printf("请输入学生的数量：\n");
	scanf("%d", &n);//读取多少个学生 
	for(int i = 0; i < n; i++){//信息搜集 
		p = (struct Student*)malloc(sizeof(struct Student));//创建学生信息节点 
		printf("请输入第%d个学生的姓名。\n", i+1);
		scanf("%s", p -> name);//数组名存放数组地址，所以这里无需取地址 
		printf("请输入第%d个学生的id。\n", i+1);
		scanf("%d", &p -> id);//导入学生id 
		tail -> next = p;//将上一个节点的next指向p，使p接入链表 
		tail = p;//将尾节点位置更新，链表彻底接入 
		tail -> next = NULL;//尾节点的next悬空，便于下一次的接入 
	}
	p = head -> next;//这里指向head节点的next跳过了头节点，回归之前的代码可以看出头节点并无实际意义 
	while(p != NULL){//当读到NULL时就到了链表的末尾。 
		printf("学生的姓名是%s\n", p -> name);
		printf("学生的id是%d\n", p -> id);
		p = p -> next;
	}	
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIxMjI3MTEwNThdfQ==
-->