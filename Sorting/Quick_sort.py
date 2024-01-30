"""
Quick sort is also known  Partition exchange sort and This algorithm follows "Divide-conquer" approach
    Best-Case --> O(n)
    Average-Case --> O(n log n)
    Worst_Case --> O(n*n)
    Space Complexity --> O(n)

Technique:
    1) Choose the first element of the array as the pivot element.
    2) Create two empty lists, left and right.
    3) For each element in the array except for the pivot:
    4) If the element is smaller than the pivot, add it to the left list.
    6) If the element is greater than or equal to the pivot, add it to the right list.
    7) Concatenate the sorted left list, the pivot element, and the sorted right list.
    8) Return the concatenated list.
"""


def Quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        left = [i for i in a[1:] if i < pivot]
        right = [j for j in a[1:] if j >= pivot]
        return Quick_sort(left) + [pivot] + Quick_sort(right)  # Recursively calling the function


lst = list(map(int, input().split(' ')))
res = Quick_sort(lst)
print(f"The Sorted list is {res}")

# Output
# 1 10 11 55 2 7 90
# The Sorted list is [1, 2, 7, 10, 11, 55, 90]
