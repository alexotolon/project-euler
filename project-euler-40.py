def D(n):
    gary = 0
    larry = ""
    while (len(larry) < n):
        gary += 1
        larry += str(gary)
    return int(larry[n - 1])

print(D(1) * D(10) * D(100) * D(1000) * D(10000) * D(100000) * D(1000000))
