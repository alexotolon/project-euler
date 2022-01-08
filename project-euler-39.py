argmax = 0

Max = 0

for p in range(1001):
    print(p)
    triangles = 0
    for a in range(1,p - 1):
        for b in range(1,p - a):
            if (p - a - b)**2 == a**2 + b**2:
                triangles += 1
    if triangles > Max:
        argmax = p
        Max = triangles

print(argmax)
