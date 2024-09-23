### recursion 递归

	recursion的情况
1. base case 基本条件
2. recursion case 递归条件
```python
def pact(n):
	if n == 1:
		return 1
	else:
		return pact(n-1)*n
		
print(pact(4))
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTIxMjI1MzM3XX0=
-->