Powers = set()

for a in range(2,101):
    for b in range(2,101):
        Powers.add(a**b)

print(len(Powers))
