# Write your solution here
def hash_square(length):
    row = 0
    while row < length:
        print("#" * length)
        row += 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)