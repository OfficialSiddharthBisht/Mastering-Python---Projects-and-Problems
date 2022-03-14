# Given two numbers X and num , to check if the value num is divisible by X
def divByX(x , num):
    if(num % x == 0):
        print("Yes")
        return
    else:
        print("No")
        return

divByX(5 ,25)