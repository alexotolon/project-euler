import math

rp = 144

Hrp = 0

while not (math.sqrt(1 + 8 * Hrp) - 1) % 2 + (math.sqrt(1 + 24 * Hrp) + 1) % 6 == 0:
    rp += 1
    Hrp = rp * (2 * rp - 1)

print(Hrp)
