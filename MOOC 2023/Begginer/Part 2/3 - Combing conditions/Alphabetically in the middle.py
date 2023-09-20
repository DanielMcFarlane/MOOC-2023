# Write your solution here
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

if first > second and first > third:
    if second > third:
        mid = second
    else:
        mid = third
elif second > third:
    if third > first:
        mid = third
    else:
        mid = first
else:
    if second > first:
        mid = second
    else:
        mid = first
print(f"The letter in the middle is {mid}")


# A simpler way is

first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")

list = [first, second, third]
sorted_list = sorted(list)
print(f"The letter in the middle is {sorted_list[1]}")