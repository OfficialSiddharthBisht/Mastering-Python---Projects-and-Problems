# There is a long queue of people in front of ATMs. Due to withdrawal limit per person per day, people come in groups to withdraw money.
# Groups come one by one and line up behind the already present queue. The groups have a strange way of arranging themselves.
# In a particular group, the group members arrange themselves in increasing order of their height(not necessarily strictly increasing).
# You are given a array representing heights of persons in queue. Since groups are standing behind each other, one cannot differentiate between different groups and the exact count cannot be given.
# Can you find the minimum number of groups that can be observed in the queue?
def atmQueue(arr , N):
    no_of_line = 1
    for i in range(1 , N ):
        if(arr[i] < arr[i - 1]):
            no_of_line = no_of_line + 1
    return no_of_line

print(atmQueue([1,2,4,3,5,8],6))