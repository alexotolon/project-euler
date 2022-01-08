import math

Answer = 0

words = open("poforto_words.txt")

usable_words = words.read().split(",")

for z in usable_words:
    r = 0
    for z2 in z:
        if z2 != '"':
            r += ord(z2) - 64
    if((math.sqrt(1+8 * r) - 1) / 2) % 1 == 0.0 : 
        Answer += 1

#usable_names

print(str(Answer))
