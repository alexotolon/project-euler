answer = '123456789'

for this in range(1,10000):
    concatanation = str(this)
    good = True
    multiplier = 1
    while len(concatanation) < 9:
        multiplier += 1
        concatanation += str(this *multiplier)
        if len(concatanation) != len(set(concatanation)) or "0" in concatanation:
            good = False
            break
    if good and int(concatanation) > int(answer):
        answer = concatanation
print(answer)
