'''
6. Write a Python class to implement pow(x, n).
'''

import math

class Power:
    @staticmethod
    def pow(x, n):
        if n == 0: return 1
        if x == 0 or x == 1: return int(x)
        if n == 1: return x if not float(x).is_integer() else int(x)
        n_neg_flag = 0
        x_neg_flag = 0
        original_n = n
        original_x = x
        if n == 0: return 1
        if n < 0:
            n *= -1
            n_neg_flag = 1
        if x < 0:
            x_neg_flag = n%2
            x = -x
        res = math.exp(n * math.log(x))
        if n_neg_flag: res = 1/res
        if x_neg_flag: res *= -1
        if float(original_n).is_integer() and float(original_x).is_integer() and not n_neg_flag:
            return int(round(res, 0))
        return res


x, n = list(map(float, input("Enter x and n: ").split()))
res = Power.pow(x,n)
if float(n).is_integer() and float(x).is_integer():
    x, n = int(x), int(n)
print(f"pow({x}, {n}) = {round(res, 6)}")

'''
output:
Enter x and n: 2 10
pow(2, 10) = 1024
'''