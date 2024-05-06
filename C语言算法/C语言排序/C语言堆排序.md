堆排序
```c
#include <stdio.h>

// 用于交换两个元素的值
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

// 调整堆
void heapify(int arr[], int n, int i) {
    int largest = i;        // 初始化最大值为根节点
    int left = 2 * i + 1;   // 左子节点
    int right = 2 * i + 2;  // 右子节点

    // 如果左子节点大于根节点
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // 如果右子节点大于最大值
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // 如果最大值不是根节点，交换之，并递归地调整受影响的子树
    if (largest != i) {
        swap(&arr[i], &arr[largest]);
        heapify(arr, n, largest);
    }
}

// 堆排序函数
void heapSort(int arr[], int n) {
    // 构建最大堆（重排数组）
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // 一个个从堆顶取出元素
    for (int i = n - 1; i >= 0; i--) {
        // 移动当前根节点到数组末尾
        swap(&arr[0], &arr[i]);

        // 调用heapify减少堆的大小，并重新调整堆
        heapify(arr, i, 0);
    }
}

// 打印数组的函数
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    printf("\n");
}

// 主函数
int main() {
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapSort(arr, n);

    printf("Sorted array is \n");
    printArray(arr, n);
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5NzgwMDIwMjddfQ==
-->