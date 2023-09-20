# Write your solution here
number = int(input("Please type in a number: "))
a = 1

while a <= number:
    b = 1
    while b <= number:
        print(f"{a} x {b} = {a * b}")
        b += 1
    a += 1