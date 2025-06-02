"""
The selection sort algorithm is an In-place comparison algorithm in which the list is divided into two parts:
    --> Sorted part at left end
    --> Unsorted part at right end
Initially, the Sorted part is empty.


Technique:
    First, find the smallest value in the array and place it in the first position. Then find the second-smallest value of the array and place it in the second position. 
    The process continues until we get a sorted array
    
        In pass_1:
            smallest value in the array is found along with index position then swap array[0] and array[position]
            Thus array[0] is sorted.
        In pass_2:
            Find the position of the second-smallest value present in the sub-array then swap array[1] with array[position]
            Thus array[0] and array[1] sorted.
"""


def Selection_Sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


lst = list(map(int, input().split(" ")))
Selection_Sort(lst)
print(lst)


# Output:
# 1 10 11 55 2 7 90
# [1, 2, 7, 10, 11, 55, 90]
