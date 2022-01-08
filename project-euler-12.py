T = 1
i = 1

while True:
    i += 1
    T += i 

    divisors = 0
    for n in range(1,T + 1):
        if T % n == 0:
            divisors = divisors + 1

    if divisors > 500:
        print (T)
