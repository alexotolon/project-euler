TheAnswer = 0
TheAnswerLength = 0
for num in range(1,1000):
    ModHistory = [.1]
    while True:
        result = (ModHistory[-1] * 10) % num
        if result in ModHistory:
            break
        ModHistory.append(result)
    #print(len(ModHistory) - ModHistory.index(result))
    if len(ModHistory) - ModHistory.index(result) > TheAnswerLength:
        TheAnswerLength = len(ModHistory) - ModHistory.index(result)
        TheAnswer = num
print(TheAnswer)
