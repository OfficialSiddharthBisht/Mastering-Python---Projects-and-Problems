#  Given a number stored in a variable with the name n
#  To print n lines and on each line print n stars
# eg- n=4
# * * * *
# * * * *
# * * * *
# * * * *
def boxPattern(N):
    for i in range(N):
        str = ""
        for j in range(N):
            str += "* "
        print(str)

boxPattern(5)