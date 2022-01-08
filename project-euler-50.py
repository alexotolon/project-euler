primeset = { int(prime) for prime in (open("complete and cool prim composite.txt")).read().split(", ") }

primelist = [ int(prime) for prime in (open("complete and cool prim composite.txt")).read().split(", ") ]

finale = 0

finale_counter = 0

starts = 0

for start in primelist:
    counter = 0
    starts += 1
    for new in primelist[starts:]:
        start += new
        counter += 1
        if start > 1000000:
            break
        if start in primeset and counter > finale_counter:
            finale = start
            finale_counter = counter

print(finale)
