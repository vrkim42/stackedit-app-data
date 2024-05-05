插入排序
思路：设定第一个数有序，分为第一个数和后面无序的数两部分，然后把后面的数按序插入到前面有序的部分中。
```c
#include<stdio.h>

void InsertSort(int a[],int l) {
	for(int i=1; i<l; i++) {//从第二个数开始
		if(a[i]<a[i-1]) {
			int temp=a[i];
			int j;
			for(j=i-1; j>=0&&temp<a[j]; j--) {
				a[j+1]=a[j];
			}
			a[j+1]=temp;

		}
	}
	for(int k=0; k<l; k++)
		printf("%d ", k);
}


int main() {
	int a[10]= {2,5,8,3,6,9,1,4,7};
	int len=9;
	InsertSort(a,len);
	return 0;
}

```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM0MjMxODcxOV19
-->