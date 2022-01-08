for n in range (10,100):
    for samedig in str(n):
        for diffdig in range(1,10):
            if n * diffdig == int(samedig + str(diffdig)) * int(str(n).replace(samedig,'',1)) and \
               samedig != "0" and int(samedig + str(diffdig)) > n:
                print(n)
                print(samedig + str(diffdig))
            if n * diffdig == int(str(diffdig) + samedig) * int(str(n).replace(samedig,'',1)) and \
               samedig != "0" and int(str(diffdig) + samedig) > n:
                print(n)
                print(str(diffdig) + samedig)
