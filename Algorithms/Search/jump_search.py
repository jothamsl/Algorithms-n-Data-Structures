"""
TASK
----
Given a sorted array of elements, find the value x using the jump search
algorithm

EXPLANATION
------------
Like Binary search, jump search is a search algorithm for sorted arrays.
The basic idea is to check fewer elements (than linear search) by jumping
ahead by fixed steps or skipping some elements in place of searching all
elements. The sorted array of data is split into subsets of elements
called blocks. x is found by comparing it with the search candidate in
each block. Since the array is sorted, the search candidate is the
highest value of a block.
                          1         2
                      |-------| |-------|
[1, 2, 3, 4, 5, 6] -> [1, 2, 3] [4, 5, 6] <- Compare x conditionaly, if x
                          ^         ^        Greater than largest value 
   x = 4                  |---------|        in 1 (3), then move on to 2.
                               |             Then perform linear search 
                             Blocks          on 2 till value is found. If
                                             the search candidate is the 
                                             same as x, return the candidate
"""

import math
from typing import List


def jump_search(arr: List[int], x: int) -> int:
    """
    Jump search
    -----------
    Jump search algorithm

    arr: Input array
    x: search value
    n: length of array
    m: step length (amount of values in block)
    i: starting interval
    """
    n = len(arr) 
    m = int(math.sqrt(n))
    i = 0

    def lin(array: List[int], val: int, loc: int) -> int:
        # loc is the index where the remaining block begins
        i = 0
        while i != len(array):
            if array[i] == val:
                return loc+i 
            i += 1
        return -1

    while i != n-1 and arr[i] < x:
        # [(m+i)-1] is the last index of each block
        if arr[(m+i)-1] == x: # if largest of block is equal to x
            return (i+m)-1
        if arr[(m+i)-1] > x: # if largest of block is greater than x
            return lin(arr[i:(m+i)-1], x, i)
        i += m

    b = arr[i:i+m] # if 
    return lin(b, x, i)



if __name__ == "__main__":
    array = list(map(int, input("Input array: ").split(" ")))
    val = int(input("Input search value: "))
    result = jump_search(array, val)
    if result != -1:
        print(f"Search result {val} found in index {result}")
    else:
        print("Value not found")
