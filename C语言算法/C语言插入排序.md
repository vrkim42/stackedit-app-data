插入排序
```c
#include<stdio.h>

using namespace std;

void InsertSort(int a[],int l)
{
    int temp;
    int j;
    for(int i=1;i<l;i++)
    {
        if(a[i]<a[i-1])
        {
            temp=a[i];
            for(j=i-1;j>=0&&temp<a[j];j--)
            {
                a[j+1]=a[j];
            }
            a[j+1]=temp;

        }
        for(int k=0;k<l;k++)
            printf("%d ", k);
        putchar(10);

    }
}


int main()
{
    int a[10]={2,5,8,3,6,9,1,4,7};
    int b[10]={1,2,3,4,5,6,7,8,9};
    int len=9;
    InsertSort(a,len);
    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMTYxNjY3MTVdfQ==
-->