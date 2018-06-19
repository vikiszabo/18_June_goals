'''
Given an array of integers, Find the minimum sum which is obtained from summing each Two integers product.
Array/list will contain positives only.
Array/list will always have even size
1- minSum({5,4,2,3}) ==> return (22)
The minimum sum obtained from summing each two integers product , 5*2 + 3*4 = 22
'''


tomb = [5,4,2,3]

def find_min_sum(arr):
    pass

def min_num(arr):
    min = 1000000
    for i in range(0, len(arr)):
        if arr[i] < min:
            min = arr[i]
            arr[i] = None
    return min


def max_num(arr):
    max = 0
    for i in range(0, len(arr)):
        if arr[i] > max:
            max = arr[i]
            arr[i] = None
    return max


print(find_min_sum(tomb))