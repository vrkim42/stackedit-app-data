## 
```c
#include <stdio.h>
//选择排序，挑出其中一个数，和他相邻的数比较，满足相应要求后选择将那个数变成所选数或者保持不变，以此循环
int main(){
    int arr[5] = {1,3,5,2,4};
        printf("排序后的结果是:\n");
        for(int i = 1;i <= 5;i++){//大循环执行五次，要选择五个数进行比较
            int t = arr[i];//存储所选数
            int j = i-1;//选择要比较的相邻数
            while(j >= 0 && arr[j] > t){//升序排序
                arr[j+1] = arr[j];
                arr[j] = t;
                j--;
            }
        }
        for(int i = 0;i < 5;i++){
            printf("%-4d",arr[i]);
        }
    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjQ5NzE2MjkzXX0=
-->