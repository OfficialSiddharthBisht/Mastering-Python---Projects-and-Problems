# You are provided an array arr which has n integers.
# You need to find the count of all such integers in array which are larger than its neighbours.
# Neighbours of a integer in array are its adjacent integers. 
def competeWithNeighbour(arr,N):
    count = 0
    for i in range(0 , N):
        if(i == 0 and arr[i] > arr[i + 1]):
            count = count + 1
        elif(i == N - 1 and arr[i] > arr[i - 1]):
            count = count + 1
        else:
            if(arr[i] > arr[i + 1] and arr[i] > arr[i - 1]):
                count = count + 1
    return count

print(competeWithNeighbour([4,2,3,4,2,1,6,5,8],9))
