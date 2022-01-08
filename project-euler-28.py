answer = -3

for dst in range(1,1002,2):
    for arm in range(0,4):
        answer += dst**2 - dst*arm + arm

print(answer)
