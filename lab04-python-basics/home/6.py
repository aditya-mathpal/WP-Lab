'''
6. Write a Python class named Circle constructed by a radius and two methods
which will compute the area and the perimeter of a circle.
'''

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi*self.radius**2
    
    def perimeter(self):
        return 2*math.pi*self.radius

r = float(input("Enter radius of circle: "))
obj = Circle(r)
print(f"Area of circle is {round(obj.area(), 4)}, perimeter is {round(obj.perimeter(), 4)}")

'''
output:
Enter radius of circle: 4
Area of circle is 50.2655, perimeter is 25.1327
'''