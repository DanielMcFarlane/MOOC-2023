# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points *= 1.1
    print("Your bonus is 10 %")
elif points >= 100:
    points *= 1.15
    print("Your bonus is 15 %")

print(f"You now have {points} points")


# points *= 1.1 is the same thing as points = points * 1.1
