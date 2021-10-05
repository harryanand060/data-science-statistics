# # -*- coding: utf-8 -*-
# # @Time    : 8/10/2021 3:11 PM
# # @Author  : Anand Kumar
# # @Email   : harryanand060@gmail.com
# # @File    : linked_list.py
# # @Software: PyCharm
#
#
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
# class LinkedList:
#     def __init__(self):
#         self.head=None
#
#     def insert(self,data):
#         new_node=Node(data)
#         if self.head:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=new_node
#         else:
#             self.head=new_node
#
#     def get_data(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next
# ll=LinkedList()
# ll.insert(1)
# ll.insert(2)
# ll.insert(3)
#
# ll.get_data()


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next_node:
                current = current.next_node
            current.next_node = new_node
        else:
            self.head = new_node

    def get_data(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next_node

ll=LinkedList()
ll.insert(1)
ll.insert(3)
ll.insert(4)

ll.get_data()

class Singalton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(Singalton, cls).__call__(*args, **kwargs)

        return cls._instance[cls]

import  abc
class MyClass(metaclass=Singalton):
    pass
