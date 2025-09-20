"""
Bubble sort / Sinking sort algorithm in Python

Technique: 

    1) First we need to find length of the list(N) then we require N-1 passes for sort the given list
    
    2) In pass_1
            array[0] is compared with array[1] 
            array[1] is compared with array[2] and .......
            At the end of the pass_1, the largest element in the list is placed at the highest index on the list
            
    3) In pass_2
            array[0] is compared with array[1] 
            array[1] is compared with array[2] and so .......
            At the end of the pass_2, the second largest element in the list is placed at the second highest index on the list
            
    4) In pass(N-1)
            array[0] is compared with array[1] 
            array[1] is compared with array[2] and .......
            At the end of the pass(N-1), the smallest element in the list is placed at the first index on the list  
"""


# Bubble Sort
class bubbleSort:
    def __init__(self, array):
        self.array = array

    def Sorting(self):
        length = len(self.array)
        for i in range(length - 1):  # outerloop for passes (n-1)
            swapped = False
            for j in range(length - i - 1):  # Inner loop avoids sorted part
                if self.array[j] > self.array[j + 1]:  # comparison and swapping
                    swapped = True
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
            if not swapped:
                break
                
        return self.array


lst = list(map(int, input().split()))
obj = bubbleSort(lst)
result = obj.Sorting()
print(*result)

# output:
# 5 8 9 1 10 15 2 4 -- input
# 1 2 4 5 8 9 10 15 -- output
