# You are given an array, stored in a variable with the name array
# The size of the array is stored in a variable with the name N
# You are also given another number stored in a variable with the name K
# Print the output according to the following conditions
# 1. If the count of odd elements in the array is greater than the value stored in K, print "Nice Array", without quotes
# 2. Else, print "Bad Array", without quotes
def niceArr(arr ,N , K):
    count = 0
    for i in range(0 , N):
        if(arr[i] % 2 != 0):
            count = count + 1
    if(count > K):
        return "Nice Array"
    return "Bad Array"

print(niceArr([1,2,3,4,5],5,8))