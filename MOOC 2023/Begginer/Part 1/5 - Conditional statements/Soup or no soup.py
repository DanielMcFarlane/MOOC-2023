# Write your solution here
name = input('Please tell me your name: ')

if name != "Jerry":
    portions = int(input('How many portions of soup? '))
    cost = 5.90
    print(f'The total cost is {portions * cost}')
    print('Next please!')
else: 
    print('Next please!')
    