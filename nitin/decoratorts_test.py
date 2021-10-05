# -*- coding: utf-8 -*-
# @Time    : 7/10/2021 2:58 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : decoratorts_test.py
# @Software: PyCharm

def test1(name):
    def inner(fun):
        def wrapper(*args):
            # args.append(name)
            fun(*args)
            # print(new_fun.upper())
        return wrapper
    return inner

# a="kumar"
@test1("anand2")
def test2(a,b,c,*args):
    print(a,b,c,args)


test2("anand","kumar","singh")
