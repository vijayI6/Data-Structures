"""
Linear Search is also called Sequential Search and it is a simple method which is used to find a particular value in a array.
It works by comparing given value by every value in the array one by one in the sequence untill match is found

Best_Case --> Given value present in the first position
Worst_Case --> Given value is not present in the array
Time Complexity --> O(n)
Auxiliary Space -->O(1) 

"""
class LinearSearch:
    def __init__(self: object, array: list, value: int) -> None:
        self.array = array
        self.value = value

    def Searching(self) -> int:
        for i in range(len(self.array)):
            if self.value == self.array[i]:
                return i
        return -1



arr = list(map(int, input().split()))
val = int(input())
res = LinearSearch(arr, val)
print(f'The element is {res.Searching()} index position')

# Output
# 10 8 2 7 3 4 9 1 6 5
# 6
# The element is 8 index position
