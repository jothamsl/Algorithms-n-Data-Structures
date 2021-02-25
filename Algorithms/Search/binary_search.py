"""
TASK
____
Given a sorted array of n elements, write a function "binary_search()" to 
search for a given element x in the array. 

EXPLANATION
____________
The binary search algorithm is only valid on an array of sorted values.
To perform a binary search operation, search a sorted array by reapeatedly
dividing the search interval in half.

[1, 2, 3, 4, 5] -> [1, 2, 3, 4, 5] <- If x is greater than the middle value,
                          ^           traverse the right side of the array 
  x = 4                   |           otherwise, traverse the left side of 
                       Mid val        the array. If x is equal to mid value,
                                      then return index of mid value
"""

from typing import List


def binary_search(arr: List[int], x: int):
    """
    Binary search algorithm divides array in to smaller halves in 
    search of x

    arr: Input array
    x: Search value
    """

    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        val = arr[mid]

        if val == x:
            return mid
        if val < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def binary_search_recursive(arr: List[int], x: int, f: int, r: int) -> int:
    """
    Recursive Binary search algorithm divides array into to smaller
    halves recursively in order to find x 

    arr: Input array
    x: Search value
    f: start index
    r: max index value
    """

    if r >= f:
        mid = f + (r - f) // 2
        print(mid)

        if arr[mid] == x:
            return mid
        if arr[mid] > x:
            binary_search_recursive(arr, x, f, mid-1)
        else:
            return binary_search_recursive(arr, x, mid+1, r)
    else:
        return -1


if __name__ == "__main__":
    array = list(map(int, input("Input array: ").split(" ")))
    val = int(input("Input search value: "))
    # result = binary_search_recursive(array, val, 0, len(array)-1)
    result = binary_search(array, val)
    if result != -1:
        print(f"Value {val} found at index {result}")
    else:
        print("Element not found")
