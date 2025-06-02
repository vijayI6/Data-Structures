"""
Bubble sort / Sinking sort algorithm in Python

Technique: 

    1) First we need to find length of the list(N) then we require N-1 passes for sort the given list
    
    2) In pass_1
            array[0] is compared with array[1] 
            array[1] is compared with array[2] and .......
            At the end of the pass_1, the largest element in the list is placed at the highest index on the list
            
    3) In pass_2
            array[0] is compared with array[1] 
            array[1] is compared with array[2] and so .......
            At the end of the pass_2, the second largest element in the list is placed at the second highest index on the list
            
    4) In pass(N-1)
            array[0] is compared with array[1] 
            array[1] is compared with array[2] and .......
            At the end of the pass(N-1), the smallest element in the list is placed at the first index on the list  
"""


def bubble_sort(a):
    n = len(a)
    for i in range(n - 1):  # outerloop for passes (n-1)
        swapped = False
        for j in range(0, n - i - 1): # Inner loop avoids sorted part
            if a[j] > a[j + 1]:  # comparison and swapping
                swapped = True
                a[j], a[j + 1] = a[j + 1], a[j]
        if not swapped:
            break


lst = list(map(int, input().split()))
bubble_sort(lst)
print(lst)

# output:
# 5 8 9 1 10 15 2 4 -- input
# 1 2 4 5 8 9 10 15 -- output
