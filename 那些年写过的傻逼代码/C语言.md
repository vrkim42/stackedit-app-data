## 1
```c
#include<stdio.h>
#include<string.h>

int main(){
    char str[110];
    scanf("%s", str);
    int len = strlen(str);
    for(int i = len - 1; i >=0 ; i--){
        if(i != 0)
        printf("%c-", str[i]);
        if(i == 0)
        printf("%c", str[i]);
    }
}
```
优化后：
```c
#include <stdio.h>
#include <string.h>

int main(){
    char str[110];
    scanf("%s", str);
    int len = strlen(str);

    for(int i = len - 1; i >= 0; i--){
        printf("%c", str[i]);
        if(i != 0){
            printf("-");
        }
    }

    return 0;
}
```


## 2

<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1Mzk5NjMyNDNdfQ==
-->