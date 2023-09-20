# Write your solution here
def greatest_number(num1, num2, num3):
    list = []
    list.append(num1)
    list.append(num2)
    list.append(num3)
    return max(list)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)