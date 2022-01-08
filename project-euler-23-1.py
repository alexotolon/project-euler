the_list = []

for t in range (1,28124):
    abundancy = 0
    for lessT in range (1,t):
        if t % lessT == 0:
            abundancy += lessT
    if abundancy > t:
        the_list.append(t)

print(the_list)
