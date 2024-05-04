```c
#include<stdio.h>

int main(){
	int arr[] = {12,2,54,465,22,132};//定义一个数组
	int n = sizeof(arr) / sizeof(arr[0]);//得出数组的大小
	for(int i = 0; i < n - 1; i++){//一共n个数，但是只需要比较n-1次即可
		for(int j = i; j < n - i - 1; j++){//这个循环进行mei'yi'ci'de
			if(arr[j] > arr[j + 1]){
				int temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	for(int i = 0; i< n; i++){
		printf("%d\t", arr[i]);
	} 
} 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTYzMzg4MTYyNCwtMjExOTI4NjY5N119
-->