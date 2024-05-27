
### 什么是静态链表

静态链表是一种链表的实现方式，但不同于常规的动态链表，它在存储上**使用数组**而不是指针。这种实现方式在某些情况下具有一定的优势，比如在**不支持动态内存分配**的环境中使用。

### 静态链表的结构

静态链表通过一个数组和一个“游标”来实现。数组中的每个元素包含两个部分：

1. 数据域：存储节点的数据。
2. 游标域：存储下一个节点在数组中的下标。

通常，静态链表会定义一个特殊的值（例如-1）来表示链表的结束。

### 详细分析

#### 优点

1. **固定内存开销**：因为静态链表使用的是数组，所以它的内存分配是*一次性的，固定的*。这在一些内存管理较为严格的环境中非常有用。
2. **没有内存碎片**：动态链表可能会因为频繁的内存分配和释放导致内存碎片问题，而静态链表则不会有这个问题。
3. **简化内存管理**：无需考虑动态分配和释放的问题，减少了内存泄漏的风险。

#### 缺点

1. **灵活性不足**：数组的大小在初始化时确定，无法根据实际需要动态扩展。因此，当链表需要存储的元素数量超出预设大小时，会导致问题。
2. **效率问题**：由于数组的元素位置是固定的，插入和删除操作可能需要移动大量的元素，导致效率降低。
3. **空间浪费**：如果链表的实际使用大小远小于数组的大小，会造成内存的浪费。

### 实现示例

#### 静态链表的基本结构

我们先定义静态链表的结构：

```c
#define MAX_SIZE 100

typedef struct {
    int data;  // 数据域
    int next;  // 游标域，指向下一个节点的下标
} StaticNode;

typedef struct {
    StaticNode nodes[MAX_SIZE];  // 静态链表的节点数组
    int head;  // 头节点的下标
    int size;  // 当前链表的大小
} StaticLinkedList;
```

#### 初始化

静态链表的初始化操作：

```c
void initList(StaticLinkedList* list) {
    list->head = -1;  // 初始时头节点为空
    list->size = 0;  // 初始时链表大小为0
    for (int i = 0; i < MAX_SIZE; i++) {
        list->nodes[i].next = -1;  // 将所有节点的next域初始化为-1
    }
}
```

#### 增添节点

在静态链表中插入节点的操作（在索引index处插入数据value）：

```c
int insert(StaticLinkedList* list, int index, int value) {
    if (list->size >= MAX_SIZE) 
    return -1;  // 链表已满

    int newNode = list->size++;  // 新节点的下标为当前链表大小
    list->nodes[newNode].data = value;  // 设置新节点的数据域

    if (index == 0) {  // 插入到链表头部
        list->nodes[newNode].next = list->head;
        list->head = newNode;
    } else {  // 插入到链表中部或尾部
        int prev = list->head;
        for (int i = 1; i < index; i++) {
            prev = list->nodes[prev].next;
        }
        list->nodes[newNode].next = list->nodes[prev].next;
        list->nodes[prev].next = newNode;
    }

    return 0;  // 插入成功
}
```

### 删除节点

删除静态链表中指定位置的节点（在索引index处删除节点）：

```c
void delete(StaticLinkedList* list, int index) {
    if (list->head == -1) return;  // 链表为空

    if (index == 0) {  // 删除头节点
        int temp = list->head;
        list->head = list->nodes[temp].next;
        list->nodes[temp].next = -1;  // 清空被删除节点的next域
    } else {  // 删除链表中部或尾部的节点
        int prev = list->head;
        for (int i = 1; i < index; i++) {
            prev = list->nodes[prev].next;
        }
        int temp = list->nodes[prev].next;
        list->nodes[prev].next = list->nodes[temp].next;
        list->nodes[temp].next = -1;  // 清空被删除节点的next域
    }

    list->size--;  // 链表大小减1
}
```

### 遍历节点

遍历静态链表并打印所有节点的数据：

```c
void traverse(StaticLinkedList* list) {
    int current = list->head;
    while (current != -1) {
        printf("%d ", list->nodes[current].data);  // 打印当前节点的数据
        current = list->nodes[current].next;  // 移动到下一个节点
    }
    printf("\n");
}
```

### 示例

下面是一个使用上述功能的完整示例：

```c
#include <stdio.h>

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
    if (list->size >= MAX_SIZE) return -1;

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
    if (list->head == -1) return;

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

void traverse(StaticLinkedList* list) {
    int current = list->head;
    while (current != -1) {
        printf("%d ", list->nodes[current].data);
        current = list->nodes[current].next;
    }
    printf("\n");
}

int main() {
    StaticLinkedList list;
    initList(&list);

    insert(&list, 0, 10);
    insert(&list, 1, 20);
    insert(&list, 2, 30);
    insert(&list, 1, 15);

    printf("链表内容: ");
    traverse(&list);

    delete(&list, 1);
    printf("删除索引1后: ");
    traverse(&list);

    delete(&list, 0);
    printf("删除索引0后: ");
    traverse(&list);

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE0MTE0MDU1MDldfQ==
-->