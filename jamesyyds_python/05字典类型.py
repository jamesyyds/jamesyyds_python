# -*-coding: Utf-8 -*-
# @File : 05字典类型 .py
# author: Chimengmeng
# blog_url : https://www.cnblogs.com/dream-ze/
# Time：2024/7/16

# 列表中可以存储多个属性类型相同的值
# 存储多个人的名字 ， 年龄

# 当我的年龄和名字混到一起的时候，就分不清谁知年龄谁是名字
name = "dream"
age = 18

# ● 如果我们需要用一个变量记录多个值，但多个值是不同属性的
#   ○ 比如人的姓名、年龄、身高，用列表可以存，但列表是用索引对应值的，而索引不能明确地表示值的含义
# ● 这就用到字典类型，字典类型是用 key：value 形式来存储数据
#   ○ 其中key可以对value有描述性的功能，能够明确的描述详细信息

# 语法 ： {"key":"value"}

person_info = {
    "name": "dream",
    "age": 18,
    "gender": "male"
}

# 存储数据是为了取数据去用
# 方式一： 字典["key"]
print(person_info["name"])
print(person_info["age"])
# 方式二：字典.get("key")
print(person_info.get("gender"))

# 方式一： 字典["key"] 如果字典中没有指定的键就会报错
# print(person_info["hobby"])
# 方式二：字典.get("key") 如果字典中没有指定的键不会报错
print(person_info.get("hobby"))  # None

# 列表和字典 ---> 组合嵌套
info = {
    'name': 'Dream',
    'addr': {
        '国家': '中国',
        'info': [666, 999, {'编号': 466722, 'hobby': ['read', 'study', 'music']}]
    }
}
# 格式化输出：my name is name , my age is age , my 国家 is 国家 , my 编号 is 编号
# hobby : my hobby is read , study and music
