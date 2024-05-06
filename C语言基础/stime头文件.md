```c
#include <stdio.h>
#include <time.h>

int main(int argc, char** argv){
    puts("time部分。");
    time_t current_time;
    time(&current_time);
    printf("1970.1.1以后的秒数：Current time: %ld\n", current_time);
    struct tm *local_time = localtime(&current_time);
    printf("local time:%s",asctime(local_time));        
    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbNjYzODQwNDIxXX0=
-->