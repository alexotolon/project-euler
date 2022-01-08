FactorialAns = 1
Total = 0

for t in range(int(input("what number should I add the digits of it's factorial "))):
    FactorialAns *= t + 1

for n in str(FactorialAns):
    Total += int(n)

print(Total)
