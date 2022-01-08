knownNums = { 1 : 1, 2 : 1}

def fib(i):
    if i not in knownNums:
        knownNums[i] = fib(i-1) + fib(i-2)
    return knownNums[i]

#print(fib(int(input("what num in the fibonacci sequence should I say? "))))

b = 3

while True:
    if len(str(fib(b))) == 1000:
        print(fib(b))
        break
    b += 1
