# 3-Sum
nums = list(map(int, input().split()))
res = []
nums.sort()
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    j = i + 1
    k = len(nums) - 1
    while j < k:
        total = nums[i] + nums[j] + nums[k]
        if total == 0:
            res.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1

            while j < k and nums[j] == nums[j - 1]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1

        elif nums[i] + nums[j] + nums[k] < 0:
            j += 1
        else:
            k -= 1
print(res)

# Output:
# 0 0 0
# [[0, 0, 0]]


# 4 Sum
nums = list(map(int, input().split()))
target = int(input())
nums.sort()
res = []

n = len(nums)
for i in range(n - 3):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, n - 2):
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:
            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total == target:
                res.append([nums[i], nums[j], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1
            else:
                right -= 1
print(res)


# Output:
# 2 2 2 2
# 8
# [[2, 2, 2, 2]]

