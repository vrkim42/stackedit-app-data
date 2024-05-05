先初始化序号为0-9十个桶，先根据个位的数，将个位0与桶编号相同的数放进对应的桶中，按照0 - 9 的顺序将数然后根据十位数
```c
#include <stdio.h>

// 获取数组中的最大值
int getMax(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }
    return max;
}

// 使用计数排序根据指定的位数对数组进行排序
void countSort(int arr[], int n, int exp) {
    int output[n]; // 存储排序后的结果
    int i, count[10] = {0};

    // 统计每个数字出现的次数
    for (i = 0; i < n; i++) {
        count[(arr[i] / exp) % 10]++;
    }

    // 将计数数组转换为位置数组，表示每个数字在排序后的数组中的位置
    for (i = 1; i < 10; i++) {
        count[i] += count[i - 1];
    }

    // 构建排序后的数组
    for (i = n - 1; i >= 0; i--) {
        output[count[(arr[i] / exp) % 10] - 1] = arr[i];
        count[(arr[i] / exp) % 10]--;
    }

    // 将排序后的数组复制回原数组
    for (i = 0; i < n; i++) {
        arr[i] = output[i];
    }
}

// 基数排序函数
void radixSort(int arr[], int n) {
    // 获取数组中的最大值，以确定要进行基数排序的位数
    int max = getMax(arr, n);

    // 对每个位数进行计数排序
    for (int exp = 1; max / exp > 0; exp *= 10) {
        countSort(arr, n, exp);
    }
}

// 测试基数排序算法
int main() {
    int arr[] = {170, 45, 75, 90, 802, 24, 2, 66};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("原始数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    radixSort(arr, n);

    printf("排序后的数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTIwODI5ODk4MThdfQ==
-->