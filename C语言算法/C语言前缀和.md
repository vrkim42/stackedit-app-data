前缀和
思路是保存一个要进行前缀和数组的副本，然后利用副本将前缀和的值返回到结果数组中，最后循环打印结果数组的值。
```c
#include<stdio.h>

void prefixSum(int *arr, int n){
	int arr1[n];
	for(int i = 0; i < n; i++){
		arr1[i] = arr[i];
	}
	for(int i = 1; i < n; i ++){
		arr[i] = arr1[i - 1] + arr1[i];
	}
	for(int i = 0; i < n; i++){
		printf("%d\n", arr[i]);	
	}
}

int main() {
	int arr[] = {2, 4, 6, 10, 13};
	int n = sizeof(arr) / sizeof(arr[0]);
	prefixSum(arr, n);
	 
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk1MDE3NTk3NywtMjA4ODc0NjYxMl19
-->