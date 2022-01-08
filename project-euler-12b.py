T = 1
i = 1

while True:
    i += 1
    T += i 

    divisors = 0
    for n in range(1,T + 1):
        if T % n == 0:
            divisors = divisors + 1

    if i % 10 == 0:
        print("trying " + str(T))
        
    if divisors > 500:
        print("the answer is" + str(T))
        break
