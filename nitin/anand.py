#
# class Table1(model.Model):
#     name=model.charFiled()
#     name=model.integer()
#     name=model.boolean()
#
#
#
# def get_data(request):
#     if request.Method=="GET":
#         model=Table1(
#         data=model.object.filter(__name__="anand")
#         response(context=data)
#
#
# a = [2, 2, 2, 2, 3, 1, 3, 3, 3, 5, 5, 5, 5, 6, 6, 6]
#
# b = {}
# for i in a:
#     if i in b.keys():
#         b[i] += 1
#     else:
#         b[i] = 1
#
# print(b)
# for j in b:
#     if b[j] == 1:
#         print(j)
# #         break
# a = ["a", "e", "i", "o", "u"]
# # b = [ord(i) for i in a]
#
# c=[]
# def check_vowels(word):
#     count = False
#     list_word = list(word)
#     # print(list_word)
#     for i in a:
#         # print(i)
#         if i in list_word:
#             c.append(True)
#         # else:
#         #     c.append(False)
#     return all(c)
#


# 3
# [2,3,5,6,14]
# def binary_search(ele):
#     a = [14, 3, 2, 5, 6]
#     a.sort()
#     length_arr=len(a)
#     left=0
#     right=length_arr-1
#     mid = length_arr // 2
#
#     while mid < right:
#         mid = length_arr // 2
#         if ele==a[mid]:
#             return mid
#         if ele < a[mid]:
#             right=mid -1
#         if ele > a[mid]:
#             left=mid + 1


# anand aand
# anand anand
# line_count=0
# dict_data={}
# with open("abc.txt","r") as f:
#     for i in f.readline():
#         string_length =len(i.split(" "))
#         line_count +=1
#         dict_data[line_count]=string_length


#
#
# def max_substring(a):
#     list_string=list(a)
#
#     # ele=a[0]
#     count=1
#     max_count=1
#     prev_string=""
#     current_string=""
#     for i in list_string:
#         current_string +=i
#         for j in list_string[count:]:
#             if j in current_string:
#                 if len(current_string) > len(prev_string):
#                     prev_string=current_string
#                     current_string=""
#                 else:
#                     # max_count = 0
#                     current_string = ""
#                 break
#             else:
#                 max_count +=1
#                 current_string +=j
#         count +=1
#
#     print(len(prev_string))
#     print(prev_string)
#     # print(current_string)
#
#
#
# a="abcdabefgagh"
#
# max_substring(a)

# a=1,2,

# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass

import encodings

# a="2130706433W2665427192904"
# c=a.encode()
# print(c)


'''
expnases
total expanses 
and show to user

# '''
#
#
# "url.py"
#
# urlpatterns[
#     path("/api/claculte",views.calculate)
# ]
#
# "view.py"
#
# def calculate(request):
#     if request.method=="POST":
#         food=request.get("food")
#         cloths=request.get("cloth")
#         extra=request.get('extra')
#
#         sum=food+cloths+extra
#         return render(request,"cal.html",data={"total":sum})


import abc


class CAR(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def streeing(self):
        print("parent Streeing")

    @abc.abstractmethod
    def wheel(self):
        print("parent wheel")


class Maruti(CAR):

    def __init__(self):
        super(Maruti, self).__init__()

    def wheel(self):
        print("child Wheel")

    def streeing(self):
        print("child streeing")


m = Maruti()

m.wheel()


def check(fun):
    def inner():
        print("inner")
        fun()

    return inner


@check
def add():
    print("main function")


add()
