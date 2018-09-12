numbers = {}


def returnDict(): 
    for number in range(1, 16):
        numbers[number] = number**2
    return numbers

print(returnDict())
