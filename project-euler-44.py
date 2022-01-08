import math

answer = 100000000000000000000000000000000

def IsPentagonal(p):
    if (math.sqrt(1 + 24 * p) + 1) % 6 == 0:
        return True
    else:
        return False
for j in range(1,10000):
    Pj = j * (3 * j - 1) / 2
    if j % 1000 == 0:
        print(j)
    for k in range(j,10000):
        Pk = k * (3 * k - 1) / 2
        if IsPentagonal(Pk - Pj) and IsPentagonal(Pk + Pj) and Pk - Pj < answer:
            answer = Pk - Pj
            print("wow," + str(answer) + " or something like that")
print(answer)
