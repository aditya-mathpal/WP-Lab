'''
3. Write a python program to sort words in alphabetical order.
'''

def merge(l, r):
    res = []
    i = j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1
    
    res.extend(l[i:])
    res.extend(r[j:])
    return res

def sort_words(arr):
    n = len(arr)
    if n <= 1:
        return arr
    if n == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    
    left = sort_words(arr[:n//2])
    right = sort_words(arr[n//2:])

    return merge(left, right)

print("Enter words to sort:")
strings = list(input().split())
strings = sort_words(strings)
print("Sorted words: ", strings)


'''
output:
Enter words to sort:
this is a test
Sorted words:  ['a', 'is', 'test', 'this']
'''