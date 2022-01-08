ChodeCoreList = ["9","8","7","6","5","4","3","2","1","0"]

anser = 0

while len(ChodeCoreList) > 0:
    while len(ChodeCoreList[-1]) < 10:
        popstorage = ChodeCoreList.pop()
        for i in reversed(range(10)):
            if str(i) not in popstorage:
                ChodeCoreList.append(popstorage + str(i))
    pandig = ChodeCoreList.pop()
    if int(pandig[1:4]) %2 == 0 and int(pandig[2:5]) %3 == 0 and int(pandig[3:6]) %5 == 0 and int(pandig[4:7]) %7 == 0 and int(pandig[5:8]) %11 == 0 and int(pandig[6:9]) %13 == 0 and int(pandig[7:10]) %17 == 0:
        anser += int(pandig)

print(anser)
