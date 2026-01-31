'''
4. Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '['
and ']. These brackets must be close in the correct order, for example "()" and
"()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
'''


def verify_string(s):
    stack = []
    dict = {')':'(', '}':'{', ']':'['}
    for i in s:
        if i in '({[':
            stack.append(i)
        elif dict[i] == stack[-1]:
            stack.pop()
        else:
            return 0
    return not stack

s = input("Enter string: ")
if verify_string(s):
    print("Valid string")
else:
    print("Invalid string")

'''
output:
Enter string: ()[]{}
Valid string

Enter string: {{{
Invalid string
'''