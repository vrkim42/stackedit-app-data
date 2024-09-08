## class
```
class Animal:
	def __init__(self, color, legs):#the first parament must be self
		self.color = color
		self.legs = legs

class Cat(Animal): # inherit
	def bark(self):
		print("Woof!")
		
class Dog(Cat):
	def bark(self):
		print("woof!woof!")#the same function will be replaced by the latter
		super().bark()#but you can use the previous function in this way
		
felix = Cat("yellow", 4) #after inheriting,you need also give the paraments `Animals` needs
rover = Cat("green", 4) #actually, we can name a new typement like this.
felix.bark()
dog1 = Dog("red", 3)
dog1.bark()


# magic method
class MyClass:
	def __init__(self, value):
		self.value = value

	def __add__(self, other):
		return MyClass(self.value + other.value)

a = MyClass(10)
b = MyClass(20)
c = a + b  # 调用 __add__ 方法,it will be run autoly without usual call

def add(x, y):# against usual function
	return x + y

result = add(10, 20)
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc4Mzc0NTM3MF19
-->