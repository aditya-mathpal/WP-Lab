'''
1. Write a python program to select smallest element from a list in an expected
linear time.
'''

arr = list(map(int, input("Enter elements of the list: ").split()))
smallest = float('inf')
for i in arr:
    if smallest > i: smallest = i
print("smallest element is", smallest)

'''
output:
Enter elements of the list: 7 2 9 5 1 6
smallest element is 1
'''