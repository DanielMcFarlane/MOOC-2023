# Write your solution here
limit = int(input("Limit: "))
floor = 1
sum = 1
numbers = "1"

while sum < limit:
    floor += 1
    sum += floor
    numbers += f" + {floor}"
print(f"The consecutive sum: {numbers} = {sum}")