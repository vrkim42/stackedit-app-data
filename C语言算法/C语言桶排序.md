
```c
#include <stdio.h>
#include <stdlib.h>

// 定义桶的结构体
struct Node {
    int data;
    struct Node* next;
};

// 插入排序，用于对桶内元素进行排序
void insertionSort(struct Node* bucket) {
    struct Node* i = NULL;
    struct Node* j = NULL;
    int temp;

    for (i = bucket; i != NULL; i = i->next) {
        temp = i->data;
        for (j = i->next; j != NULL; j = j->next) {
            if (temp > j->data) {
                int t = temp;
                temp = j->data;
                j->data = t;
            }
        }
        i->data = temp;
    }
}

// 桶排序函数
void bucketSort(int arr[], int n, int num_buckets) {
    // 创建桶数组
    struct Node* buckets[num_buckets];

    // 初始化桶数组为NULL
    for (int i = 0; i < num_buckets; i++) {
        buckets[i] = NULL;
    }

    // 将元素分配到桶中
    for (int i = 0; i < n; i++) {
        int index = arr[i] / num_buckets;
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = arr[i];
        newNode->next = NULL;

        // 插入新节点到对应的桶中
        if (buckets[index] == NULL) {
            buckets[index] = newNode;
        } else {
            struct Node* current = buckets[index];
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    // 对每个桶内的元素进行插入排序
    for (int i = 0; i < num_buckets; i++) {
        insertionSort(buckets[i]);
    }

    // 合并各个桶的元素到原始数组
    int index = 0;
    for (int i = 0; i < num_buckets; i++) {
        struct Node* current = buckets[i];
        while (current != NULL) {
            arr[index++] = current->data;
            current = current->next;
        }
    }

    // 释放桶数组中的节点内存
    for (int i = 0; i < num_buckets; i++) {
        struct Node* current = buckets[i];
        while (current != NULL) {
            struct Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
}

// 测试桶排序算法
int main() {
    int arr[] = {29, 25, 3, 49, 9, 37, 21, 43};
    int n = sizeof(arr) / sizeof(arr[0]);
    int num_buckets = 5;

    printf("原始数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    bucketSort(arr, n, num_buckets);

    printf("排序后的数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}#include <stdio.h>
#include <stdlib.h>

// 定义桶的结构体
struct Node {
    int data;
    struct Node* next;
};

// 插入排序，用于对桶内元素进行排序
void insertionSort(struct Node* bucket) {
    struct Node* i = NULL;
    struct Node* j = NULL;
    int temp;

    for (i = bucket; i != NULL; i = i->next) {
        temp = i->data;
        for (j = i->next; j != NULL; j = j->next) {
            if (temp > j->data) {
                int t = temp;
                temp = j->data;
                j->data = t;
            }
        }
        i->data = temp;
    }
}

// 桶排序函数
void bucketSort(int arr[], int n, int num_buckets) {
    // 创建桶数组
    struct Node* buckets[num_buckets];

    // 初始化桶数组为NULL
    for (int i = 0; i < num_buckets; i++) {
        buckets[i] = NULL;
    }

    // 将元素分配到桶中
    for (int i = 0; i < n; i++) {
        int index = arr[i] / num_buckets;
        struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
        newNode->data = arr[i];
        newNode->next = NULL;

        // 插入新节点到对应的桶中
        if (buckets[index] == NULL) {
            buckets[index] = newNode;
        } else {
            struct Node* current = buckets[index];
            while (current->next != NULL) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    // 对每个桶内的元素进行插入排序
    for (int i = 0; i < num_buckets; i++) {
        insertionSort(buckets[i]);
    }

    // 合并各个桶的元素到原始数组
    int index = 0;
    for (int i = 0; i < num_buckets; i++) {
        struct Node* current = buckets[i];
        while (current != NULL) {
            arr[index++] = current->data;
            current = current->next;
        }
    }

    // 释放桶数组中的节点内存
    for (int i = 0; i < num_buckets; i++) {
        struct Node* current = buckets[i];
        while (current != NULL) {
            struct Node* temp = current;
            current = current->next;
            free(temp);
        }
    }
}

// 测试桶排序算法
int main() {
    int arr[] = {29, 25, 3, 49, 9, 37, 21, 43};
    int n = sizeof(arr) / sizeof(arr[0]);
    int num_buckets = 5;

    printf("原始数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    bucketSort(arr, n, num_buckets);

    printf("排序后的数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTkzMDI1MjIyM119
-->