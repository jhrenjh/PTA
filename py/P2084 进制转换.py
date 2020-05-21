#!/usr/bin/python
def wrapper(func):
    def inner():
        return next(func)
    return inner
input = wrapper(open('data.in'))
#----------------以上语句，用于重定向输入，提交前需注释掉-------------------
s=input().split()
print(s)
# a=int(s[0])
# l=len(s[1])
# b=s[1].split()
# c=[]
# for i in range(l):
#     c.append(b[i]+"*"+a+"^"+(l-1-i))

# print(c)
