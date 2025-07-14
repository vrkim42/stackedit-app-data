x = 'a'
y = 'b'
print(x)
print(x, end=' ') # 不换行输出

print('''
静夜思
李白
床前明月光,
疑是地上霜。
举头望明月,
低头思故乡。
''')

userName=input('请输入你的姓名:')
age=int(input('请输入你的年龄:'))
sal=float(input('请输入你的薪资:'))
print('姓名是%s,年龄是%d,薪资是%f'%(userName,age,sal))
print(f'姓名{userName},年龄{age},薪资{sal:.2f}')  # 使用f-string格式化输出
print('姓名{1},年龄{0},薪资{2:.2f}'.format(age, userName, sal))  # 使用format方法格式化输出

