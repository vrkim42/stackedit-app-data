# C++ 数据结构和操作速查表

## 字符串操作

- 获取长度: `length()` 或 `size()` (返回无符号整数)
- 替换: `.replace(起始位置, 长度, 要替换的内容)`
- 拼接: 使用 `+` 或 `.append("要添加内容")` (可连续使用)
- 查找: `.find(要查找的字符串)` (返回下标,从0开始)
- 提取: `.substr(开始位置, 长度)` (开始位置从0开始)
- 比较: `str1.compare(str2)` (0相等, <0则str1小于str2, >0则str1大于str2)

## 输入和输出

### scanf 和 printf
- 读取格式化输入: `scanf("%c:%c", &a, &b);`
- 注意: 使用%s读取时,遇到空格或回车会停止

### cin 和 cout
- `cin` 读取到空格或回车时停止
- 读取整行: `getline(cin, s)`
- 格式化输出: `cout << fixed << setprecision(3) << a;`
- 条件输出: `cout << a << " \n"[i == n];`

### 取消同步流
```cpp
ios::sync_with_stdio(0), cin.tie(0), cout.tie(0);
```

## 常用函数

- 大小写判断: `islower()`, `isupper()`
- 大小写转换: `tolower()`, `toupper()`
- 二分查找: `lower_bound()`, `upper_bound()` (要求数组非降序)

## 排序
```cpp
sort(v.begin(), v.end(), [](const int &u, const int &v) { return u > v; });
```

## 容器

### vector (动态数组)
- 创建: `vector<int> numbers;`
- 添加: `push_back()`
- 遍历: `for (const auto& number : numbers)`
- 排序: `sort(numbers.begin(), numbers.end())`
- 去重: `numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());`
- 插入: `insert()`
- 其他: `empty()`, `clear()`, `size()`

### set (有序集合,不允许重复)
- 操作: `insert()`, `erase()`, `find()`, `lower_bound()`, `upper_bound()`
- 其他: `size()`, `empty()`, `clear()`, `begin()`, `end()`, `rbegin()`, `rend()`, `swap()`
- 降序set: `set<int, greater<int>> mySet;`

### multiset (允许重复的有序集合)
- 操作同set
- 删除单个元素: `st.erase(st.find(value))`

### unordered_set (无序集合)
- 主要操作: `insert()`, `erase()`, `find()`, `size()`, `count()`

### stack (栈,先入后出)
- 操作: `push()`, `pop()`, `top()`, `empty()`, `size()`

### queue (队列,先入先出)
- 操作: `push()`, `pop()`, `front()`, `back()`, `empty()`, `size()`

### priority_queue (优先队列)
- 操作: `push()`, `pop()`, `top()`, `empty()`, `size()`
- 小顶堆: `priority_queue<int, vector<int>, greater<int>> pq;`

### deque (双端队列)
- 操作: `push_back()`, `push_front()`, `pop_back()`, `pop_front()`
- 访问: `front()`, `back()`
- 其他: `empty()`, `size()`, `clear()`, `insert()`, `erase()`

### pair (对组)
- 创建: `pair<int, int> p1 = {1, 2};`
- 访问: `p1.first`, `p1.second`

# C++ 数据结构和操作速查表 (更新版)

[原有内容保持不变...]

## 新增内容

### map (关联容器)
- 创建: `map<string, int> myMap;`
- 插入: `myMap["key"] = value;` 或 `myMap.insert({"key", value});`
- 访问: `myMap["key"]`
- 检查: `myMap.count("key")` 或 `myMap.find("key") != myMap.end()`
- 遍历: 
  ```cpp
  for(const auto& pair : myMap) {
      cout << pair.first << ": " << pair.second << endl;
  }
  ```
- 其他操作: `erase()`, `clear()`, `size()`, `empty()`

### unordered_map (哈希表)
- 用法与 map 类似,但内部实现使用哈希表,查找效率更高
- 适用于不需要按键排序的场景

### list (双向链表)
- 创建: `list<int> myList;`
- 操作: `push_back()`, `push_front()`, `pop_back()`, `pop_front()`
- 插入: `insert()`
- 删除: `erase()`
- 其他: `size()`, `empty()`, `clear()`, `sort()`

### 位操作
- 与: `&`
- 或: `|`
- 异或: `^`
- 左移: `<<`
- 右移: `>>`
- 取反: `~`
- 获取最低位的1: `n & (-n)`
- 判断奇偶: `n & 1`

### 常用算法 (需包含 <algorithm>)
- 最大值: `max(a, b)` 或 `*max_element(v.begin(), v.end())`
- 最小值: `min(a, b)` 或 `*min_element(v.begin(), v.end())`
- 交换: `swap(a, b)`
- 反转: `reverse(v.begin(), v.end())`
- 计数: `count(v.begin(), v.end(), value)`
- 查找: `find(v.begin(), v.end(), value)`
- 二分查找: `binary_search(v.begin(), v.end(), value)`
- 排列: `next_permutation(v.begin(), v.end())`

### 随机数生成
```cpp
#include <random>
random_device rd;
mt19937 gen(rd());
uniform_int_distribution<> dis(1, 6);
int random_number = dis(gen);
```

### 时间复杂度
- O(1): 常数时间
- O(log n): 对数时间,如二分查找
- O(n): 线性时间,如遍历数组
- O(n log n): 如快速排序、归并排序
- O(n^2): 如简单的嵌套循环
- O(2^n): 指数时间,如递归斐波那契

注意: 在实际应用中,根据具体问题选择合适的数据结构和算法至关重要。

![输入图片说明](/imgs/2024-11-03/pQxsDjeDwD6pF3tg.png)


一般情况下使用`vector`
双端操作频繁使用`deque`
最值操作使用`priority_queue`
FIFO 使用`queue`


<!--stackedit_data:
eyJoaXN0b3J5IjpbLTcwMjQzOTMzMCwtMTQ4NTI5OTE0NiwxNT
A4NjcyOTk0XX0=
-->