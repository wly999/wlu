# '''print("nihao")#字符串
# print(111)
# print(True)
# print({})

# print(444.11)
# print("哈哈哈",2222)
# print(111,{})
# print("haha"+"xoxo")
# print("ww"*100)
# print({}+[])
# print(((1+2)*10-12)/2)
# print(2>3)
# name="zhangsan"
# print(name)
# '''
# # a = input("请输入：")
# # print("input获取的值:",a)
# # print(type("haha"))
# # print(type(2.33))
# # print(type({}))
# # a=float(input("请输入："))
# # b=float(input("请输入："))
# # print("input获取的值:",a+b)
# # a="KKHOJHI ojkojk"
# # print(len(a))
# # """练习：通过代码获取2段不同的代码的内容，并计算他们长度的值"""
# # a = input("请输入:")
# # b = input("请输入:")
# # print("字数",len(a)+len(b))



# # #元组,下标从0开始编号
# # a =(1,2,3,"hahah","hahah","hehe",True,False)#元组可以装任何类型
# # print(a[0:3])#输出123
# # print(a[6:7])#输出True
# # print(a[:])#输出所有数值
# # # 切片，左闭右开

# # # 查找下标
# # print(a.count())
# # 二维元组
# # a =(1,2,3,"hahah","hahah","hehe",True,False)#元组可以装任何类型
# # b=(a,"haha","xixi")
# # print(b[0][1])
# #数组
# # a=[1,2,3,"hahah","hahah","hehe",True,False]
# # a.clear()
# # a.append(7)
# #
# # a.append(55)
# # a.insert(1,66)#在第一个数值前插入
# # b=a.pop(0)#剪切
# # c=a.pop(0)#剪切
# # print(b+c)
# # print(a)
# # print(b)
# #xx=[55.48]
# # a.extend(xx)
# # a=[4,5,3,"hahah","hahah","hehe",True,False]
# # b=a.remove(1)

# # print(a)
# # # print(b)
# # xx=[0,True,1,False]
# # c=xx.count(0)
# # d=xx.index(True)
# # print(c)
# # print(d)
# #字典
# from sys import pycache_prefix


a={"name":"zhangsan","age":12}
# print(a["name"])
# a["heigh"]="183cm"

# a["name"]="李四"

# # b=a.pop("name")
# # print(b)
# # print(a)
# a.update(name=11)
# print(a)
# # del a["name"]
# a=[1,2,3]
# del a[0]
# print(a)
# print("---------")
# print(a.get("name1"))
# print(a["name1"])



#获取用户输入的个人信息，并存储到字典中；姓名，年龄，性别