# Given an array of N elements print the sum of all elements in the array
def sumArr(arr):
    sum = 0
    for x in arr:
        sum += x;
    return sum;

print(sumArr([1,2,3,4,5]))