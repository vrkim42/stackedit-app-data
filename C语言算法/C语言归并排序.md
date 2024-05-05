归并排序的思路是将数组分为多个数组，然后分别将多个数组的数字插入到元数组中达成排序的目的。

```c
先以分为两个数组为例，左边四个数有序，右边四个数也有序，这样啊我们就可以将这两个数组中的数一一比较，将小的放到结果数组中，然后其对应的数组序号加一。直到排序完成返回结果。
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
那么如果原数组没有已经排好序的部分而是一片混乱怎么办，简单，利用微分的思想，将他彻底打散成单个数组成分，利用递归进行排序。
```c
完全体归并排序。
#include <stdio.h>

void merge(int arr[], int L, int M, int R) {
    int LEFT_SIZE = M - L;//保存左数组大小
    int RIGHT_SIZE = R - M + 1;//右数组大小
    int left[LEFT_SIZE];//创建左数组
    int right[RIGHT_SIZE];//创建右数组
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
            arr[k] = left[i++];//左边数小先放左边的数 
        }else{
            arr[k] = right[j++];//右边数小放右边的 
        }
    }
    //for循环结束后可能有一个数组里的数没有全部放到arr数组中，这里放进去。 
    while(i < LEFT_SIZE){
        arr[k++] = left[i++];
    }
    while(j < RIGHT_SIZE){
        arr[k++] = right[j++];
    }
}

void mergesort(int arr[],int L,int R){
    if(L == R){
        return;
    }else{
        int M = (L + R) / 2;//找到数组中间点划分左右数组 
        mergesort(arr, L, M);//分割成单个数组 
        mergesort(arr, M + 1, R);
        merge(arr, L, M + 1, R);//进行排序 
    }
}


int main(void) {
    int arr[] = {6, 8, 10, 9, 4, 5, 2, 7};
    int L = 0;//左端点
    int R = 7;//左数组右端点
    mergesort(arr, L, R);
    int i;
    
    for(i = 0; i <= R; i++){
        printf("%d\n",arr[i]);
    }
    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTcxMjgzNTMwOSwtNDkyMDAxNTU1LDEzMj
U5OTUwMzgsLTUxMzQzOTQ2OSwtMjA4ODc0NjYxMiw0NDA5MDU2
MTldfQ==
-->