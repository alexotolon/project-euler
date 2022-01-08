lopp =list(range(2,1000000))
count =0
while count < 10001:
    print(lopp[0])
    count =count+1
    lopp =[w for w in lopp if w%lopp[0] != 0]
