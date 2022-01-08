import math

Primemrory = {1: "It's neither"}

largestprimecount = 0

answer = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        xtra_long = "n*n + a*n + b"
        #xtra_long = input("(Test) what formula should I determine how may primes it can consecutavly produce? ")

        primecount = 0

        for n in range(1000):
            exec("x = " + xtra_long)
        
            if x > 0:    
                try:
                    Primemrory[x]
                except:
                    other_Primemrory = False
                    for I in range(2,math.floor(math.sqrt(x)) + 1):
                        if x % I == 0:
                            #print("It's a composite")
                            Primemrory[x] = "It's a composite"
                            other_Primemrory = True
                            break

                    if not other_Primemrory:
                        #print("It's a prime")
                        Primemrory[x] = "It's a prime"

            try:
                if not Primemrory[x] == "It's a prime":
                    break
                else:
                    primecount += 1
            except:
                break
           
        if primecount > largestprimecount:
            largestprimecount = primecount
            answer = a*b
print(answer)
