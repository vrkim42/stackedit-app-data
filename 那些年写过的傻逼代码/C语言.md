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
            if (offset > 0) {  // 处理正数偏移量
                if (islower(str[i])) {  // 处理小写字母
                    str[i] = 'a' + (str[i] - 'a' + offset) % 26;
                } else {  // 处理大写字母
                    str[i] = 'A' + (str[i] - 'A' + offset) % 26;
                }
            } else {  // 处理负数偏移量
                if (islower(str[i])) {  // 处理小写字母
                    str[i] = 'a' + (str[i] - 'a' + 26 + offset) % 26;
                } else {  // 处理大写字母
                    str[i] = 'A' + (str[i] - 'A' + 26 + offset) % 26;
                }
            }
        }
    }
}

int main() {
    char str[81];
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0'; // 移除换行符

    int offset;
    scanf("%d", &offset);

    caesarCipher(str, offset);

    printf("%s", str);

    return 0;
}
```

## 4
```c
#include<stdio.h>
#include<string.h>
#include<ctype.h>


int main(){
 char str1[21];
 char str2[21];
 int flag = 0;
 fgets(str1,sizeof(str1),stdin);
 fgets(str2,sizeof(str2),stdin);
 for(int i = 0; i < strlen(str1); i++){
  if(str1[i] == str2[i]){
   flag++;
   continue;
  }
  if(islower(str1[i])){
   str1[i] -= 32;
  }
  if(islower(str2[i])){
   str2[i] -= 32;
  }
  if(str1[i] == str2[i])
   flag++;
 }
 printf("%d", flag);
}
```
youhua
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char str1[21];
    char str2[21];
    int flag = 0;

    fgets(str1, sizeof(str1), stdin);
    fgets(str2, sizeof(str2), stdin);

    for (int i = 0; str1[i] != '\0' && str2[i] != '\0'; i++) {
        char c1 = toupper(str1[i]);  // 将字符转换为大写
        char c2 = toupper(str2[i]);

        if (c1 == c2) {
            flag++;
        }
    }

    printf("%d", flag);
    return 0;
}
```

```c
#include<stdio.h>
#include<string.h>


int main(){
 char str[101];
 fgets(str,sizeof(str),stdin);
 int len = strlen(str) - 1;
 for(int i = 0; i < len; i++){
  for(int j = 0; j < len - i; j++){
   if(str[j] > str[j+1]){
    int temp = str[j];
    str[j] = str[j+1];
    str[j+1] = temp;
   }
  }
 }
 for(int i = 0; i < len - 1; i++){
  if(str[i] != '0'){
   for(int j = i; j < len - 1; j++){
    printf("%c",str[j]);
   }
   break;
  }
 }
 printf("%c", str[len]);
}
```
不仅优化了，还改对了
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// 自定义比较函数，用于qsort排序
int compare(const void *a, const void *b) {
    return (*(char *)a - *(char *)b);
}

int main() {
    char n[101];
    scanf("%s", n);

    // 排序字符串
    qsort(n, strlen(n), sizeof(char), compare);

    // 跳过前导零
    int i = 0;
    while (n[i] == '0') {
        i++;
    }

    // 输出排序后的整数
    if (n[i] != '\0') {
        printf("%s", &n[i]);
    } else { // 处理输入为0的情况
        printf("0");
    }

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTMyOTkyNzA5LDE3MTI3NDI3NDIsLTUyNj
MyMTA0OCwxNzI1NTk2ODM3LDc0MDM5NDI3NV19
-->