"""
Two-Pointer Algorithm: It is a method used in programming to solve problems by using two pointers (or indices) to navigate through data structures like arrays or lists.

Syntax:

        # Sort the array to traverse the array
        array_name.sort()
        
        # Initialize two pointers
        i = 0                                     # Start pointer at the beginning
        j = len(array_name) - 1                   # End pointer at the end of the list

        # Loop until the two pointers meet
        while i < j:
            start = array_name[i]              # Element at the start pointer
            end = array_name[j]                # Element at the end pointer

            # Check if a specific condition is met
            if start + end == target:       # Example condition
                return (start, end)         # Return the pair if condition is true

            # Adjust pointers based on the condition
            if start + end < target:
                i += 1                       # Move the start pointer to the right
            else:
                j -= 1                       # Move the end pointer to the left

        # If no pair is found
        return None


"""


# Ex: Two sum (consecutive elements sum == target)

def Two_Sum(arr, tar):
    arr.sort()
    i = 0
    j = len(arr) - 1
    while i < j:
        start = arr[i]
        end = arr[j]

        if start + end == tar:
            return start, end
        elif start + end < tar:
            i += 1
        else:
            j -= 1

    return False


lst = list(map(int, input().split()))
target = int(input())
print(Two_Sum(lst, target))

"""
Output:
        1 2 3 4 5 6
        9
        (3, 6)
"""


# Ex: To check given data is palindrome or not?

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
