def D(a):
     return sum ([(A if a % A == 0 else 0) for A in range(1,a)])

print (sum ([(n if D(D(n)) == n and D(n) != n else 0) for n in range(1,10001)]))
