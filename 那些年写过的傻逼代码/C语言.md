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

# 3
```c
#include<stdio.h>
#include<string.h>

int main(){
    char str[81];
    fgets(str,sizeof(str),stdin);
    int arr;
    scanf("%d", &arr);
    if(arr > 0){
        for(int i = 0; i < strlen(str); i++){
            if((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z')){
                if(str[i] >= 'a' && str[i] <= 'z'){
                    str[i] += arr;
                if(str[i] >= 'z'){
                    str[i] -= 26;
                }
                }else{
                    str[i] += arr;
                    if(str[i] >= 'Z'){
                        str[i] -= 26;
                    }
                }
                
            }
        }
    }else{
        for(int i = 0; i < strlen(str); i++){
            if((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' || str[i] <= 'Z')){
                if(str[i] >= 'a' && str[i] <= 'z'){
                    str[i] += arr;
                if(str[i] <= 'a'){
                    str[i] += 26;
                }
                }else{
                    str[i] += arr;
                    if(str[i] <= 'A'){
                        str[i] += 26;
                    }
                }
                
            }
        }
    }
    printf("%s", str);
}
```
you hua
```c
#include <stdio.h>
#include <string.h>

void caesarCipher(char *str, int offset) {
    int len = strlen(str);
    for (int i = 0; i < len; i++) {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z')) {  // 检查是否为字母
            if (islower(str[i])) {  // 处理小写字母
                str[i] = 'a' + (str[i] - 'a' + offset + 26) % 26;
            } else {  // 处理大写字母
                str[i] = 'A' + (str[i] - 'A' + offset + 26) % 26;
            }
        }
    }
}

int main() {
    char str[81];
    fgets(str, sizeof(str), stdin);

    int offset;
    scanf("%d", &offset);

    // 处理偏移量大于等于26或小于等于-26的情况
    offset = offset % 26;

    caesarCipher(str, offset);

    printf("%s", str);

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTg0Njc3Nzc3LDE3MjU1OTY4MzcsNzQwMz
k0Mjc1XX0=
-->