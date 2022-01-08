lopp =list(range(2,2000000))
count =0
while len(lopp) !=0:
    #print(lopp[0])
    count =count+lopp[0]
    lopp =[w for w in lopp if w%lopp[0] != 0]
print(count)
