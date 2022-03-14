# Given a number , stored in a variable with the name num
# To find the sum of all even numbers greater than 0, and less than or equal to the value stored in num
def evenSum(N):
    sum = 0
    for i in range(N + 1):
        if(i % 2 == 0):
            sum += i
    print(sum)

evenSum(6)
#  2 + 4 + 6 = 12