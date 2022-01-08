total = 0
Next = 1
Prev = 1
PrevPrev = 1
while True:
    Next = Prev + PrevPrev
    if Next > 4000000:
        break
    if Next % 2 == 0:
        total = total + Next
    PrevPrev = Prev
    Prev = Next
    
print(total)

