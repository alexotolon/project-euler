p = 1

total = 0

names = open("names.txt")

usable_names = names.read().split(",")

usable_names.sort()

for z in usable_names:
    r = 0
    for z2 in z:
        if z2 != '"':
            r += ord(z2) - 64
    total += r*p
    p += 1

#usable_names

print(str(total))
