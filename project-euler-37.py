primeset = set((open("complete and cool prim composite.txt")).read().split(", "))
primeset.add("")

answer = 0

for prime in primeset:
    good = True
    prime2 = prime
    prime3 = prime
    for LR in range(len(prime2)):
        prime2 = prime2[1:]
        if not prime2 in primeset:
            good = False
    for RL in range(len(prime3)):
        prime3 = prime3[:-1]
        if not prime3 in primeset:
            good = False
    if good and prime != "":
        answer += int(prime)
print(answer - 17)
