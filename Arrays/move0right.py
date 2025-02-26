# Approach-1 using extra space or array
def move0RightI(arr):
    temp = []
    for element in arr:
        if element != 0:
            temp.append(element)

    temp.extend([0] * (len(arr) - len(temp)))
    return temp  # [Time and space complexity is O(n)]


# Approach-2 without using extra space or array
def move0RightII(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr


if __name__ == '__main__':
    lst = list(map(int, input().split(" ")))
    print(move0RightI(lst))
    print(move0RightII(lst))

# Output:
# 0 0 0 1 3 4 0 0
# [1, 3, 4, 0, 0, 0, 0, 0]
# [1, 3, 4, 0, 0, 0, 0, 0]
