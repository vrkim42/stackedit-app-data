归并排序的思路是将数组分为多个数组，然后分别将多个数组的数字插入到元数组中达成排序的目的。

```c
先以分为两个数组为例，左边四个数有序，右边四个数也有序，这样就省去了将每个数都划分成孤立数组的办法，当然后者才是归并排序的完全体，这个只是帮助大家理解归并数组思路。
#include <stdio.h>

void merge(int arr[], int L, int M, int R) {
    int LEFT_SIZE = M - L;保存左数组大小
    int RIGHT_SIZE = R - M + 1;//右数组大小
    int left[LEFT_SIZE];创建左数组
    int right[RIGHT_SIZE];创建右数组
    //fill in the left sub array;
    int i ,j , k;
    for(i = L;i < M; i++){
        left[i - L] = arr[i];//i - L相当于从0开始自增
    }
    //fill in the right array
    for(i = M; i <= R; i++){
        right[i - M] = arr[i];
    }
    //fill in the original array
    i = 0;  j = 0;  k = L;//L的值在此是0,但是使用L方便控制循环，i和j分别计数左右数组的使用量。
    for(;i < LEFT_SIZE && j < RIGHT_SIZE; k++){//循环条件是左右数组还有剩余。
        if(left[i] < right[j]){
            arr[k] = left[i++];//
        }else{
            arr[k] = right[j++];
        }
    }
}

int main(void) {
    int arr[] = {3,4,5,6,2,7,8,9};//数组
    int L = 0;//左端点
    int M = 4;//右数组右端点
    int R = 7;//左数组右端点
    merge(arr, L, M, R);
    int i = 0;//打印
    while(i < R + 1){
        printf("%d",arr[i++]);
    }
    return 0;
}
```
```c
完全体归并排序。

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ5MjAwMTU1NSwxMzI1OTk1MDM4LC01MT
M0Mzk0NjksLTIwODg3NDY2MTIsNDQwOTA1NjE5XX0=
-->