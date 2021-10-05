# -*- coding: utf-8 -*-
# @Time    : 7/15/2021 11:56 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : multithreading.py
# @Software: PyCharm
from threading import *
import time
import threading
import concurrent.futures

#
# class Hello(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hello")
#             time.sleep(1)
#
#
# class Hi(Thread):
#     def run(self):
#         for i in range(10):
#             print("Hi")
#             time.sleep(1)
#
# start=time.perf_counter()
# t1 = Hello()
# t2 = Hi()
#
# t1.start()
# time.sleep(0.2)
# t2.start()
# t1.join()
# t2.join()
# print("Bye")

start = time.perf_counter()


def test_multithreading(sec, process_count=1):
    print(f"Process {process_count} sleeping {sec} Second...")
    time.sleep(sec)
    print(f"Process {process_count} Done Sleeping...")


# t1 = threading.Thread(target=test_multithreading)
# t2 = threading.Thread(target=test_multithreading)
# thread_list = []
# count = 0
# for _ in range(10):
#     count += 1
#     t1 = threading.Thread(target=test_multithreading, args=[1,count])
#     t1.start()
#     thread_list.append(t1)
#
#
# for thread in thread_list:
#     thread.join()

# t1.start()
# t2.start()
# t1.join()
# t2.join()
# test_multithreading()
# test_multithreading()

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results=[executor.submit(test_multithreading, 1) for _ in range(20)]
        # t1 = executor.submit(test_multithreading, 1)
        # t2 = executor.submit(test_multithreading, 1)
        # t1.result()
        # t2.result()
        for t in concurrent.futures.as_completed(results):
            t.result()


    end = time.perf_counter()
    print(f"Total Elapsed Time : {round(end - start, 2)} Sec")

str()
from collections import ChainMap
#
# d1 = {'a': 1, 'b': 2}
# d2 = {'c': 3, 'd': 4}
# d3 = {'e': 5, 'f': 6}
#
# # Defining the chainmap
# # c = ChainMap(d1, d2, d3)
# #
# # print(type(c))
# anand="anand"
# print(anand[1:])
# anand.lower()
#
# print(d1.keys())

# from collections import OrderedDict
#
# numbers = OrderedDict([("one", 1), ("two", 2), ("three", 3)])
#
# print(numbers)
# print(type(numbers))
# print(isinstance(numbers,OrderedDict))


for i in range(100):
    print(i)



