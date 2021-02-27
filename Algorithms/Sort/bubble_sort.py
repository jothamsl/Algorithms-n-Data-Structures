"""
TASK
----
Given an array, sort the array in an ascending order

EXPLANATION
-----------
The bubble sort algorithm takes in an array and compares each successive
pair of elements and inverts the elements if they are not in order.

[4, 2, 1, 0] -> [4, 2, 1, 0] -> [0, 1, 2, 4]
                 ^  ^
                 |--|-------- Compare both values, since
                              4 is larger than 2, swap position
"""



from typing import List


def bubble(arr: List[int]) -> List[int]:
    """
    Binary Sort
    -----------

    arr: Input array
    """
    i = len(arr) - 1
    while i >= 0:
        for j in range(1, i+1):
            if arr[j-1] > arr[j]:
                x = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = x
        i -= 1
    return arr


if __name__ == "__main__":
    array = list(map(int, input("Input array: ").split(" ")))
    print(bubble(array))
