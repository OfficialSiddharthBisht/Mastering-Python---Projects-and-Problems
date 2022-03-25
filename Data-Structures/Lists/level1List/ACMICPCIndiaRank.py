# ICPC (https://icpc.baylor.edu/) is International Collegiate Programming Contest is an algorithmic programming contest for college students. You are provided list of countries in correct ranking. Your task is to write a program that prints the rank of India in ICPC.
# Input         Output
# 5             5
# Russia
# USA
# Japan
# China
# India
def icpcIndiaRank(arr,N):
    for i in range(0,N):
        if(arr[i] == "India"):
            print(i + 1)

icpcIndiaRank(["Russia","USA","Japan","China","India"],5)