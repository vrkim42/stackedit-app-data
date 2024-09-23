### recursion 递归

	recursion的情况
1. base case 基本条件 （什么时候执行代码）
2. recursion case 递归条件（什么时候结束代码）
```python
def pact(n):
	if n == 1:
		return 1
	else:
		return pact(n-1)*n
		
print(pact(4))
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTQ2NzM3NDQ0NCw5MjEyMjUzMzddfQ==
-->