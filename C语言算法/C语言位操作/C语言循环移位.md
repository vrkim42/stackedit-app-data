## C语言循环移位
逻辑很简单重点在代码实现，就是移位检查最后一位数的情况，是1就xian'yi'wei
```c
#include <stdio.h>

int main() {
    unsigned int a, b;
    int n, i; // 要转化掉的数，循环几位。
    scanf("%u%d", &a, &n);
    if (n >= 32) return -1; // 确保 n 不超过 32 位

    // 初始化 b 为 0
    b = 0;

    // 将 a 的最高 n 位设置为 1
    for (i = 0; i < n; i++) {
        b = b << 1; // 向左移动 b，为最高位腾出空间
        if (a & 1) { // 如果 a 的最低位是 1，则将 b 的最高位设置为 1
            b = b | 0x80000000;
        }
        a = a >> 1; // 移除 a 的最低位
    }

    // 输出 b 的值
    printf("%u\n", b);

    return 0;
}
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTI2NDMzMDkyMF19
-->