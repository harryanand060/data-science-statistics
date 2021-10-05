# # -*- coding: utf-8 -*-
# # @Time    : 8/11/2021 5:10 PM
# # @Author  : Anand Kumar
# # @Email   : harryanand060@gmail.com
# # @File    : test2.py
# # @Software: PyCharm
#
# # using stack
# # a=[13,7,6,12]
# #
# # out=[-1,12,12,-1]
# #
# # for i in a:
# #
# # c = {}
# # a = [0, 1, 2, 1, 0, 1, 2]
# #
# # out = [0, 0, 1, 1, 1, 2, 2]
# #
# # for i in a:
# #     if i in c.keys():
# #         c[i] += 1
# #     else:
# #         c[i] = 1
# #
# # print(c)
# #
# # new=[]
# #
# # for i in c:
# #     for j in range(c[i]):
# #         new.append(i)
# #
# # print(new)
#
# a = [6, 3, -1, -3, 4, -2, 2,4, 6, -12, -7]
#
# sub = []
# count = 0
# j = 1
# for i in a:
#     val = i
#     for k in a[j:]:
#         val += k
#         if val == 0:
#             count += 1
#     j+=1
#
# print(count)
