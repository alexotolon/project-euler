total = 0

number = 1
while number < 1000:
    if number % 3 == 0 or number % 5 == 0:
        total = total + number
    number = number+1
print("The answer is " + str(total))
