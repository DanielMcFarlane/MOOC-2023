# Write your solution here
# Let's take the square root of math-module in use
from math import sqrt

a = float(input('Value a: '))
b = float(input('Value b: '))
c = float(input('Value c: '))

# Note that the square root can also be calculated using power.
# sqrt(9) is equivalent to 9 ** 0.5

x1 = (-b + sqrt(b ** 2 - (4 * a * c)))  / (2 * a)
x2 = (-b - sqrt(b ** 2 - (4 * a * c)))  / (2 * a)
print(f'The roots are {x1} and {x2}')