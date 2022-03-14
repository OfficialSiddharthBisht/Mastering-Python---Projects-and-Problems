# Given a string str and its length N , print true if the string constains atleast one vowel else print false
# len 
def checkVowel(string):
    for i in range(len(string)):
        if(string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u"):
            print(True)
            return
    print(False)
    return

checkVowel("siddharth")
checkVowel("bcdfg")

