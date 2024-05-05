计数排序
计数排序通过统计每个元素出现的频次，然后按照元素的大小顺序将其放置到正确的位置，实现排序。
```c
#include <stdio.h>

// 计数排序函数
void countSort(int arr[], int n) {
    // 寻找数组中的最大值以确定计数数组的大小
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // 创建计数数组并初始化为0
    int count[max + 1];
    for (int i = 0; i <= max; i++) {
        count[i] = 0;
    }

    // 统计每个元素的出现次数
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // 将计数数组转换为位置数组，表示每个元素在排序后数组中的位置
    for (int i = 1; i <= max; i++) {
        count[i] += count[i - 1];
    }

    // 创建临时数组以存储排序后的结果
    int output[n];
    for (int i = 0; i < n; i++) {
        output[i] = 0;
    }

    // 根据位置数组将元素放置到正确的位置上
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }

    // 将排序后的结果复制回原始数组
    for (int i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// 测试计数排序算法
int main() {
    int arr[] = {4, 2, 2, 8, 3, 3, 1};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("原始数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    countSort(arr, n);

    printf("排序后的数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbODM3MzUxNzg3XX0=
-->