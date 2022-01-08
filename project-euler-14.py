highest = 0
highestNum = 0

for times in range(1,1000001):
    n = times
    count = 0
    while n != 1:
        if n % 2== 1:
            n= 3*n +1
        else:
            n= n/2
        count += 1
    
    #print("Done "+str(times)+" in "+str(count)+" steps")
    
    if highest < count:
        highest = count
        highestNum = times
print("The answer is "+str(highest)+" on "+str(highestNum)+"!")
