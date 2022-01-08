Mr_Hashtag = 20
while True:
    goodsofar = True
    for Div in range(1,21): 
        if Mr_Hashtag % Div != 0:
            goodsofar = False
            break
    if not goodsofar:
        Mr_Hashtag = Mr_Hashtag + 1   
    else:
        print(Mr_Hashtag)
    
    
    






    
