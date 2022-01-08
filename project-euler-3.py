#alpha version -- just working some ideas
#not final version
#crazy = 600851475143
crazy = 21

#first try to see if it's prime
testDivisor = 2
while testDivisor < crazy:
    if crazy % testDivisor == 0:
        print("Found a divisor!  It was " + str(testDivisor))
        break
    testDivisor = testDivisor+1
    #somehow test if crazy is divisible by testDivisor
    #if so, it's not a prime!
    #otherwise add one to testDivisor

#is it divisible by 2?
#is it divisible by 3?
#is it divisible by 4?
#is it divisible by 5?

    
#it was divisible by 71!!!!!!!!
