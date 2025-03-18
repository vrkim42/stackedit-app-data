## 二维差分

```c
#include <stdio.h>

void horizontalDifference(int arr[][4], int rows, int cols, int diff[][4]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (j > 0) {
                diff[i][j] = arr[i][j] - arr[i][j - 1];
            } else {
                diff[i][j] = arr[i][j]; // 边界条件
            }
        }
    }
}

void verticalDifference(int arr[][4], int rows, int cols, int diff[][4]) {
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (i > 0) {
                diff[i][j] = arr[i][j] - arr[i - 1][j];
            } else {
                diff[i][j] = arr[i][j]; // 边界条件
            }
        }
    }
}

int main() {
    int arr[4][4] = {
        {1, 2, 3, 4},
        {5, 6, 7, 8},
        {9, 10, 11, 12},
        {13, 14, 15, 16}
    };
    int rows = 4, cols = 4;
    int hor_diff[4][4], ver_diff[4][4];

    horizontalDifference(arr, rows, cols, hor_diff);
    verticalDifference(arr, rows, cols, ver_diff);

    printf("水平差分:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", hor_diff[i][j]);
        }
        printf("\n");
    }

    printf("垂直差分:\n");
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", ver_diff[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY2NDU5ODcwMl19
-->