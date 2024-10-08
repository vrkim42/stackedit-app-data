### 字符串操作
- [ ] 获取**字符串长度**使用length/size()函数，size()返回无符号整数
- [ ] **字符串替换**使用replace函数，.replace(起始位置，长度，要替换的内容)
- [ ] **字符串拼接**使用+或者append函数，使用.append("要添加内容") <- 可以连续多次使用
- [ ] **字符串查找**使用find函数，.find(要查找的字符串)，返回该字符串的下标，下表从零开始
- [ ] **提取字符串**使用substr函数，返回提取到的字符串，.subStr(开始位置，长度)开始位置从0开始
- [ ] **字符串比较大小**使用compare函数,str1.compare(str2)返回一个数，是0相等，小于0 则str1小于str2，大于0 则str1大于str2。

### 输入和输出

#### scanf 和 printf
读取 a:b
`scanf("%c:%c", &a, &b);`
使用%s进行读取时遇到*空格*或者*回车*，读取会**停止**。

#### cin 和 cout
当cin的类型为double但是输入的为整数，cout的时候不会为你转化小数，而是单单输出哪个你输入的整数
除非 `cout << fixed <<setprecision(3) << a << " ";`，这样的话会为你转化出一个三位小数的输出结果。
cin也是遇到空格或者回车时停止输入，对此我们可以使用getline(cin, s)的方法读取一行数据
输出时，可以使用cout << a << " \n"[i == n]进行格式化输出，即当i达到n时，输出"\n"其余时间输出空格。
也可以输出 cout << "0ll" 表示输出的是longlong类型的整数。
### 取消同步流
`ios::sync_with_stdio(0),cin.tie(0),cout.tie(0)`
加速cpp的输入和输出到和c一致

### islower()/isupper()函数
返回一个布尔值，是返回true

### tolower()/toupper()函数
将字符进行大小写转换，不会转换其他字符和空格

### lower_bound()/upper_bound()函数
**数组必须非降序**
返回第一个大于目标数的位置或者第一个小于目标数的地址（一般要减去开始位置得到索引），使用方法是lower_bound(起始位置，终止位置，目标数)

### sort函数的使用
sort(起始地址，终止地址下一位， *排序方式)
`sort(v.begin()，v.end(),[](const int &u,const int &v){return u>v} `
这里使用[]进行匿名函数声明，也可以使用自定义函数，方法类似


### vector向量（动态数组，可扩列）
1. `std::vector<int> numbers;`创建vector对象
2. `push_back`添加元素
3. `for(const auto& number in numbers)`打印元素
4. `sort(numbers.begin(), numbers.end())`排序
5. `numbers.erase(unique(numbers.begin(),numbers.end()),numbers.end());`去除重复元素
6. `numbers.insert(numbers.begin()+2, 3)`插入元素
7. `numbers.empty()`判断是否为空
8. `numbers.clear()`清空向量
9. `numbers.size()`向量大小

### stack（先入先出）
1. push(x) 栈顶插入元素x
2. pop() 弹出栈顶元素
3. top() 返回栈顶元素
4. empty() 检查栈是否为空
5. size() 返回栈中元素个数   
6. `stack<int> myStack`初始化
7. `myStack.empty()` 检查是否为空
8. `myStack.size()` 栈的大小

### set容器 （不允许重复，排序）
1. 
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NDk2MzQ0NzAsNjYyOTA2NTc5LDYzNj
c2NDcyNiw2ODI0NTkyMTMsMTEyNjA4OTMzNCw1ODg1MDEwNjld
fQ==
-->