"""
Two-Pointer Algorithm: This is a programming method that solves problems by using two pointers (or indices) to navigate data structures like arrays, lists, and Strings.

Syntax:

               def two_pointer_algorithm(arr):
                  # Optional: sort the array if needed for the specific problem
                  arr.sort()
    
                  # Initialize two pointers
                  left = 0
                  right = len(arr) - 1

                   
                  while left < right:  # Process the array until the two pointers meet
                        # Access elements using arr[left] and arr[right]
                        # Example: check if their sum equals a target, swap values, etc.
                        # Custom logic here
                
                        # Move the pointers inward
                        left += 1
                        right -= 1
                
                   
                    return arr  # Return the processed array or result

"""

# sum of 2 numbers that is equal to the given target value
def two_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == target:
            return arr[left], arr[right]
          
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1

    return False

arr = [1, 2, 3, 4, 5, 6]
target = 10
print(two_sum(arr, target))   # Output:  (4, 6)



# Ex: To check whether the given data is a palindrome or not.
def check_palindrome(var):
    left = 0
    right = len(var) - 1

    while left < right:
        if var[left] != var[right]:
            return False
        left += 1
        right -= 1
    return True

for tc in range(int(input())):
    data = input()
    print(check_palindrome(data))


# Output:
#         2
#         99
#         True
#         100
#         False


# Ex: Reverse an array
arr = list(map(int, input().split(" ")))
left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1
  
print(arr)

# Output : [5, 4, 3, 2, 1]
