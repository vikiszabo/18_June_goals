'''
Given an array/list [] of n integers , find maximum triplet sum in the array Without duplications .
Array/list size is at least 3.
Array/list numbers could be a mixture of positives , ngatives also zeros .
Repeatition of numbers in the array/list could occur , So (duplications are not included when summing).
As the triplet that maximize the sum {6,8,3} in order , their sum is (17)
Note : duplications are not included when summing , (i.e) the numbers added only once .
As the triplet that maximize the sum {8, 6, 4} in order , their sum is (18) ,
Note : duplications are not included when summing , (i.e) the numbers added only once
As the triplet that maximize the sum {12 , 29 , 0} in order , their sum is (41) ,
Note : duplications are not included when summing , (i.e) the numbers added only once .
'''
import sys

arr = {1, 1, 3, 5, 5, 6}


def max_tri_sum(array):
    if len(array) < 4:
        return 0
    set_array = set(array)
    max = -1000000
    cut_list = list(set_array)
    for i in range(0, len(cut_list)):
        for j in range(i+1, len(cut_list)):
            for k in range(j+1, len(cut_list)):
                maxn = cut_list[i] + cut_list[j] + cut_list[k]
                if maxn > max:
                    max = maxn
    return max


print(max_tri_sum(arr))


def mmax_tri_sum(numbers):
    return sum(sorted(set(numbers))[-3:])