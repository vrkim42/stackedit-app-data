```c
#include<stdio.h>

int main(){
	int arr[] = {12,2,54,465,22,132};
	int n = sizeof(arr) / sizeof(arr[0]);
	for(int i = 0; i < n - 1; i++){
		for(int j = i; j < n - i - 1; j++){
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
eyJoaXN0b3J5IjpbLTczMjY0MTE5LC0yMTE5Mjg2Njk3XX0=
-->