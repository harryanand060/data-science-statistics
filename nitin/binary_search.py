# -*- coding: utf-8 -*-
# @Time    : 7/7/2021 7:57 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : binary_search.py
# @Software: PyCharm

import math

unsorted_list = [56, 4, 8, 98, 1, 4, 6]
# unsorted_list = [1, 1, 4, 4, 6, 56, 98]
sorted_list = sorted(unsorted_list)
print(sorted_list)
key = 98


# Complexity O(n)
def linear_search():
    for k, val in enumerate(sorted_list):
        if key == val:
            return k


# Complexity O(logn)
def binary_search():
    l = 0
    r = len(sorted_list) - 1
    m = 0
    while r >= l:
        m = (l + r) // 2
        if key > sorted_list[m]:
            l = m + 1
        elif key < sorted_list[m]:
            r = m - 1
        else:
            return m
    return -1


print(linear_search())
