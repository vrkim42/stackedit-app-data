1. 对于一组**首尾相同**的字符串，如`pth`,`ph`,`ptrh`,`prrrh`.可以使用 p[t|tr|rrr]?h 进行替换。
2. 对于末尾多次重复时，如`py`,`pyy`,`pyyy`,可以使用`py+`进行替换。
3. 用`py`(举例)开头，且后续不存在 `p`,`y`，内容不多于十个字母，可以使用
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTgzMDY5NTM0N119
-->