### qsort

	quicksort的思想 － 分而治之
1. base case 基本情况
2. inductive case 归纳情况
```python
def qsort(array):
	if len(array) < 2:
		return array
	else:
		pivot = array[0]
		less = [i for i in array[1:] if i < pivot]
		greater = [i for i in array[1:] if i > pivot]
		return qsort(less) + [pivot] + qsort(greater)
		
print(qsort([10, 3, 4, 5]))
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTk0Njg1OTY4OV19
-->