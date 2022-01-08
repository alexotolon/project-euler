primelist = [ int(prime) for prime in (open("complete and cool prim composite.txt")).read().split(", ") ]

previousEntries = [False]*4

currentEntry = 4

def halfone(f):
    factors = 0
    for e in primelist:
        able = False
        while f % e == 0:
            f //= e
            able = True
        if able:
            factors += 1
        if f == 1:
            break
    return factors == 4
    
while False in previousEntries:
    currentEntry += 1
    previousEntries.append(halfone(currentEntry))
    previousEntries.pop(0)

print(currentEntry - 3)
