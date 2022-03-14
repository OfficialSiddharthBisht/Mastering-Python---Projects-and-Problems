# You are given an array, stored in a variable with the size arr
# The size of the array is stored in a variable with the name n
# You have to traverse the array, and print only the even elements in the array.
# Print each number on a new line
# For example, consider the array as arr = [1 2 3 4 5], and the value stored in n = 5
# Then, the required output will be
# 2
# 4

def evenArr(arr):
    for i in range(len(arr)):
        if(arr[i] % 2 == 0):
            print(arr[i])
evenArr([1,2,3,4,5])