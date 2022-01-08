import math

ChodeCoreList = ["1","2","3","4","5","6","7"]

answer = 0

while len(ChodeCoreList) > 0:
    while len(ChodeCoreList[-1]) < 7:
        popstorage = ChodeCoreList.pop()
        for i in range(1,8):
            if str(i) not in popstorage:
                ChodeCoreList.append(popstorage + str(i))
    aNsWeR = int(ChodeCoreList.pop())
    good = True
    for j in range(2,math.ceil(math.sqrt(aNsWeR))):
        if aNsWeR % j is 0:
            good = False
            break
    if good:
        print(aNsWeR)
        break
