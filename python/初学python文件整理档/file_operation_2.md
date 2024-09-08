## file_operation_2
```
# you can use a function twice by doing this
def apply_twice(func, arg):
	return func(func(arg))
def add_five(x):
	return x+5
print(apply_twice(add_five, 10))

# you can use lambda to name a easy function
a = (lambda x: x*x)(8) # this function you squred the number '8'
# actually, you can do it in the other way
double = lambda x: x*2 and print(double(7))
	
# map
nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums)) # you can operate the whole list easily in this way
print(result)
# you can do it this way
result = list(map(lambda x: x+5,nums))
print(result)

#filter: you can delete the element you actually need with this method
#res = list(filter(lambda x: x%2==0,nums)) and print(res) # the output is [22,44]
	
# generatorsd: it will save all the elements into list
def countdown():
	i = 5
	while i > 0: #after i <= 0,this function will end
		yield i #equivalent to saving a value once per iteration
		i -= 1
		
for i in countdown():
	print(i)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2NzA3NjUyMzNdfQ==
-->