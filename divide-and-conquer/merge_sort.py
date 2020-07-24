# Input: array of n numbers, unsorted
# Output: array of same numbers, sorted in increasing order.
# O(nlogn)
# For every input array of n numbers, Merge Sort produces a sorted output array and uses at most 6nlogn + 6n operations

from typing import List
import math

def merge_sort(n: List):
    length = len(n)
    if (length == 1):
        return n
    middle = math.floor(length / 2)
    left = n[0:middle]
    right = n[middle:length]
    return merge(merge_sort(left), merge_sort(right))

def merge(left: List, right: List):
    result = []

    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result


test_list = [8, 7, 6, 5, 4, 3, 2, 1, 7, 6, 5, 4, 3, 2, 1, 54, 26, 93, 17, 77, 31, 44, 55, 20]
print(merge_sort(test_list))