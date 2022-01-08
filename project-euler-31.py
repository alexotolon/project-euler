coins = [1,2,5,10,20,50,100,200]

answer = 0

def next_node (value,target):
    global answer
    if target == 0 or value == 0:
        answer += 1
        return
    for p in range((target//coins[value])+1):
        next_node(value - 1,target - p*coins[value])

next_node(len(coins) - 1, 200)
print(answer)
