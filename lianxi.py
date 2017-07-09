# 练习测试
# n='0'
# a='3'
# for i in range(1,5):
#      n+=a+str(i)
# print(n)

# 乘法口诀表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(i,'*',j,'=',i*j,'\t',end='')
#     print()

# 逻辑判断练习
# import random
#
# a = ['a','b','c','d']
# a_sub = a[:]
#
# while a:
#         if a_sub:
#                 res = random.choice(a_sub)
#                 print(res)
#                 a_sub.remove(res)
#         else:
#                 a_sub = a_sub+a

# import random
#
# a = ['a','b','c','d']
# a_sub = a[:]
# print(a_sub)
# while a:
#     if a_sub:
#         res = random.choice(a_sub)
#         print(res)
#         a_sub.remove(res)
#     else:
#         a_sub = a

# total = []
# for i in range(1, 5):
#     for j in range(1, 5):
#         for k in range(1, 5):
#             if (i != j) and (i != k) and (j != k):
#                 total.append((i, j, k))
# print(len(total), total)

# list1 = [1, 5, 7, 8, 3]
# list2 = [3, 5, 9, 1, 2]
#
# list3 = list1[:]
# for i in list2:
#     if i in list3:
#         continue
#     else:
#         list3.append(i)
# print(list3)
# list3 = list(set(list1+ list2))
# print(list3)

# province = {
#     "河北": {
#         "石家庄": ["鹿泉", "藁城", "元氏"],
#         "邯郸": ["永年", "涉县", "磁县"],
#     },
#     "湖南": {
#         "长沙":['a','b','c'],
#         "株洲":['d','e','f']
#     },
#     "湖北": {
#         "武汉":['g','h','i'],
#         "黄石":['j','k','l']
#     	}
# }
# print(province['河北'])

import time
import datetime
print(type(datetime.datetime.now()))
print(type(datetime.datetime.now().minute))
print(datetime.datetime.now().second)
#print(hour)

