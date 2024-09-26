def is_even(x):
 	if x == 0:
 		return True
 	else:
	    return is_odd(x-1)
 
def is_odd(x):
	return not is_even(x)
 
print(is_odd(17)) # the final output is True
print(is_even(23))  # the final output is False


python递归过程判断
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTY4MDAyNzU5XX0=
-->