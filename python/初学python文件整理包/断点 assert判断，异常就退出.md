在这段代码中，我们展示了 Python 中的 `assert` 语句的使用。`assert` 语句用于在程序中插入断言，以确保某些条件为真。如果断言条件为假，程序将引发 `AssertionError` 异常并停止执行。下面是对代码的详细解释：

### 使用 `assert` 语句

```python
# assert 1 + 1 == 3
# print(3)  # 如果 assert 后面的条件为假，程序将停止并输出 `AssertionError`
```

在这段代码中，我们使用 `assert` 语句来断言 `1 + 1 == 3`。由于这个条件为假，程序将引发 `AssertionError` 异常并停止执行。因此，`print(3)` 这行代码不会被执行。

### 带参数的 `assert` 语句

```python
# 你可以给 assert 添加一个参数，如 `assert (temp >= 0), "在0以下！"`
# 期望的输出是 `AssertionError: 在0以下！`
```

在这段代码中，我们展示了如何给 `assert` 语句添加一个参数，以便在断言条件为假时输出自定义的错误消息。

- `assert (temp >= 0), "在0以下！"`：断言 `temp` 大于或等于 0。如果条件为假，程序将引发 `AssertionError` 异常，并输出自定义的错误消息 `在0以下！`。

### 示例代码

```python
temp = -1
assert (temp >= 0), "在0以下！"
print("温度正常")
```

在这段代码中，我们定义了一个变量 `temp`，并使用 `assert` 语句断言 `temp` 大于或等于 0。由于 `temp` 为 -1，断言条件为假，程序将引发 `AssertionError` 异常，并输出自定义的错误消息 `在0以下！`。因此，`print("温度正常")` 这行代码不会被执行。

### 知识点总结

1. **`assert` 语句**：用于在程序中插入断言，以确保某些条件为真。如果断言条件为假，程序将引发 `AssertionError` 异常并停止执行。
2. **带参数的 `assert` 语句**：可以给 `assert` 语句添加一个参数，以便在断言条件为假时输出自定义的错误消息。

希望这些解释对你理解 `assert` 语句的使用有所帮助！
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE1MTQ3OTM5NzVdfQ==
-->