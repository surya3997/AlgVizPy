from sympy import *
import matplotlib.pyplot as plt

"""
x(k)  =    x(k - 1) - f(x(k - 1))
                     -------------
                      f'(x(k - 1))
"""

precision = 4
stopper = 20

var('x')

""" function of x """
f = x * cos(x) + 1

f_prime = diff(f)

x0 = 0
cnt = 1

y = N(f.subs(x, x0))
y_prime = N(f_prime.subs(x, x0))
x1 = round(x0 - (y / y_prime), precision)

x_list = []
y_list = []
print(x0, y)
x_list.append(x0)
y_list.append(y)

while(cnt < stopper and x0 != x1):
    x0 = x1
    y = N(f.subs(x, x0))
    y_prime = N(f_prime.subs(x, x0))
    x1 = round(x0 - (y / y_prime), precision)
    print(x0, '\t', y)
    x_list.append(x0)
    y_list.append(y)
    cnt += 1

print(x0, '\t', y)
x_list.append(x0)
y_list.append(y)
print("The method took", cnt, "iterations to complete.")

plt.scatter(x_list, y_list)
plt.scatter(x0, y, c='red')
plt.show()
