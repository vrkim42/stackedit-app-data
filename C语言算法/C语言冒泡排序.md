## 冒泡排序
最简单的排序思路了，从第一个数开始进行遍历，如果他比第二个数大就“上浮”一位，反之不变，然后对下一个数进行处理，如此持续。
定义一个大循环，大循环包括总共进行的次数，然后小循环是每一次进行排序
```c
#include<stdio.h>

int main(){
	int arr[] = {12,2,54,465,22,132};//定义一个数组
	int n = sizeof(arr) / sizeof(arr[0]);//得出数组的大小
	for(int i = 0; i < n - 1; i++){//一共n个数，但是只需要比较n-1次即可
		for(int j = i; j < n - i - 1; j++){//这个循环进行每一次的比较，前面已经排完序号的数不需要再进行比较所以从i开始，一共执行n-i-1次结束
			if(arr[j] > arr[j + 1]){//交换数组中数的经典办法
				int temp = arr[j];
				arr[j] = arr[j+1];
				arr[j+1] = temp;
			}
		}
	}
	for(int i = 0; i< n; i++){//打印排完序号后的数组
		printf("%d\t", arr[i]);
	} 
} 
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNDQ2NzEzNTE5LC04MTA2Mzc3OSwtMjExOT
I4NjY5N119
-->