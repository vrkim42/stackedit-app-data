```c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char** argv){
    puts("stdio.h部分。");
    int n = 0;
    char str[100] = "123";
    sscanf(str, "%d", &n);
    printf("%d\n", n);//上面的sscanf() 写法的作用是把字符数组str 中的内容以"%d" 的格式写到n 中
    
    n = 233;
    sprintf(str, "%d", n);
    printf("%s\n", str);//而sprintf() 写法的作用是把n 以"%d" 的格式写到str 字符数组中（还是从右至左）
    
    double db;
    int n1;
    char str3[100] = "2048:3.14,hello", str2[100];
    sscanf(str3, "%d:%lf,%s",&n1, &db, str2);//使用sscanf() 将字符数组str 中的内容按"%d:%lf,%s"的格式写到int 型变量n、double 型变量db、char型数组str2中
    printf("n1 = %d, db = %lf, str2 = %s\n", n1, db, str2);
    
    sprintf(str, "%d:%.2f,%s", n, db, str2);
    printf("str = %s\n", str);//s系列对字符串操作特化，sp读取到数组，sc读取到个体变量。
    
    puts("请输入字符串：");
    gets(str);
    puts(str);
    
    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE2OTk4OTk5NV19
-->