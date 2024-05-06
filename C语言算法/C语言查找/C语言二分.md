二分查找
```c
#include<stdio.h>

int half_find(int* arr, int l, int r, int target){
	int mid = (l+r) / 2;
	while(l < r){
		if(arr[mid] == target){
		return mid;
	}else if(arr[mid] > target){
		return half_find(arr, l, mid, target);
	}else{
		return half_find(arr, mid, r, target);
	}
	}
	return -1;
}

int main(){
	printf("输出-1表示没找到。\n"); 
	int arr[] = {1, 3, 5, 7, 9};//要进行寻找的数组 
	int target = 7;//要找的数 
	printf("对应数的位置是：%d\n",(half_find(arr, 0, sizeof(arr) / sizeof(arr[0]), target) + 1));
	//传入数组，左边界，右边界
	return 0; 
} #include<stdio.h>

int half_find(int* arr, int l, int r, int target){
	int mid = (l+r) / 2;
	while(l < r){
		if(arr[mid] == target){
		return mid;
	}else if(arr[mid] > target){
		return half_find(arr, l, mid, target);
	}else{
		return half_find(arr, mid, r, target);
	}
	}
	return -1;
}

int main(){
	printf("输出-1表示没找到。\n"); 
	int arr[] = {1, 3, 5, 7, 9};//要进行寻找的数组 
	int target = 7;//要找的数 
	printf("对应数的位置是：%d\n",(half_find(arr, 0, sizeof(arr) / sizeof(arr[0]), target) + 1));
	//传入数组，左边界，右边界
	return 0; 
} 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTczNDk1NzYwMiwxMzA2NDkyMDcxXX0=
-->