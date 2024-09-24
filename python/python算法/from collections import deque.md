`deque` 是 Python 的 `collections` 模块中提供的一种数据结构，代表双端队列（double-ended queue）。与普通的列表相比，`deque` 在两端都能高效地进行插入和删除操作，时间复杂度为 O(1)，而列表在头部插入或删除的时间复杂度为 O(n)。

### `deque` 的基本用法

以下是 `deque` 的一些常用方法和操作：

1. **导入 `deque`**：
   ```python
   from collections import deque
   ```

2. **创建 `deque`**：
   ```python
   # 创建一个空的 deque
   d = deque()

   # 创建一个包含初始元素的 deque
   d = deque([1, 2, 3, 4])
   ```

3. **基本操作**：
   - **添加元素**：
     - 在右侧添加元素：
       ```python
       d.append(5)  # d 变为 deque([1, 2, 3, 4, 5])
       ```
     - 在左侧添加元素：
       ```python
       d.appendleft(0)  # d 变为 deque([0, 1, 2, 3, 4, 5])
       ```

   - **删除元素**：
     - 从右侧删除元素：
       ```python
       d.pop()  # 返回并删除 5，d 变为 deque([0, 1, 2, 3, 4])
       ```
     - 从左侧删除元素：
       ```python
       d.popleft()  # 返回并删除 0，d 变为 deque([1, 2, 3, 4])
       ```

4. **访问元素**：
   `deque` 支持通过索引访问元素，与列表类似：
   ```python
   first_element = d[0]  # 访问第一个元素
   ```

5. **旋转**：
   `deque` 提供了旋转的方法，可以将元素向右或向左旋转指定的次数：
   ```python
   d.rotate(1)  # 右旋转 1 位，d 变为 deque([4, 1, 2, 3])
   d.rotate(-1)  # 左旋转 1 位，d 变为 deque([1, 2, 3, 4])
   ```

6. **清空 `deque`**：
   ```python
   d.clear()  # 清空所有元素
   ```

### 例子

下面是一个使用 `deque` 的简单示例，模拟一个任务队列：

```python
from collections import deque

# 创建一个任务队列
task_queue = deque()

# 添加任务
task_queue.append("Task 1")
task_queue.append("Task 2")
task_queue.appendleft("Task 0")  # 在左侧添加任务

print("当前任务队列：", task_queue)

# 处理任务
while task_queue:
    current_task = task_queue.popleft()  # 从左侧处理任务
    print(f"处理 {current_task}")

print("所有任务已处理。")
```

### 总结

`deque` 是一个非常灵活且高效的数据结构，适用于需要频繁在两端添加和删除元素的场景，如任务队列、缓存等。由于其 O(1) 的时间复杂度，它在某些情况下比 Python 的列表更优。若您对 `deque` 的某些特性或应用场景有进一步的问题，请告诉我！
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTA5ODQwNzY0MF19
-->