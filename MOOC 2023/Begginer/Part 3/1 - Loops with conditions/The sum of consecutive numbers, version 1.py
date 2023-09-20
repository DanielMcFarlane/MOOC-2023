# Write your solution here
limit = int(input("Limit: "))
floor = 1
sum = 1

while sum < limit:
    floor += 1
    sum += floor
print(sum)