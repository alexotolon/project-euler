import math

answer = 0

for n in range(10,1000000):
    if sum([math.factorial(int(dig)) for dig in str(n)]) == n:
        answer += n
    
