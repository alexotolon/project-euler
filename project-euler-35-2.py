primeset = set((open("complete and cool prim composite.txt")).read().split(", "))

answer = 0

#print(len(primeset))
for prime in primeset:
    #o = answer
    answer += .01
    for n in range(1,len(prime)):
        firstdig = prime[0]
        prime = prime[1:] + firstdig
        if prime in primeset:
            answer += 1/(len(prime) - 1)
    #if int(answer) == o + 1:
        #print(prime)
    answer = int(answer)
#print("------")
print(answer)
