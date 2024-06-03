
## 简述
strcpy 抄
strcmp 比较
strncmp 比较
strcat 追加
strlen 长度
strchr 查找字符
strstr 查找字符串
strtok 切割
```c
#include <stdio.h>
#include <string.h>

int main() {
    // strcpy()用于将一个字符串复制到另一个字符串中。
    char destination[20];
    char source[] = "Hello, world!";
    strcpy(destination, source);
    printf("复制后的字符串: %s\n", destination);
    
    // strcat()用于将一个字符串追加到另一个字符串的末尾。
    char str1[20] = "Hello";
    char str2[] = " world!";
    strcat(str1, str2);
    printf("追加后的字符串: %s\n", str1);
    
    // strlen()用于获取字符串的长度。
    char str[] = "Hello";
    int length = strlen(str);
    printf("字符串长度: %d\n", length);
    
    // strcmp()用于比较两个字符串。
    char str1_cmp[] = "Hello";
    char str2_cmp[] = "hello";
    int result = strcmp(str1_cmp, str2_cmp);
    if (result == 0) {
        printf("Strings are equal\n");
    } else if (result < 0) {
        printf("String 1 is less than string 2\n");
    } else {
        printf("String 1 is greater than string 2\n");
    }
    
    // strncmp()用于比较两个字符串的前n个字符。
    char str1_n_cmp[] = "Hello";
    char str2_n_cmp[] = "Hell";
    int result_n = strncmp(str1_n_cmp, str2_n_cmp, 4);
    if (result_n == 0) {
        printf("Strings are equal\n");
    } else if (result_n < 0) {
        printf("String 1 is less than string 2\n");
    } else {
        printf("String 1 is greater than string 2\n");
    }
    
    // strchr()用于在字符串中查找指定字符的第一个匹配。
    char str_chr[] = "Hello, world!";
    char *ptr_chr = strchr(str_chr, 'o');
    printf("First occurrence of 'o' is at position: %ld\n", ptr_chr - str_chr + 1);
    
    // strstr()用于在字符串中查找子字符串的第一个匹配。
    char str_str[] = "Hello, world!";
    char *ptr_str = strstr(str_str, "world");
    printf("Substring found at position: %ld\n", ptr_str - str_str + 1);
    
    // strtok()用于将字符串分解为一系列子字符串。
    char str_tok[] = "Hello,world";
    char *token = strtok(str_tok, ",");
    while (token != NULL) {
        printf("%s\n", token);
        token = strtok(NULL, ",");
    }
    
    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY4ODUxOTk3NiwxOTAxNzk4OTQsMzc2OD
U2NjQwLDE5Mzk1NzU5MDhdfQ==
-->