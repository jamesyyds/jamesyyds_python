# -*-coding: Utf-8 -*-
# @File : 03八大基本数据类型 .py
# author: Chimengmeng
# blog_url : https://www.cnblogs.com/dream-ze/
# Time：2024/7/16

# 【一】基本数据类型引入
# 【1】学习变量的目的
# ● 学习变量有助于我们在程序中存储和操作数据，提高代码的灵活性和可维护性。
# ● 通过使用变量，我们可以方便地引用和修改数据，使得程序能够动态地响应不同的输入和条件。
# 【2】学习基本数据类型的目的
# ● 学习基本数据类型有助于我们理解不同类型的数据在计算机中的表示和操作方式。
# ● 不同的数据类型适用于不同的场景，了解它们的特性有助于我们编写更加高效和健壮的代码。
# 【3】基本数据类型介绍
# ● 数字类型
#   ○ 整数类型(int)
#   ○ 浮点类型(float)
# ● 字符串类型(str)
# ● 列表类型(list)
# ● 字典类型(dict)
# ● 布尔类型(bool)
# ● 元祖类型(tuple)
# ● 集合类型(set)

# 【二】数字类型
# 整数或者浮点数 (小数)
# 【1】整数类型
# 整数类型用于表示整数，是一种基本的数字类型，广泛用于表示计数、索引等整数值。
# 语法 ：变量名 = 整数值
age = 18  # integer
print(type(age))  # <class 'int'>
# 语法：：做算数运算
print(1 + 1)
print(2 > 1)

# 【2】浮点数类型
# 浮点类型用于表示带有小数部分的数值，适用于需要更精确表示的情况。
# 语法：变量名 = 浮点数值(小数值)
salary = 100.23
print(type(salary))  # <class 'float'>

# 【二】字符串类型
# 字符串类型用于表示文本信息，是一种非常重要的数据类型，用于处理文字、字符等信息
name = "dream"
print(type(name))  # <class 'str'>
# 语法：
# 1. 单引号包裹起来的字符
# 2. 双引号包裹起来的字符
# 3. 三个单引号包裹起来的字符
# 4. 三个双引号包裹起来的字符
name_1 = "dream"
print(name_1, type(name_1))
name_2 = 'dream'
print(name_2, type(name_2))
name_3 = '''dream'''
print(name_3, type(name_3))
name_4 = """dream"""
print(name_4, type(name_4))

# 引号嵌套
name_5 = "my name is dream , i hope your life is wonderful"
name_5 = 'my name is dream , i hope your life is wonderful'
# 左边的单引号和右侧单引号被切合开了
# name_5 = 'my name is dream , i hope your life is 'wonderful''
name_5 = 'my name is dream , i hope your life is "wonderful"'
name_5 = "my name is dream , i hope your life is 'wonderful'"
print(name_5)

name_6 = '''
1
2
3
4
'''
print(name_6)

# 补充：字符串的使用方法
# 数字进行乘法 ---> 数字相乘得到乘法的结果
print(2 * 2)  # 4
# 字符串 * 数字 ---> 当前字符串被重复出现指定次数
print("d" * 5)  # ddddd

# 数字进行加法---> 得到加法的结果
print(1 + 1)  # 2
# 字符串 + 数字 ---> 不行 因为类型不一样无法运算
# 字符串 + 字符串 ----> 将两个字符拼接到一起
print("d" + '1')  # d1

# 索引取值
# 正向索引取值 ，索引下表从 0 开始
#  dream
# d r e a m
# 0 1 2 3 4
print('dream'[0])  # d
print('dream'[1])  # r
# 负向索引取值 ， 索引下表就从 -1
# d r e a m
# -5 -4 -3 -2 -1
print("dream"[-1])  # m

# 【4】字符串的格式话输出语法
sentence_one = "my name is dream ,my age is 18 "
sentence_two = "my name is hope ,my age is 28 "
sentence_three = "my name is opp ,my age is 38 "
# 不断地修改同一快代码 为了方便于是就有了格式化输出语法
# （1）方案一 %s 站位
sentence_four = "my name is %s ,my age is %s"
print(sentence_four % ("dream", 18))
print(sentence_four % ("hope", 28))

# ● 在上例中，%s 和 %d 是占位符，分别表示字符串和整数，而 (name, age) 是传入这两个占位符的实际值。
# ● 占位符类型
#   ○ %s：字符串
#   ○ %d：整数
#   ○ %f：浮点数
#   ○ %x：十六进制整数

# （2）format方法输出 : 用 {} 站位
sentence = "my name is {} ,my age is {}"
print(sentence.format("dream", "18"))
# format 按照 {} 位置传参数的时候如果位置替换就会导致替换错乱
print(sentence.format(18, "dream_format"))

# 可以用关键字占据指定位置 {name} 站位 在传递参数的时候要按照关键字传参数
sentence = "my name is {name} ,my age is {age}"
print(sentence.format(name="dream", age="18"))
# 在上面定义字符串的时候 用 {变量名} 占位置 在传递参数的时候按照关键字=值的方式传入参数
print(sentence.format(age="18", name="dream"))

# （3）方案三：f"{name}"

name = "dream_f"
age = "18"
sentence = f"my name is {name} , my age is {age} "
print(sentence)
