answer = 0

for p in range(1000,10000):
    for m1 in range(1,100):
        fulfillednums = str(p) + str(m1) + str(p/m1)
        if [fulfillednums.count(str(dig)) for dig in range(1,10)] == [1,1,1,1,1,1,1,1,1] and fulfillednums[-1] == "0":
            answer += p
            print(p,m1,p/m1)
            break

print(answer)
