希尔排序
优化版的插入排序
```c
#include <stdio.h>

// 希尔排序函数
void shellSort(int arr[], int n) {
    // 定义间隔序列
    int gap = n / 2;
    int i, j, temp;

    // 不断缩小间隔，直至间隔为1
    while (gap > 0) {
        // 对每个子序列进行插入排序
        for (i = gap; i < n; i++) {
            temp = arr[i];
            j = i;

            // 在当前子序列中进行插入排序
            while (j >= gap && arr[j - gap] > temp) {
                arr[j] = arr[j - gap];
                j -= gap;
            }

            // 将temp插入到正确位置
            arr[j] = temp;
        }

        // 缩小间隔
        gap /= 2;
    }
}

// 测试希尔排序算法
int main() {
    int arr[] = {12, 34, 54, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    printf("原始数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    shellSort(arr, n);

    printf("排序后的数组：\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjYyNzY2MjAxXX0=
-->