# Given a list/array of N elements print the alternate elements of the list

def alternateElem(arr,N):
    for i in range(0, N , 2):
        print(arr[i])

alternateElem([1,2,3,4,5],5)