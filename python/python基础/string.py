姓名 = "Charlie_James"
str = '123456789'
# 输出字符串
print(str)
# 输出第一个到倒数第二个的所有字符
print(str[:-1])
# 输出字符串第一个字符
print(str[0])
# 输出从第三个开始到第六个的字符（不包含）
print(str[2:5])
# 输出从第三个开始后的所有字符
print(str[2:])
# 输出从第二个开始到第五个且每隔一个的字符（步长为2）
print(str[1:5:2])
# 输出字符串两次
print(str*2)
# 连接字符串
print(str+str)
print(str + " is a string")
print('str\nstr') # 转义字符
print(r'str\nstr') # 原始字符串,不会发生转义

print("\n" + "="*50)
print("Python字符串知识点补充")
print("="*50)

# 1. 字符串格式化
print("\n1. 字符串格式化:")
name = "Alice"
age = 25
# % 格式化（旧式）
print("姓名：%s，年龄：%d" % (name, age))
# .format() 方法
print("姓名：{}，年龄：{}".format(name, age))
print("姓名：{0}，年龄：{1}".format(name, age))
print("姓名：{name}，年龄：{age}".format(name=name, age=age))
# f-string（推荐，Python 3.6+）
print(f"姓名：{name}，年龄：{age}")
print(f"姓名：{name}，年龄：{age}，明年：{age + 1}岁")

# 2. 字符串方法
print("\n2. 常用字符串方法:")
test_str = "  Hello World Python  "
print(f"原字符串: '{test_str}'")
print(f"去除空格: '{test_str.strip()}'")
print(f"转大写: '{test_str.upper()}'")
print(f"转小写: '{test_str.lower()}'")
print(f"首字母大写: '{test_str.capitalize()}'")
print(f"标题格式: '{test_str.title()}'")
print(f"替换: '{test_str.replace('World', 'Python')}'")
print(f"分割: {test_str.split()}")
print(f"查找位置: {test_str.find('World')}")
print(f"是否以Hello开头: {test_str.strip().startswith('Hello')}")
print(f"是否以Python结尾: {test_str.strip().endswith('Python')}")

# 3. 字符串判断方法
print("\n3. 字符串判断方法:")
test_cases = ["123", "abc", "ABC", "123abc", "  ", ""]
for case in test_cases:
    print(f"'{case}': 数字={case.isdigit()}, 字母={case.isalpha()}, 字母数字={case.isalnum()}, 空格={case.isspace()}")

# 4. 字符串拼接和连接
print("\n4. 字符串拼接和连接:")
words = ["Python", "是", "很棒的", "编程语言"]
print("用空格连接:", " ".join(words))
print("用-连接:", "-".join(words))
print("用空字符串连接:", "".join(words))

# 5. 多行字符串
print("\n5. 多行字符串:")
multi_line1 = """这是一个
多行字符串
可以包含换行"""
print("三引号多行字符串:")
print(multi_line1)

multi_line2 = "这是使用\n" \
              "反斜杠连接的\n" \
              "多行字符串"
print("\n反斜杠连接:")
print(multi_line2)

# 6. 字符串编码
print("\n6. 字符串编码:")
chinese_str = "你好世界"
print(f"中文字符串: {chinese_str}")
print(f"UTF-8编码: {chinese_str.encode('utf-8')}")
print(f"字符串长度: {len(chinese_str)}")
print(f"字节长度: {len(chinese_str.encode('utf-8'))}")

# 7. 字符串比较
print("\n7. 字符串比较:")
str1, str2 = "apple", "banana"
print(f"'{str1}' == '{str2}': {str1 == str2}")
print(f"'{str1}' < '{str2}': {str1 < str2}")  # 字典序比较
print(f"'{str1}' > '{str2}': {str1 > str2}")

# 8. 转义字符大全
print("\n8. 转义字符:")
print("换行: \\n ->", repr("line1\nline2"))
print("制表符: \\t ->", repr("col1\tcol2"))
print("回车: \\r ->", repr("abc\rdef"))
print("反斜杠: \\\\ ->", repr("path\\to\\file"))
print("单引号: \\' ->", repr("it\'s"))
print("双引号: \\\" ->", repr("say \"hello\""))

# 9. 字符串切片进阶
print("\n9. 字符串切片进阶:")
s = "0123456789"
print(f"原字符串: {s}")
print(f"反转字符串: {s[::-1]}")
print(f"每两个字符: {s[::2]}")
print(f"倒数第三个到倒数第一个: {s[-3:-1]}")
print(f"从倒数第五个开始反向每两个: {s[-5::-2]}")

# 10. 字符串格式化进阶
print("\n10. 字符串格式化进阶:")
pi = 3.14159
print(f"π保留2位小数: {pi:.2f}")
print(f"π保留4位小数: {pi:.4f}")
print(f"右对齐10位: '{pi:>10.2f}'")
print(f"左对齐10位: '{pi:<10.2f}'")
print(f"居中10位: '{pi:^10.2f}'")
print(f"用0填充: '{pi:010.2f}'")

num = 42
print(f"二进制: {num:b}")
print(f"八进制: {num:o}")
print(f"十六进制: {num:x}")
print(f"十六进制(大写): {num:X}")

# 11. 字符串和列表转换
print("\n11. 字符串和列表转换:")
text = "Hello,World,Python"
word_list = text.split(",")
print(f"分割成列表: {word_list}")
print(f"重新连接: {','.join(word_list)}")

# 字符串转字符列表
char_list = list(text)
print(f"字符列表: {char_list[:10]}...")  # 只显示前10个

# 12. 字符串内存和性能
print("\n12. 字符串内存特性:")
a = "hello"
b = "hello"
print(f"a is b: {a is b}")  # 小字符串可能被缓存
print(f"id(a): {id(a)}, id(b): {id(b)}")

# 13. 常见字符串操作技巧
print("\n13. 实用技巧:")
# 移除字符串中的空格
messy_str = "  h e l l o  w o r l d  "
print(f"移除所有空格: {''.join(messy_str.split())}")

# 检查回文
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(f"'A man a plan a canal Panama'是回文: {is_palindrome('A man a plan a canal Panama')}")

# 统计字符频率
text = "hello world"
char_count = {}
for char in text:
    char_count[char] = char_count.get(char, 0) + 1
print(f"字符频率: {char_count}")

print("\n" + "="*50)
print("字符串知识点补充完成")
print("="*50)