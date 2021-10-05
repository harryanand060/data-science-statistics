# -*- coding: utf-8 -*-
# @Time    : 8/12/2021 4:01 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : test4.py
# @Software: PyCharm


# def foo(x=[]):
#     x.append(1)
#     return x
#
#
# print(foo())
# print(foo())

# magic method

# p=["a","n","a","n","d"]
# # monkey patching
#
# c=''.join(p)
# print(ord('a'))
# b = 85
# print(str(b)[1:])
# a = [8, 25, 65, 21, 84]
#
# count = ""
# for i in a:
#     count += str(i)[-1]
#
# print(count)
# if int(count) % 10==0:
#     print("Yes")
# else:
#     print("NO")

s1 = "anand"
s2 = "sonali"
x = 18
#
# def test():
#     n = len(s1)
#     arr1 = list(s1)
#     arr2 = list(s2)
#
#     for i in range(n):
#         print(f"ORD arr2 {ord(arr2[i])}")
#         print(f"ORD arr1 {ord(arr1[i])}")
#         diff = ord(arr2[i]) - ord(arr1[i])
#         print(f"Diff {diff}")
#         if diff == 0:
#             continue
#
#         if diff < 0:
#             diff +=26
#
#         if diff > x:
#             return False
#         print(f"Diff {diff}")
#     return True

# a1=[1,1,2]
# a2=[1,1]
# a2.remove(1)
# print(a2)

#
# count = 0
# i = 1
# arr = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# # b = arr[i:]
# # b.remove(10)
# # print(b)
# for row in arr:
#     print(f"ARR {arr}")
#     if row in arr[i:]:
#         next = arr[i:]
#         next.remove(row)
#         count += 1
#         arr = next
#     i += 1
# print(count)
#
#
# def check_pair(arr, count, i):
#
#     if row in arr[i:]:
#         arr = arr[i:]
#         arr.remove(row)
#         count += 1
#     i += 1
#     check_pair(arr, count, i)

# print(test())

# from collections import  deque
#
# a=deque([1,2,3])
# # a.append(4)
# # a.appendleft(5)
# # a.pop()
# # a.popleft()
# a.rotate(7)
# print(a)

# a={1:"anand",2:"kumar"}
# a.pop(1)
# print(a)



'''I want you to create a method to increment a number. The number can be any number, 
but it will be given as an array of digits. The output also should be an array, which is the number incremented.
 I want to see array handling logic, so don’t do x*100 + y*10 - or converting to string (and then to number) etc
Example Output:'''

# def incr([2,3,4]) =>as good as incr(234) => 235 => [2,3,5]
# def incr([3,4,2,5]) =>as good as incr(3425) => Result: 3426 => [3,4,2,6]




def incr(num):
    number=num[-1]
    # print(number)
    # last_dig = int(num[-1])
    # last_dig += 1
    # num[-1] = str(last_dig)
    # print(num)
    # num +=1
    print(number)


# number=list(input("Please Eneter Number: \n"))
incr(2235)
# print(number)
# number=[2,3,6,8] #2368 2369



# def incr(num)
















