# Given a number stored in a variable with the name num 
# Print num lines such that there are numbers from 1 to i,such that on each line you print only one number. Also i represents all the numbers form 1 to num.
# eg n=5 output - 1 1 2 1 2 3 1 2 3 4 1 2 3 4 5

def tillN(N):
    ans = ""
    for i in range(N + 1):
        for j in range(i):
            ans += str(j + 1) + " "
            j = j + 1
        i = i + 1
    print(ans)
tillN(5)