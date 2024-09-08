```
print("Hello World!")
print("\'") # use \ to output the '
#as for python, we usually use True and False for the bool but not true and false
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[2][2]) # python usually be used to discribe 2D net table,because python is short in higher net table.


def shout(word):
	return word + "!"
speak = shout # give the value "shout" to speak,then speak is seen as shout
output = speak("shout") # use the function "shout" to do the next things.
print(output)  # the final result is shout!


# 数据类型问题。string类型的*只支持int类型，+只支持string类型
practice_one = float('220' * int(input("输入一个数: "))) #这个是对的
# practice_one = float('220' + int(input("输入一个数: "))) 报错
# practice_one = float('220' * (input("输入一个数: ")) 报错


# .append(value) add a new thing to the end, .index(value) find the position of this value
# .insert(position, value) this new value will be add to the position we provided
# len(tuple) return the length of this tuple
# range(value) = [0 ~ value-1], range(value1, value2) = [value1 ~ value2-1],as for the length of it is value2 - value1
# range(value1, value2, value3) = [value1, value1+value3,..., value2-value3]
# you can try something for `value` times by using `for i in range(value):` to make a loop to finish it
# you can build your own function by using `def function_name(parameter):` and use a table to continue your function

# as for module you can use `import math` to use the API from math
# and you can use `from math import PI`to use the function PI from math
# but if you import unknown function you will get `ImportError`
# you can use as to rename the function you have imported `from math import sqrt as sqrt_root`,but when you use the original name you will get `An error occurs`
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE2OTkxNjQ0MzddfQ==
-->