"""
Selection sort algorithm is an In-place comparison based algorithm in which list is divided into two parts:
    --> Sorted part at left end
    --> Unsorted part at right end
Initially Sorted part is empty


Best_Case --> 0(n*n)
Worst_Case --> 0(n*n)
Average_Case --> 0(n*n)
Time Complexity --> O(n*n)
space complexity --> O(1)

Technique:
    First find the smallest value in the array and place it on first position. Then find the second-smallest
    value of the array and place it on second position. The process continues until we get sorted array

        In pass_1:
            smallest value in the array is fond along with index position then swap array[0] and array[position]
            Thus array[0] is sorted.
        In pass_2:
            Find the position of the second-smallest value present in the sub-array then swap array[1] with array[position]
            Thus array[0] and array[1] sorted.
"""


def Selection_Sort(array, size):
    for i in range(size):
        minimum_index = i
        for j in range(i + 1, size):
            if array[j] < array[minimum_index]:
                minimum_index = j
        array[i], array[minimum_index] = array[minimum_index], array[i]


lst = list(map(int, input().split(" ")))
length = len(lst)
Selection_Sort(lst, length)
print(f"Selection sort of the given array is {lst}")
