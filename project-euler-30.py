answer = 0

for num in range(2,1000001):
    if num == sum(int(R)**5 for R in str(num)):
        answer += num

print(answer)
