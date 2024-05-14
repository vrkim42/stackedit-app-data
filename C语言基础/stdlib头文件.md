```c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    puts("stdlib部分。");
    puts("为arr分配内存。");
    int test, i = 0;
    
    
    //malloc构造动态数组
    printf("输入test大小：\n");
    scanf("%d",&test);
    int* arr  = (int *) malloc (sizeof(int) * test);
    for(i = 0; i < test; i++){
        printf("请输入底%d个数：",i);
        scanf("%d", &arr[i]);
    }
    
    
    //malloc函数动态分配大小
    puts("为ptr分配内存。");
    int* ptr = (int*) malloc (5 * sizeof(int));//为ptr分配五个整数的大小。
    if(ptr == NULL){
        puts("内存分配失败。");
        exit(1);
    }
    for(i = 0; i < 5; i++){
        printf("请输入底%d个数：",i);
        scanf("%d", &arr[i]);
    }
    
    
    //calloc函数
    //calloc() 函数用于动态分配内存空间并将其初始化为零。它接受两个参数：
    //分配的元素数量和每个元素的大小（以字节为单位），并返回一个指向分配的内存空间的指针。如果内存分配失败，则返回空指针。
    int *ptr2;
    ptr2 = (int *)calloc(5, sizeof(int)); // 分配包含 5 个整数的内存空间，并将其初始化为零
    if (ptr2 == NULL) {
        printf("内存分配失败\n");
        exit(1); // 退出程序
    }
    // 使用分配的内存空间
    for (int i = 0; i < 5; i++) {
        printf("%d\n", ptr2[i]); // 输出为 0
    }
    // 释放内存空间
    


    
    //realloc函数。
    /*realloc() 函数用于重新分配之前分配的内存空间的大小，可以增大或缩小。它接受两个参数：
    一个是指向之前分配的内存空间的指针，另一个是重新分配的大小（以字节为单位）。如果分配成功，则返回一个指向新内存空间的指针，并释放之前分配的内存空间。
    如果分配失败，则返回空指针，原始内存空间仍然保持不变。*/
    
    ptr = (int *)realloc(ptr, 10 * sizeof(int));//重新分配ptr的内存到十个整形大小
    if (ptr == NULL) {
        printf("内存重新分配失败\n");
        exit(1); // 退出程序
    }
    // 输出重新分配后的内存空间中的值
    printf("\n");
    for (int i = 0; i < 10; i++) {
        printf("%d ", ptr[i]); // 输出为 0
    }
    
    //rand函数
    /*当你需要生成特定范围内的随机数时，你可以使用 rand() 函数。下面是一个示例，演示如何生成介于 min 和 max（包括 min 和 max）之间的随机整数：*/
    int min = 10;
    int max = 20;
    
    // 生成介于 min 和 max 之间的随机数
    int random_number = min + rand() % (max - min + 1);

    // 打印生成的随机数
    printf("生成的随机数：%d\n", random_number);

    free(ptr2);
    free(arr);
    free(ptr);
    return 0;
}
```
`calloc` 和 `malloc` 都是 C 语言中用于动态内存分配的函数，它们在 `<stdlib.h>` 头文件中定义。尽管它们都用于分配内存，但它们之间有一些关键的区别：
1. **目的**:
   - `malloc`（Memory ALLOCation）用于分配指定大小的内存块，但不初始化分配的内存。分配的内存中的数据是未定义的，可能是任意的垃圾值。
   - `calloc`（CONTIGUOUS allocation）用于分配指定数量的元素，每个元素具有指定的大小，并且会初始化所有分配的内存为0。
2. **参数**:
   - `malloc` 接受一个参数，即要分配的内存字节数：
     ```c
     void *malloc(size_t size);
     ```
   - `calloc` 接受两个参数，分别是元素的数量和每个元素的大小：
     ```c
     void *calloc(size_t num, size_t size);
     ```
3. **内存初始化**:
   - `malloc` 分配的内存不进行初始化，因此新分配的内存中可能包含随机数据。
   - `calloc` 分配的内存会自动初始化为0，这意味着如果你分配一个整数数组，所有元素都会被设置为0。
4. **性能**:
   - `malloc` 通常比 `calloc` 快，因为它不需要初始化内存。
   - `calloc` 需要初始化内存，因此在分配大量内存时可能会比 `malloc` 慢。
5. **返回值**:
   - 两者都返回一个指向分配的内存的指针，如果分配失败，则返回 `NULL`。
6. **重分配**:
   - `malloc` 分配的内存可以通过 `realloc` 函数重新分配，而 `calloc` 分配的内存也可以通过 `realloc` 重新分配，但是通常使用 `calloc` 来分配数组，而 `malloc` 用于其他类型的内存分配。
在实际使用中，选择 `malloc` 还是 `calloc` 取决于你的具体需求。如果你需要初始化内存，或者你在分配数组时希望所有元素都是0，那么 `calloc` 是更好的选择。如果你不关心内存中的初始值，或者你需要最大程度的性能，那么 `malloc` 可能是更好的选择。
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTEwOTExNzU3NzAsMTY0NDI1NTU4NV19
-->