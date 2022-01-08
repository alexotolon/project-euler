ChodeCoreList = ["a","b","c"]

while len(ChodeCoreList) > 0:
    while len(ChodeCoreList[-1]) < 3:
        popstorage = ChodeCoreList.pop()
        popstorageA = popstorage + "a"
        popstorageB = popstorage + "b"
        popstorageC = popstorage + "c"
        ChodeCoreList.append(popstorageA)
        ChodeCoreList.append(popstorageB)
        ChodeCoreList.append(popstorageC)
    print(ChodeCoreList.pop())
