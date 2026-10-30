for number in range(1,101):
    value = ''
    if(number%3 == 0 or number%5 == 0):
        if(number%3 == 0):
            value = 'Fizz'
        if(number%5 == 0):
            value = value + 'Buzz'
    else: 
        value = number
    print(value)
    