Total = 0
nums = ['',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten',
        'eleven',
        'twelve',
        'thirteen',
        'fourteen',
        'fifteen',
        'sixteen',
        'seventeen',
        'eighteen',
        'nineteen']

tens = ['',
        'ten',
        'twenty',
        'thirty',
        'forty',
        'fifty',
        'sixty',
        'seventy',
        'eighty',
        'ninety']

def printNum(x):
    if x < 20:
        print(nums[x])
    elif x < 100:
        print(tens[x //10] + "-" + nums[x %10])
    elif x < 1000:
        print(nums[x //100] + " hundred and", end = " ")
        y = x %100
        printNum(y)
    else:
        print("one thousand")

for x in range(1001):
    printNum(x)
