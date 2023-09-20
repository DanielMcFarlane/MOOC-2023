#  Getting position can be done with [] it starts at 0 and the final character has the index lenght -1
# input_string = input("Please type in a string: ")
# print("First character: " + input_string[0])
# print("Last character: " + input_string[len(input_string) - 1])

# The following program loops through all the characters in a string from first to last:
# input_string = input("Please type in a string: ")
# index = 0
# while index < len(input_string):
#     print(input_string[index])
#     index += 1

# you can use negative numbers to count backwards. You can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].
# input_string = input("Please type in a string: ")
# print("First character: " + input_string[0])
# print("Last character: " + input_string[-1])

# Write your solution here
word = input("Please type in a string: ")
index = -1

while index >= -len(word):
    print(word[index])
    index -= 1
