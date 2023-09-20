# Write your solution here
word = input("Please type in a string: ")
index = 0

second = word[1]
second_last = word[-2]

if len(word) > 1 and second == second_last:
    print(f"The second and the second to last characters are {second}")
else:
    print("The second and the second to last characters are different")