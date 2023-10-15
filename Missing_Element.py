"""
Rule: (sorted / unsorted) data must be in a sequence and n is greater than len(lst)
"""

n = int(input('Enter length:'))
lst = list(map(int, input().split()))
print((n * (n + 1) // 2) - sum(lst), 'is the missing number')

# sample output:
# n = 6
# lst = [1, 3, 4, 5, 6]
# 2 is the missing element
