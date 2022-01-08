theMax = 1000
for a in range(0, theMax+1):
    for b in range(0, theMax-a+1):
        c = theMax-a-b
        if a**2+b**2==c**2:
            print(a*b*c)
