"""
Given an array of n elements, write a function "search()" that finds 
element x in arr
"""

from typing import List 


def search(arr: List[int], x: int) -> int:
    """
    Search for value (x) in arr
    
    arr: List of values
    x: Search value
    """
    for i in range(len(arr)):  # Loop through array
        if x == arr[i]:  # if value x is equal to i
            return i  # return the index
    return -1


if __name__ == "__main__":
    array = list(map(int, input("Input array values: ").split(" ")))
    val = int(input("Input search value: "))
    res = search(array, val)

    if (res != -1):
        print(f"Value {val} found in index {res}")
    else:
        print("Value not found")

