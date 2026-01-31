'''
1. Write a python program to reverse a content a file and store it in another file.
'''

with open('input.txt', 'r') as file:
    contents = file.read()

with open('output.txt', 'w+') as file:
    file.write(contents[::-1])

'''
input.txt:
this is a test file, the outputs will be reversed

tuptuo eht ni elbadaer si trap siht


output.txt:
this part is readable in the output

desrever eb lliw stuptuo eht ,elif tset a si siht
'''