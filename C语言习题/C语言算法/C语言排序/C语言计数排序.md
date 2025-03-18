计数排序
计数排序是一种高效的排序算法，适用于整数排序，特别是当整数范围不大时。它的基本思想是通过统计每个元素出现的次数，然后根据这些统计结果直接将元素放到正确的位置。具体步骤如下：
1. 找出数组中的最大值和最小值，确定计数数组的大小。
2. 创建一个计数数组，大小为最大值减去最小值加一，用于计数。
3. 遍历输入数组，统计每个元素出现的次数，存入计数数组中。
4. 重建数组，按计数数组的顺序将元素放回原数组或新数组中。
5. 输出排序后的数组。
计数排序的时间复杂度是O(n+k)，其中n是数组的长度，k是数组中最大值和最小值之差。这种排序算法特别适合于整数排序，尤其是当k不大时。它的优点是简单、高效，且不需要进行比较，但缺点是适用范围有限，需要额外的内存空间，对数据类型有要求。

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
eyJoaXN0b3J5IjpbLTE0NjYxOTkyNDNdfQ==
-->