## 快速排序
快排的思路是找到一个基准值，然后将大于基准值的放在右边，小于基准值的放在左边，完成排序，没错，也要进行微分达到宏观处理一切数据的办法。
```c
#include <stdio.h>
#include <stdlib.h>
#define  N  10//宏定义数组大小
 
int quick_sort(int *a, int low, int high)//导入数组，左端点和右端点
{
	int i = low;	//左端点
	int j = high;	//右端点
	int key = a[i]; //将第一个数作为基准值，快排的灵魂所在。
	while (i < j)//直到排完序结束
	{
		while(i < j && a[j] >= key)//i<j防止出现越界，a[j] >= key是要找出基准值右边比基准值小的数与基准值互换位置，直到右边都比基准值大为止。
		{
			j--;
		}//如果不成立，那么a[j] <= key;右面的比基准值小了，那就把a[j]的数据给a[i]	
		a[i] = a[j];	
 //这一步同理找出左边比基准值大的数和基准值互换直到都小于基准值为止。
		while(i < j && a[i] <= key)
		{
			i++;
		}
		//移动完以后，把新的位置的a[i]的数值 给刚才的 a[j],然后开始下一次循环
		a[j] = a[i];
	}
 
	//跳出循环，将基准值放入数据a[i]中
	a[i] = key;
	//这个部分和前面归并一样，将数组划分为无数个小部分，使的其可以应对所有一般情况
	if (i-1 > low) //i - 1还比low大，说明还没排到边
	{
		quick_sort(a, low, i-1);
	}

	if (i+1 < high)
	{
		quick_sort(a, i+1, high);
	}
 
	return 0;
} 
 
int main()
{
	int a[N] = {1, 3, 5, 7, 9, 2, 4, 6, 8, 0}
	quick_sort(a, 0, N-1);
														
	printf("排序后:\n");
	for(i = 0; i < N; i++)
	{
		printf("%d ", a[i]);
	}
	putchar(10);
	
	return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMjEwMzYyOTAwNV19
-->