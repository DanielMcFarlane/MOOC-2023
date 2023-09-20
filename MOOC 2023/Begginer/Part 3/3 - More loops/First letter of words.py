# Write your solution here
word = input("Please type in a sentence: ")
i = 0

if len(word) != 0:
    print(word[0])
    while i < len(word):
        if word[i] == " ":
            print(word[i+1])
        i += 1