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

## 静态链表的创建
```c
#define MAX_SIZE 100

typedef struct {
    int data;
    int next;
} StaticNode;

typedef struct {
    StaticNode nodes[MAX_SIZE];
    int head;
    int size;
} StaticLinkedList;

void initList(StaticLinkedList* list) {
    list->head = -1;
    list->size = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        list->nodes[i].next = -1;
    }
}

int insert(StaticLinkedList* list, int index, int value) {
    if (list->size >= MAX_SIZE) return -1; // List is full
    int newNode = list->size++;
    list->nodes[newNode].data = value;
    if (index == 0) {
        list->nodes[newNode].next = list->head;
        list->head = newNode;
    } else {
        int prev = list->head;
        for (int i = 1; i < index; i++) {
            prev = list->nodes[prev].next;
        }
        list->nodes[newNode].next = list->nodes[prev].next;
        list->nodes[prev].next = newNode;
    }
    return 0;
}

void delete(StaticLinkedList* list, int index) {
    if (list->head == -1) return; // List is empty
    if (index == 0) {
        int temp = list->head;
        list->head = list->nodes[temp].next;
        list->nodes[temp].next = -1;
    } else {
        int prev = list->head;
        for (int i = 1; i < index; i++) {
            prev = list->nodes[prev].next;
        }
        int temp = list->nodes[prev].next;
        list->nodes[prev].next = list->nodes[temp].next;
        list->nodes[temp].next = -1;
    }
    list->size--;
}
```

#### 动态链表
```c
#include <stdio.h>
#include <stdlib.h>

// 链表节点结构体
typedef struct Node {
    int data;
    struct Node *next;
} Node;

// 创建链表
Node *createList() {
    Node *head = (Node *)malloc(sizeof(Node));
    if (head == NULL) {
        return NULL;
    }
    head->data = 1;
    head->next = NULL;
    return head;
}

// 插入节点
void insertNode(Node **head, int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node *temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

// 删除节点
void deleteNode(Node **head, int data) {
    Node *temp = *head, *prev = NULL;
    if (temp != NULL && temp->data == data) {
        *head = temp->next;
        free(temp);
        return;
    }
    while (temp != NULL && temp->data != data) {
        prev = temp;
        temp = temp->next;
    }
    if (temp == NULL) return;
    prev->next = temp->next;
    free(temp);
}

// 遍历链表
void traverseList(Node *head) {
    Node *temp = head;
    while (temp != NULL) {
        printf("%d ", temp->data);
        temp = temp->next;
    }
    printf("\n");
}

int main() {
    Node *head =
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTI4MTY5MjAwMV19
-->