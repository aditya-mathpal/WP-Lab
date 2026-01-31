'''
5. Write a Python class to reverse a string word by word.
'''

class Reverse:
    def __init__(self, s):
        self.s = s
    
    def rev(self):
        words = self.s.split()
        res = ' '.join(words[::-1])
        return res

words = input("Enter string: ")
obj = Reverse(words)
output = obj.rev()
print("Words reversed:", output)

'''
output:
Enter string: this is a test
Words reversed: test a is this
'''