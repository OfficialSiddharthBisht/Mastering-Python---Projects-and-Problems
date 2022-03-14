# Given a 2d array arr with N rows and M columns for all columns print the sum of even numbers present in the column

def columnEvenSum(N , M , arr):
    # print(N , M , arr)
    for i in range(N):
        sum = 0
        for j in range(M):
            if(arr[i][j] % 2 == 0):
                sum += arr[i][j]
        print(sum)

columnEvenSum(3 , 4 , [[1,2,3,4],[4,5,6,7],[7,8,9,10]])
# 2 + 4 = 6
# 4 + 6 = 10
# 8 + 10 = 18
# expected 6 10 18