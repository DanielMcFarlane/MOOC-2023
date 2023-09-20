# Write your solution here
number = int(input("Please type in a number: "))

l = 1
r = number

while l < r:
    print(l)
    print(r)
    l += 1
    r -= 1

if l == r:
    print(l)