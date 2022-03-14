# You are given two numbers stored in the variable with the following names,
# num, K
# You have to print all the numbers in the range[1,num], such that for each number, the operation i % K == 0, where i refers to the numbers present in that range
# Print each number on a new line

def divByK(num , K):
    for i in range(num):
        if( i % K == 0 and i != 0):
            print(i)

divByK(7,2)