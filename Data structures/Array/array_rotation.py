"""
Array Rotation
--------------

Write a function "rotate(arr[], d, n)" that rotates arr[] of size n by d elements.
E.g Given array [1, 2, 3, 4, 5, 6, 7], d = 2.
Rotate by 2 => [3, 4, 5, 6, 7, 1, 2]
"""

from typing import List
from copy import copy

arr = [1, 2, 3, 4, 5, 6, 7]
N = len(arr)
D = 6


def rotate(arr: List[int], d: int, n: int) -> List[int]:
    """
    Rotates Array by d
    """
    temp = [arr.pop(0) for i in range(d)]  # Pop first two array values
    for i in temp:
        arr.append(i)  # Append popped items back into the list
    return arr


if __name__ == "__main__":
    print("Initial Array: {}".format(arr))
    print("Modified Array of shift {} : {}".format(D, rotate(arr, D, N)))
