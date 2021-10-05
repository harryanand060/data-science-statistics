# -*- coding: utf-8 -*-
# @Time    : 8/18/2021 2:02 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : collins.py
# @Software: PyCharm
n = 9


# p=[0,1,1,2,3,5,8,13,21]
def fibonacci(n):
    n1, n2 = 0, 1
    count = 0
    if n <= 0:
        print("Print Positive No")
        return

    if n == 1:
        print(n1)
        return

    while count < n:
        if (count == n - 1):
            print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


def bold_text(fun):
    def inner():
        fun()
        print('bold text')

    return inner


# @bold_text
# def text():
#     print("hello")


# name= validation(name=)
# select * from where name=ar1 and

a = [1, [2, 3, [4, 5, [6, 7, 8]], 9]]

b = []
def flatten_list(arr):
    for row in arr:
        if isinstance(row, list):
            flatten_list(row)
        else:
            b.append(row)

flatten_list(a)
print(b)


class A:
    def __init__(self):
        print('init A')

    def funA(self):
        print('in func A')


class B:
    def __init__(self):
        print('init B')

    def funB(self):
        print('in func B')
        self.funA()


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print('init C')

    def funC(self):
        print('in func C')
        self.funB()

    def funA(self):
        print('in func CA')


# c = C()
# c.funC()

# fibonacci(9)
