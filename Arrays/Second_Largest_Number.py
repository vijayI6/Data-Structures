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


if __name__ == '__main__':
    lst = [10, 9, 11, 15]
    print(find2LargestI(lst))
    print(find2LargestII(lst))


# Output:
# 11
# 11
