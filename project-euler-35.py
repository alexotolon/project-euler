prims = range(2,1000000)

for length_along in range(len(prims)):
    if length_along == len(prims):
        break
    primfocus = prims[length_along]
    prims = [primaybe for primaybe in prims if primaybe % primfocus != 0 or primaybe == primfocus]
#print(prims)
