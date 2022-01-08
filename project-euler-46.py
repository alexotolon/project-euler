primeset = { int(prime) for prime in (open("complete and cool prim composite.txt")).read().split(", ") }

for sl in range(3,1000001,2):
    brEak = False
    for n in range(0,sl):
        if sl - 2 * n ** 2 in primeset:
            brEak = True
            break
    if not brEak:
        print(sl)
