def square(list):
    return [i ** 2 for i in list]


PE1 = sum(range(1,101))
PE1 = PE1*PE1


PE2 = square(range(1,101))
PE2 = sum(PE2)


print(PE1 - PE2)
