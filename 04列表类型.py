# -*-coding: Utf-8 -*-
# @File : 04列表类型 .py
# author: Chimengmeng
# blog_url : https://www.cnblogs.com/dream-ze/
# Time：2024/7/16

# 当我们想存储多个人的名字的时候
user_name = "dream | hope | opp"
# 当我想取出某一个人的名字的时候 取不出来

# ● 用来存取多个相同属性的值，并且方便存取
# ● 如果我们需要用一个变量记录多个学生的姓名，用数字类型是无法实现，字符串类型则可以记录下来
user_names = ["dream", "hope", "opp"]

# 取出 dream 这人的名字

# 索引取值
# 正向索引 从 0 开始 从头向后
# 负向索引 从 -1 开始 从尾到头
print(user_names[0])
print(user_names[-3])

data_info = ["dream", "hope", "opp", [
    18, 19, 20, [
        "music", "run", "swim"
    ]
]]

# 打印 my name is name ,my age is age ,my hobby is hobby
print(f"my name is {data_info[0]} ,my age is {data_info[3][0]} ,my hobby is {data_info[3][3][0]}")
