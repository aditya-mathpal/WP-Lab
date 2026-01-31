'''
2. Write a python program to implement binary search with recursion.
'''

def bin_search(arr, l, r, key):
    if l > r: return -1
    n = (l+r)//2
    if arr[n] > key:
        return bin_search(arr, l, n-1, key)
    elif arr[n] < key:
        return bin_search(arr, n+1, r, key)
    else:
        return n

n = int(input("Enter size of array: "))
arr = [0] * n
arr = sorted(list(map(int, input("Enter elements of array: ").split())))
print("sorted array: ", arr)
key = int(input("Enter element to find: "))
res = bin_search(arr, 0, len(arr)-1, key)
if res == -1:
    print("Element not in array")
else:
    print("Element at index", res)


'''
output:
Enter size of array: 5
Enter elements of array: 7 2 9 1 8
sorted array:  [1, 2, 7, 8, 9]
Enter element to find: 7
Element at index 2
'''