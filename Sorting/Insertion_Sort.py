"""
It is a very simple sorting algorithm in which sorted array is built one element at a time because it is a comparison based sorting algorithm

Technique:
           ◎ The array is divided in to 2-sets. one set is used to store sorted values and another set is used as unsorted values
           ◎ Suppose  there are n elements in the array. Intially the element with index 0 is in the sorted set remaining elements are in the unsorted set
           ◎ During each iteration, the first element in the unsorted set is picked up and inserted into the correct position in the sorted set
           
"""
class InsertionSort:
    def __init__(self, array):
        self.array = array

    def Sorting(self):
        # Go through each element starting from index 1
        for i in range(1, len(self.array)):
            key = self.array[i]        # Current element to insert
            j = i - 1                # Previous index

            # Move larger elements one step to the right
            while j >= 0 and self.array[j] > key:
                self.array[j + 1] = self.array[j]
                j -= 1

            # Place the key in the correct position
            self.array[j + 1] = key

        return self.array


numbers = list(map(int, input("Enter numbers: ").split()))
obj = InsertionSort(numbers)
result = obj.Sorting()
print(result)


# Output:
# 8 3 5 2 7
# [2, 3, 5, 7, 8]
