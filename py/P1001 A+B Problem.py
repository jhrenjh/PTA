#!/usr/bin/python
# def wrapper(func):
#     def inner():
#         return next(func)
#     return inner
# input = wrapper(open('data.in'))
#----------------以上语句，用于重定向输入，提交前需注释掉-------------------
s=input().split()
a=int(s[0])
b=int(s[1])
c=a+b
print(c)
