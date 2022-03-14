# ICPC (https://icpc.baylor.edu/) is International Collegiate Programming Contest is an algorithmic programming contest for college students. You are provided list of countries in correct ranking. Your task is to write a program that prints the rank of India in ICPC.
# 5                                                5
# Russia
# USA
# Japan
# China
# India

def ACM_ICPC_India_Rank(N , countriesArr):
    i = 0
    while(i < N):
        if(countriesArr[i] == "India"):
            print(i + 1)
        i = i + 1
    

countriesArr=["Russia","USA","Japan","India","China"]
ACM_ICPC_India_Rank(5,countriesArr)