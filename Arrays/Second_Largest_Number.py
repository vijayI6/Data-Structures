# Approach-1
import heapq  # heapq module provides .nlargest(k, array) built-in function to get the k largest elements.

def find2LargestI(arr):
    uniqueArr = set(arr)
    if len(uniqueArr) < 2:
        return -1
    else:
        res = heapq.nlargest(2, uniqueArr)
        return res[1]


# Approach-2
def find2LargestII(arr):
    res = list(set(arr))
    res.sort()
    if len(res) < 2:
        return -1
    return res[-2]


# Approach-3
def find2LargestIII(arr):
    if len(arr) < 2:
        return 0

    max1 = float("-inf")
    max2 = float("-inf")

    for ele in arr:
        if ele > max1:
            max2 = max1
            max1 = ele
        elif ele > max2 and ele != max1:
            max2 = ele

    return max2 if max2 != float("-inf") else -1



if __name__ == '__main__':
    lst = [10, 9, 11, 15]
    print(find2LargestI(lst))
    print(find2LargestII(lst))
    print(find2LargestIII(lst))


# Output:
# 11
# 11
# 11
