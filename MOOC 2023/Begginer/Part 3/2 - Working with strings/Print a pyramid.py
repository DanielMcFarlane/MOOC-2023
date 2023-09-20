n = 10 # number of layers in the pyramid
row = "*"

while n > 0:
    print(" " * n + row)
    row += "**"
    n -= 1
    
# The print command within the loop prints a line, which begins with n spaces, followed by whatever is stored in the variable row. 
# Then two stars are added to the end of the variable row, and the value of the variable n is decreased by 1.