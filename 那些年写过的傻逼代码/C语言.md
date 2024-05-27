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
```c
#include<stdio.h>
#include<string.h>

int main(){
    char num[1010];
    scanf("%s", num);
    int len = strlen(num);
    int flag = 0;
    for(int i = 0; i <= 9; i++){
        for(int j = 0; j < len; j++){
            if(i == num[j])
                flag++;
        }
        if(flag != 0)
        printf("%d:%d\n",i,flag);
        flag = 0;
    }
    
}
```
优化后
```
#include <stdio.h>
#include <string.h>

int main(){
    char num[1010];
    scanf("%s", num);
    int len = strlen(num);
    int count[10] = {0};  // 初始化一个数组来存储0到9的计数

    // 统计每个数字字符出现的次数
    for(int j = 0; j < len; j++){
        if(num[j] >= '0' && num[j] <= '9'){  // 确保只统计数字字符
            count[num[j] - '0']++;
        }
    }

    // 输出结果
    for(int i = 0; i <= 9; i++){
        if(count[i] != 0){
            printf("%d:%d\n", i, count[i]);
        }
    }

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzQwMzk0Mjc1XX0=
-->