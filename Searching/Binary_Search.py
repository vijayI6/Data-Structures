"""
Binary Search is a searching algorithm used to find an element in a sorted array efficiently.
It follows the Divide-and-Conquer approach.

Technique:

            1. Start with two pointers:
                left = 0 (start index)
                right = n-1 (end index)


            2. Find the middle element:
                mid = (left + right) // 2

            3. Compare the middle element with the target:

                If array[mid] == value → Element found → return mid.

                If array[mid] < value → Search in the right half → left = mid + 1.

                If array[mid] > value → Search in the left half → right = mid - 1.

            4. Repeat steps 2-3 until left > right.

            5. If not found → return -1.

"""

class BinarySearch:
    def __init__(self, array, value):
        self.array = sorted(array)  # ensure array is sorted
        self.value = value

    def Searching(self):
        left = 0
        right = len(self.array) - 1

        while left <= right:
            mid = (left + right) // 2  # recalculate mid every loop

            if self.array[mid] == self.value:
                return mid

            elif self.array[mid] < self.value:
                left = mid + 1

            else:
                right = mid - 1

        return -1


arr = list(map(int, input().split()))
val = int(input())

obj = BinarySearch(arr, val)
print(f"The element is in index position {obj.Searching()}")
    

# Output:
# 10 20 30 40 50
# 40
# The element is in index position 3
