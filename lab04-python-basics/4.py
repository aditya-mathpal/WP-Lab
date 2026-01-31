'''
4. Write a Python class to get all possible unique subsets from a set of distinct 
integers
Input:[4,5,6]  
Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
'''

def subsets(arr):
    res = []

    def backtrack(curr, i):
        if i == len(arr):
            res.append(curr.copy())
            return
        
        backtrack(curr, i+1)

        curr.append(arr[i])
        backtrack(curr, i+1)
        curr.pop()
    
    backtrack([], 0)
    return res

arr = list(map(int, input("Enter elements of the array to generate all possible subsets:\n").split()))
print(subsets(arr))

'''
output:
Enter elements of the array to generate all possible subsets:
4 5 6
[[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]
'''