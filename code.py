def printFB(num):
    if num%5 == 0 and num%3 == 0:
        return 'FizzBuzz'
    elif num%5 == 0:
        return 'Buzz'
    elif num%3 == 0:
        return 'Fizz'
    else:
        return num

def print100FB():
    for num in range(100):
        if num%5 == 0 and num%3 == 0:
            print("FizzBuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num%3 == 0:
            print("Fizz")
        else:
            print(num)

print100FB()