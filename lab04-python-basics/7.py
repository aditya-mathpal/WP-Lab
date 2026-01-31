'''
7. Write a Python class which has two methods get_String and print_String. The 
get_String accept a string from the user and print_String print the string in upper 
case.
'''

class String:
    def get_String(self):
        self.str = input("Enter string: ")
    def print_String(self):
        print(self.str.upper())


s = String()
s.get_String()
s.print_String()


'''
output:
Enter string: test 
TEST
'''