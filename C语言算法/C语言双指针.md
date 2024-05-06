## 双指针
  所有需要两个指针指向数组元素的题目都可以选择这种办法。
双指针是一种常用的算法技巧，它通常用于处理数组或链表等数据结构中的元素。双指针技巧可以帮助我们在 O(n) 时间复杂度内完成某些操作，例如数组的排序、查找、删除等，本题讲解能否找到数组中两数之和等于目标数。
```c
#include<stdio.h>

bool twoSum(int* arr, int n, int target){
	int l = 0;//左边界
	int r = n - 1;//右边界
	while(l < r){//大循环执行全部情况
		if(arr[l] + arr[r] == target){//找到了就返回true
		return true;
	}else if(arr[l] + arr[r] < target){//找不到变下标继续做
		l++;
	}else{
		r--;
	}
	}
	return false;//实在找不到返回false
}
int main(){
	int arr[] = {1, 2, 3, 4, 5};//已知数组 
	int target = 9;//要找的目标是这个 
	int n = sizeof(arr) /sizeof(arr[0]);
	if(twoSum(arr, n, target)){//外部函数实现 
	printf("FOUND!");
}else{
	printf("NOT FOUND!");
}
} 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTg2MzUxNjMzOCw0NDA5MDU2MTldfQ==
-->