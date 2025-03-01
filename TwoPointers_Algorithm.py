"""
Two-Pointer Algorithm: It is a method used in programming to solve problems using two pointers (or indices) to navigate through data structures like arrays or lists.

Syntax:

                def two_pointer_algorithm(arr):
                        arr.sort()
                        
                        left = 0
                        right = len(arr) - 1  # Initialize two pointers
    
                        while left < right:  # Continue until pointers meet
                                # Process elements at arr[left] and arr[right]
        
       
                                left += 1  # Move left pointer forward
                                right -= 1  # Move right pointer backward
    
                        return arr  # Processed array             

"""

# sum of 2 numbers that is equal to the given target value
def two_sum(arr, target):
    arr.sort()
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == target:
            return arr[i], arr[j]
        elif arr[i] + arr[j] < target:
            i += 1
        else:
            j -= 1

    return False

arr = [1, 2, 3, 4, 5, 6,]
target = 10
print(two_sum(arr, target))   # Output:  (3, 6)



# Ex: To check whether the given data is palindrome or not.
def check_palindrome(var):
    i = 0
    j = len(var) - 1

    while i < j:
        if var[i] != var[j]:
            return False
        i += 1
        j -= 1
    return True

for tc in range(int(input())):
    data = input()
    print(check_palindrome(data))

"""
Output:
        2
        99
        True
        100
        False
"""


# Ex: Reverse an array
arr = list(map(int, input().split(" ")))
arr.sort()
i, j = 0, len(arr) - 1
while i < j:
    arr[i], arr[j] = arr[j], arr[i]
    i += 1
    j -= 1
print(arr)

# Output : [5, 4, 3, 2, 1]
