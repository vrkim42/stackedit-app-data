## C语言链表讲解
之前的作业题
```
#include<stdio.h> 
#include<stdlib.h>
#include<string.h>
// 定义链表节点结构体
struct Node {
    char fruit_name[20];
    float price;
    struct Node* next;//指向下一节点的指针 
};
// 创建新节点
struct Node* createNode(char fruit_name[], float price) {//创建指向Node的结构体指针 
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));//为新节点申请空间 
    strcpy(newNode->fruit_name, fruit_name);//后者的内容复制给前者 
    newNode->price = price;//更新newNode相关节点的位置 
    newNode->next = NULL;//将next节点悬空方便下一个节点的输入 
    return newNode;
}
// 在链表末尾添加节点
void appendNode(struct Node** headRef, char fruit_name[], float price) {
    struct Node* newNode = createNode(fruit_name, price);
    if (*headRef == NULL) {
        *headRef = newNode;
    } else {
        struct Node* current = *headRef;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
}
// 在链表中查找节点
int findNode(struct Node* head, char fruit_name[]) {
    struct Node* current = head;
    while (current != NULL) {
        if (strcmp(current->fruit_name, fruit_name) == 0) {
            return 1; // 节点存在
        }
        current = current->next;
    }
    return 0; // 节点不存在
}
// 删除节点
void deleteNode(struct Node** headRef, char fruit_name[]) {
    struct Node* current = *headRef;
    struct Node* prev = NULL;
    while (current != NULL) {
        if (strcmp(current->fruit_name, fruit_name) == 0) {
            if (prev == NULL) {
                *headRef = current->next;
            } else {
                prev->next = current->next;
            }
            free(current);
            printf("%s 的信息已从链表中删除。\n", fruit_name);
            return;
        }
        prev = current;
        current = current->next;
    }
    printf("%s 的信息不在链表中。\n", fruit_name);
}
// 打印链表
void printList(struct Node* head) {
    struct Node* current = head;
    while (current != NULL) {
        printf("水果名：%s, 进价：%f\n", current->fruit_name, current->price);
        current = current->next;
    }
}
int main() {
    struct Node* head = NULL;
    printf("请输入水果名和进价信息，输入 End 结束：\n");
    while (1) {
        char fruit_name[20];
        float price;
        printf("水果名：");
        scanf("%s", fruit_name);
        if (strcmp(fruit_name, "End") == 0) {
            break;
        }
        printf("进价：");
        scanf("%f", &price);
        appendNode(&head, fruit_name, price);
    }
    printf("链表内容：\n");
    printList(head);
    // 查找并删除/添加 pear
    if (findNode(head, "pear")) {
        deleteNode(&head, "pear");
    } else {
        appendNode(&head, "pear", 2.5);
    }
    printf("更新后的链表内容：\n");
    printList(head);
    // 释放链表内存
    struct Node* temp;
    while (head != NULL) {
        temp = head;
        head = head->next;
        free(temp);
    }
    return 0;
}
```

## 动态链表的创建

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM2MzcxOTQzXX0=
-->