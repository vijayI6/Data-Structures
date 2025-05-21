# 1-Approach
n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] == arr[j]:
            print(arr[i])
            break
        else:
            continue
    break


# 2-Approach
n = int(input())
arr = list(map(int, input().split()))
seen = set()
for ele in arr:
    if ele in seen:
        print(ele)
        break
    else:
        seen.add(ele)

# Output:
# 5
# 1 2 2 2 3
# 2
