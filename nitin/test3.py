# -*- coding: utf-8 -*-
# @Time    : 8/12/2021 2:42 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : test3.py
# @Software: PyCharm


a = 1


def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# main function
s = "malayalam"
# str[len(s) - i - 1]:
ans = isPalindrome(s)

if (ans):
    print("Yes")
else:
    print("No")

# def prime_number(a):
#     if a % 2== 0:
#         print(f"{a} is not prime")
#     else:
#         print(f"{a}  is prime")
#
# prime_number(3)
