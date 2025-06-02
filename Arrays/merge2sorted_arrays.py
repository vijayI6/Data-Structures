# 1-Approach without using extra space
arr1 = [1, 3, 5, 7]
arr2 = [0, 2, 6, 8, 9]

i = len(arr1) - 1
j = 0

while i >= 0 and j < len(arr2):
    if arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1
    else:
        break
      
arr1.sort()
arr2.sort()

print(arr1 + arr2)

# Output:
# [0, 1, 2, 3, 5, 6, 7, 8, 9]

# Approach-2 with using extra space
merged = []
i = j = 0
arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1
print(merged)

# Output:
# [0, 1, 2, 3, 5, 6, 7, 8, 9]
