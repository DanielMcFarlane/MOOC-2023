# Write your solution here
while True:
    number = int(input("Please type in a number: "))
    if number <= 0:
        break

    f = 1
    i = 1
    while i <= number:
        f *= i
        i += 1

    print(f"The factorial of the number {number} is {f}")
print("Thanks and bye!")
