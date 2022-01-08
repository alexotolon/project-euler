def rev(S):

    newS = ""
   
    for L in S:

        newS = L + newS

    return newS


for L in range(100,1000):
    for N in range(100,1000):
        new = rev(str(L*N))
        if new == str(L*N):
            print(new)
            







