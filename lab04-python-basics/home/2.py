'''
2. Write a python program to implement bubble sort.
'''

def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: return

arr = list(map(int, input("Enter elements of the list: ").split()))
bubble_sort(arr)
print("sorted list:", arr)

'''
output:
Enter elements of the list: 7 6 5 4 3 2 1
sorted list: [1, 2, 3, 4, 5, 6, 7]
'''