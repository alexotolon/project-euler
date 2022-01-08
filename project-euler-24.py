ChodeCoreList = ["9","8","7","6","5","4","3","2","1","0"]

counter = 0

while len(ChodeCoreList) > 0:
    while len(ChodeCoreList[-1]) < 10:
        popstorage = ChodeCoreList.pop()
        for i in reversed(range(10)):
            if str(i) not in popstorage:
                ChodeCoreList.append(popstorage + str(i))
    counter += 1
    if counter == 1000000:
        print(ChodeCoreList.pop())
    else:
        ChodeCoreList.pop()
