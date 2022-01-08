answer = 0

for n in range(1000001):
    if str(n) == str(n)[::-1] and bin(n)[2:] == bin(n)[:1:-1]:
        answer += n

print(answer)
