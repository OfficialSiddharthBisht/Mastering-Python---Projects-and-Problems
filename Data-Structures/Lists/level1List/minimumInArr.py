#Given an array, stored in a variable with the size arr
#The size of the array is stored in a variable with the name n
#You have to find the minimum number in the array
#For example, consider the array asarr = [1 2 3 4 5], and the value stored in n = 5
#Then, the required output will be 1, as it is the smallest number in the array
def minimum(arr , N):
    minimum = arr[0]
    for i in range( 1 , N):
        if(arr[i] < minimum):
            minimum = arr[i]
    return minimum

print(minimum([6,5,9,-5,2],5))
