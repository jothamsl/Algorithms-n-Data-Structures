"""
Given an array of n elements, write a function "search()" that finds 
element x in arr
"""

from typing import List, Union


def search(arr: List[int], x: int) -> int:
    """
    Search for value (x) in arr
    """
    for _, i in enumerate(arr):  # Loop through array
        if x == i:  # if value x is equal to i
            return _  # return the index
    return -1


if __name__ == "__main__":
    size = input("Input array size: ")
    array = list(map(int, input("Input array values: ").split(" ")))
    val = int(input("Input search value: "))
    res = search(array, val)

    if (val != -1):
        print("Value {} found in index {}".format(val, res))
    else:
        print("Value not found")

