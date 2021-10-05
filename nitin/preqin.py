# -*- coding: utf-8 -*-
# @Time    : 8/16/2021 6:54 PM
# @Author  : Anand Kumar
# @Email   : harryanand060@gmail.com
# @File    : preqin.py
# @Software: PyCharm


# Array Pair Sum

arr = [1, 1, 2, 3, 4, 2, 1, 3]
sum = 4
''' 
seen_set=set()
output_set=set()

1=> 4-1=> 3 not in seen_set()=> {1}
1=> 4-1=> 3 not in seen_set(1)=> {1,1}=>{1}
2=> 4-2=> 2 not in seen_set(1)=> {1,2}
3=> 4-3=> 1 not in seen_set(1,2)=> {1,2} else output_set((min(i,target),max(i,target)))=>{(1,3)}
4=> 4-4 =>0 not in seen_set(1,2)=>{1,2,0}

list(output_set)=>[(1,3)]
map(str,[(1,3)]=> ['(1,3)']
'\'.join(['(1,3)'])
output= (1,3)

'''


def pair_sum(arr, sum):
    if len(arr) < 2:
        return
    seen = set()
    output = set()
    for i in arr:
        target = sum - i
        if target not in seen:
            seen.add(i)
        else:
            output.add((min(i, target), max(i, target)))
    list_output = list(output)
    # print(list_output)
    map_val = map(str, list_output)
    # print(map_val)
    print('\n'.join(map_val))


# Matrix Region Sum

matrix_arr = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

A = (0, 0)
D = (1, 1)


def matrix_region_sum(arr, A, D):
    if len(arr) == 0:
        return False
    sum = 0
    for i in range(A[0], D[0] + 1):
        print(f"i :{i}")
        for j in range(A[1], D[1] + 1):
            sum += matrix_arr[i][j]
    print(sum)


def largest_continous_sum(arr):
    if len(arr) == 0:
        return
    max_num = currentSum = arr[0]
    for i in arr[1:]:
        currentSum = max(currentSum + i, i)
        max_num = max(currentSum, max_num)
        print(f"Current Sum : {currentSum}, max_sum : {max_num}")
    print(max_num)


def find_largest_sequence_sum(arr):
    if len(arr) == 0:
        return
    diff = 1
    i=0
    sum=0
    current=arr[0]
    next=arr[1]
    i=0
    while diff == 1:
        diff = next-current
        if diff ==1:
            sum+=current

        else:
            sum=0
            diff=1
        current = arr[i]
        next = arr[i + 1]
        i +=1

arr1=[4,1,0,2,9,6,8,7,5,3]
arr2=[6,4,7,2,1,0,8,3,9]

# print(arr1+arr2)
result=0
for row in arr1+arr2:
    result ^=row
print(result)






# if __name__ == '__main__':
#     # pair_sum(arr, sum)
#     # matrix_region_sum(matrix_arr,A,D)
#     arr = [1, 2, 3, 1, 2, 3, 4, 5, 6, -1]
#     find_largest_sequence_sum(arr)
