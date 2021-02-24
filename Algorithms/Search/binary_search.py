"""
Given a sorted array of n elements, write a function "binary_search()" to search 
for a given element x in the array. To perform a binary search operation, 
search a sorted array by reapeatedly dividing the search interval in half.
"""

from typing import List


def binary_search(arr: List[int], x: int, f: int, r: int) -> int:
    """
    Binary search algorithm divides array into to smaller
    halves inorder to find value

    arr: Input array
    x: Search value
    f: start index
    r: max index value
    """

    # Base case
    if r >= f:
        mid = f + (r - f) // 2  # Mid value

        if arr[mid] == x:
            return mid

        if arr[mid] > x:
            binary_search(arr, x, f, mid-1)

        else:
            return binary_search(arr, x, mid+1, r)
    else:
        return -1


if __name__ == "__main__":
    array = list(map(int, input("Input array: ").split(" ")))
    val = int(input("Input search value: "))
    result = binary_search(array, val, 0, len(array)-1)
    if result != -1:
        print(f"Value {val} found at index {result}")
    else:
        print("Element not found")
