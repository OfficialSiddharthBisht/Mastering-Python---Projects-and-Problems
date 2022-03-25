# You are given an array arr of N integers.
# You need to printOdd, if thesum of all odd numbers present in the array is greater than sum of all the even numbers present in the array, or else printEven.
def battleOfEvenOdd(arr ,N):
    evenSum = 0
    oddSum = 0
    for i in range(0 , N):
        if(arr[i] % 2 == 0):
            evenSum += arr[i]
        elif(arr[i] % 2 == 1):
            oddSum += arr[i]
    if(evenSum > oddSum):
        return evenSum
    return oddSum

print(battleOfEvenOdd([1,2,3,4,5],5))
print(battleOfEvenOdd([2,4,6,8,9],5))        