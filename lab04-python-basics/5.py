'''
5. Write a Python class to find a pair of elements (indices of the two numbers) 
from a given array whose sum equals a specific target number.   
Input: numbers= [10,20,10,40,50,60,70],  target=50 
Output: 2, 3.
'''

class TwoSum:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
    
    def find_pair(self):
        seen = {}
        for idx, num in enumerate(self.arr):
            n = self.target - num
            if n in seen:
                return (seen[n], idx)
            seen[num] = idx
        return None

ts = TwoSum([], 0)

ts.arr = list(map(int, input("Enter elements of the array: ").split()))
ts.target = int(input("Enter target: "))

print("Elements at indices", ts.find_pair())

'''
output:
Enter elements of the array: 10 20 10 40 50 60 70
Enter target: 50
Elements at indices (2, 3)
'''