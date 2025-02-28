# Approach-1
def cumSum1(arr):
    total = 0
    cumsum = []
    for i in arr:
        total += i
        cumsum.append(total)
    return cumsum


# Approach-2
def cumSum2(arr):
    res = [sum(arr[:+i + 1]) for i in range(len(arr))]
    return res


# Approach-3
from itertools import accumulate

def cumSum3(arr):
    res = list(accumulate(arr))
    return res


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]
    print(cumSum1(lst))
    print(cumSum2(lst))
    print(cumSum3(lst))

# Output:
# [1, 3, 6, 10, 15]
# [1, 3, 6, 10, 15]
# [1, 3, 6, 10, 15]
