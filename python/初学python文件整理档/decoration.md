## decoretion
```
def my_decorator(func):
	def wrapper():
		print("Something is happening before the function is called.")
		func()
		print("Something is happening after the function is called.")
	return wrapper

@my_decorator
def say_hello():
	print("Hello!")

say_hello()

##############################

def repeat(num_times):
	def decorator(func):
		def wrapper(*args, **kwargs):
			for _ in range(num_times):
				func(*args, **kwargs)
		return wrapper
	return decorator

@repeat(num_times=3)
def say_hello():
	print("Hello!")

say_hello()
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTM5Mjg4NDczNF19
-->