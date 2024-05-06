思路和二分查找差不多。
```c
#include <stdio.h>

int ternarySearch(int arr[], int low, int high, int target) {
    if (low <= high) {
        int mid1 = low + (high - low) / 3;
        int mid2 = high - (high - low) / 3;

        if (arr[mid1] == target) {
            return mid1;
        }
        if (arr[mid2] == target) {
            return mid2;
        }

        if (target < arr[mid1]) {
            return ternarySearch(arr, low, mid1 - 1, target);
        }
        if (target > arr[mid2]) {
            return ternarySearch(arr, mid2 + 1, high, target);
        }

        return ternarySearch(arr, mid1 + 1, mid2 - 1, target);
    }
    return -1; // 目标值不在数组中
}

int main() {
    int arr[] = {1, 3, 5, 7, 9, 11};
    int size = sizeof(arr) / sizeof(arr[0]);
    int target = 7;
    int index = ternarySearch(arr, 0, size - 1, target);

    if (index != -1) {
        printf("元素 %d 在数组中的索引是 %d。\n", target, index);
    } else {
        printf("元素 %d 在数组中未找到。\n", target);
    }

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwODA5MDY0M119
-->