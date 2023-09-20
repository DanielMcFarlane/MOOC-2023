# Write your solution here
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
opperation = input('Operation: ')

if opperation == "add":
    print(f'{number1} + {number2} = {number1 + number2}')
if opperation == "multiply":
    print(f'{number1} * {number2} = {number1 * number2}')
if opperation == "subtract":
    print(f'{number1} - {number2} = {number1 - number2}')