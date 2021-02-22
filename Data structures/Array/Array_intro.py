# Other than some generic containers like a list, Python in its definition can also handle containers with specified data types.
# The array can be handled in Python by a module named "array". They can be useful when we have to manipulate only a specific data
# type values

import array

# Initializing array with array values
# Initializes array with signed integers
arr = array.array('i', [1, 2, 3])
#                  ^
# This is the Type code ("u": unicode character, "i": signed int)

# printing original array
print("The new created array: ", end=" ")
for i in range(0, 3):
    print(arr[i], end=" ")
print("\r")

# Using append() to insert new value at end
arr.append(4)

# printing appended array
print("The appended array is :", end=" ")
for i in range(0, 4):
    print(arr[i], end=" ")
print("\r")

# using insert() to insert value at specific position
arr.insert(2, 5)
#         ^  ^
#       indx val

# Printing array after insertion
print("The array after insertion is: ", end=" ")
for i in range(0, 5):
    print(arr[i], end=" ")
print("\r")

# Using pop() to remove element at 2nd position
print("The popped element is: ", end=" ")
print(arr.pop(2))

# Printing array after popping
print("The array after popping is: ", end=" ")
for i in range(0,4):
    print(arr[i], end=" ")
print("\r")

# Using remove() to remove 1st occurrence of 1
arr.remove(1)

# Printing array after removing
print("The array after removing is: ", end=" ")
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")

# Using index() to print index of 1st occurrence of 2 
print("The array of 1st occurrence fo 2 is: ", end="")
print(arr.index(2))

# Using reverse() to revere the array
arr.reverse()

# Printing array after reversing
print("The array after reversing is: ", end="")
for i in range(0,3):
    print(arr[i], end=" ")
print("\r")
