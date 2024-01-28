"""
Bubble sort /Sinking sort algorithm in python

    Best-Case --> 0(n)
    Worst-Case -->0(n*n)
    Average-Case --> 0(n*n)
    Space Complexity --> 0(1)
"""


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):  # outerloop for passes (n-1)
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:  # comparison and swapping
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            break


lst = list(map(int, input().split(' ')))
bubble_sort(lst)
print("The Bubble Sort of given list is:")
for i in range(len(lst)):
    print(lst[i], end=" ")

# output:
# 5 8 9 1 10 15 2 4
# The Bubble Sort of given list is:
# 1 2 4 5 8 9 10 15
