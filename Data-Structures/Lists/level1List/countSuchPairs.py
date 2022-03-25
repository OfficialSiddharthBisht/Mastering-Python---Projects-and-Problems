# Given an array A of N integers along with a target integer K.
# Task is to find out the number of pairs of integers present in the array whose sum is equeal to the target value K.

def countSuchPairs(N , target ,arr):
    count = 0
    for i in range(0 , N):
        for j in range(0 , N):
            if(arr[i] + arr[j] == target):
                count = count + 1
    return int(count / 2)

print(countSuchPairs(5,9,[3,0,6,2,7]))
print(countSuchPairs(2,4,[2,2]))