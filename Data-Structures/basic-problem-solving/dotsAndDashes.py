# You are given a number stored in a variable with the name N

# Print the required pattern, such that for all numbers in the range[1, N], including N, if the number is odd, print a single _ , else print N * without space, on a new line

# For example, consider the value stored in N = 5. Therefore, the required output is

# _
# *****
# _
# *****
# _

def dotsAndDashes(N):
    for i in range(N):
        if(i % 2 == 0):
            print("_")
        else:
            print(N * "*")

dotsAndDashes(5)
