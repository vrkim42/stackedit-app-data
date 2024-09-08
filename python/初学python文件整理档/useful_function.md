## useful_function
```
nums = [55, 44, 33, 22, 11]

if all([i > 5 for i in nums]):
	print("All larger than 5")

if any([i % 2 == 0 for i in nums]):
	print("At least one is even")
	
for v in enumerate(nums): # like enum
	print(v) # output `(index, value)`
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE2NjgyMTg2NV19
-->