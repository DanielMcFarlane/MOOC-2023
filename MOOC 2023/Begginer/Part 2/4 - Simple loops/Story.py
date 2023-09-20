story = ""
previous = ""

while True: 
    word = input("Please enter your word:")
    if word == "end" or word == previous:
        break

    story += word + " "
    previous = word
 
print(story)