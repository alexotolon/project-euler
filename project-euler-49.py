primeset = { int(prime) for prime in (open("complete and cool prim composite.txt")).read().split(", ") }

for i in range (1000,10001):
    if i in primeset:
        for j in range (11,(10001 - i) // 2):
            if i + j in primeset and i + j * 2 in primeset and sorted(str(i)) == sorted(str(i + j)) == sorted(str(i + j * 2)):
                print (str(i) + str(i + j) + str(i + j * 2))
