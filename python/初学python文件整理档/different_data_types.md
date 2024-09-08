## different_data_types
```
# dictionary: the value here once be defined,they can't be changed any more
cars = {"bmw":"blue", "Volve":"red"} # if there is no values,you will get a KeyError
# you can add a new value like this: `cars["sss"] = "brown"`,and change the value like: `cars["bmw"] = "white"
# you can use `print("bmw" in cars)` to judge whether it is in the dictionary "cars".it can be keys and values
# either, you can use this function
print(cars.get("bmw", "there is no 'bmw' here"))# this function will return the willing result and can be operate next. 1.if succeed,you will get the value of "bmw". 2. if you have the second parameter and failed, you will get the parameter you give. 3. if you don't have the second parameter but failed,you will get the word "None".


# lambda: you can define an anonymous function in this way,it's temporary
add = lambda x,y:x + y
print(add(2, 3)) #the output value is 5


# tuple: use ()
# once be defined,can't be change


# list section
squres = [1, 4, 9, 16, 25, 36, 49, 64, 81]
# negative values will be settled from the end
print(squres(:7)) # output the first one to the eighth value
print(squres(7:)) # output the eighth value to the last
print(squres(2:4)) # output the third value to the fifth one,has `4-2` values
print(squres(::2)) # output the value from the first to the end,every `2` values will be output,there is one element in the middle will be missed
print(squres(2,8,2)) # output the value from the third value to the nineth value, every `2` values will be output
print(squres(8,2,-1)) # output the value from the ninth to the third one
print(squres(::-1)) # inversion list
```
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTExMjM2NjU5ODldfQ==
-->