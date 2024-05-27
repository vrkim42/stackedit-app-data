
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
这里我们假如链表最大值为100，方便之后的检索。
我们先定义静态链表的结构：

```c
#define MAX_SIZE 100

typedef struct {
    int data;  // 数据域
    int next;  // 游标域，指向下一个节点的下标
} StaticNode;

typedef struct {
    StaticNode nodes[MAX_SIZE];  // 静态链表的节点数组，每个节点通过这个数组存储数据和下一节点的指针，就是上面的那个结构体集合构成的数组。
    int head;  // 头节点的下标
    int size;  // 当前链表的大小
} StaticLinkedList;
```

#### 初始化

静态链表的初始化操作：

```c
void initList(StaticLinkedList* list) {这里使用的是结构体指针，表示的是指向结构体StaticLinkedList的指针list，区别后面讲。标记一
    list->head = -1;  // 初始时头节点为空
    list->size = 0;  // 初始时链表大小为0
    for (int i = 0; i < MAX_SIZE; i++) {
        list->nodes[i].next = -1;  // 将所有节点的next全部悬空方便下一步接入
    }
}//总而言之就是所有节点全部悬空，初始大小全为0
```

#### 增添节点

在静态链表中插入节点的操作（在索引index处插入数据value）：

```c
int insert(StaticLinkedList* list, int index, int value) {
    if (list->size >= MAX_SIZE) 
    return -1;  // 链表已满

    int newNode = list->size++;  // 新节点的下标为当前链表大小，同时size自增，已确认链表数加一,同时size的值代表着索引的位置，方便我们对节点进行插入。
    list->nodes[newNode].data = value;  // 设置新节点的数据域，nodes[newNode]是之前创建的节点数组，.data访问元素，然后赋值为value。

    if (index == 0) {  // 插入到链表头部，这个要单独列出来，因为使用的是头节点而不是索引下的next指针。
        list->nodes[newNode].next = list->head;//接入，这行代码将新节点的 next 指向当前的头节点。这是因为新节点将成为新的头节点，原来的头节点将变为第二个节点。
        list->head = newNode;//插入完了一定要更新头节点的位置，不然下次插入就麻烦了，这行代码将链表的头节点指针更新为新节点的索引，是链表操作中的一个重要步骤。
    } else {  // 插入到链表中部或尾部
        int prev = list->head;//这行代码保存头节点的索引到 prev，用于遍历找到插入位置的前一个节点。
        for (int i = 1; i < index; i++) {//从第二个链表开始遍历，直到找到插入位置的前一个节点。
            prev = list->nodes[prev].next;//上一个节点的 next 指向这个节点的头指针完成链接。
        }
        list->nodes[newNode].next = list->nodes[prev].next;//newnode的next前一秒在被插入链表的头节点，现在更新到他所在节点的 next
        list->nodes[prev].next = newNode;//这行代码将前一个节点的 next 更新为新节点的索引，完成新节点的插入。
    }

    return 0;  // 插入成功
}
```

### 删除节点

删除静态链表中指定位置的节点（在索引index处删除节点）：

```c
void delete(StaticLinkedList* list, int index) {//list是指向要操作对象的指针，便于对那个节点进行相关的操作，index是要进行操作地方的索引。
    if (list->head == -1) return;  // 链表为空

    if (index == 0) {  // 删除头节点
        int temp = list->head;//保留当前头节点的索引
        list->head = list->nodes[temp].next;//这行代码将链表的头节点指针更新为当前头节点的下一个节点的索引，即list->nodes[temp].next。这样，当前头节点被移除后，新的头节点将是原头节点的下一个节点。
        list->nodes[temp].next = -1;  //清空被删除节点的next域
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


### 为什么用结构体指针 标记一
如果我们不使用指针，初始化函数会是这样的：
```
void initList(StaticLinkedList list) {
    list.head = -1;
    list.size = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        list.nodes[i].next = -1;
    }
}
```
在这种情况下，`initList`函数接收到的是 `StaticLinkedList` 结构体的副本，函数内对 list 的修改不会影响原始的结构体。为了让 `initList` 函数能够修改原始结构体，我们使用指针：
```
void initList(StaticLinkedList* list) {
    list->head = -1;
    list->size = 0;
    for (int i = 0; i < MAX_SIZE; i++) {
        list->nodes[i].next = -1;
    }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY4ODc0MjU3MywtOTE0NDIxMDg2LC0xMT
AxMTM2MDY3LDEyMjQ1MDE0MDQsLTIwMzk5MzgyNTIsLTE0MTE0
MDU1MDldfQ==
-->