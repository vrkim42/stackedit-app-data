C语言差分
```c
#include<stdio.h>

#define N 10010
int l, r, c;
int a[N], b[N];
void insert(int r, int l, int c){
    b[l] += c;
    b[r + 1] -= c;
}

int main(){
    int n,m;
    scanf("%d%d",&n,&m);
    for(int i = 0; i < n; i++){
        scanf("%d", &a[i]);
    }
    for(int i = 1; i <= n; i++){
        insert(i, i ,a[i]);
    }
    while(m--){
        scanf("%d%d%,d",&l,&r,&c);
        insert(r,l,c);
    }
    for(int i = 1; i <= n; i++){
        b[i] += b[i - 1];
        printf("%d", b[i]);
    }
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTIwNjE3OTk5NV19
-->