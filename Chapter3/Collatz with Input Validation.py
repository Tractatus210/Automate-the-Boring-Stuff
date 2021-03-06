# (Implements the "collatz" sequence on any number input by the user,
# printing all values until the value 1 is reached.)
# Try and Except statements added to circumvent the ValueError raised
# if the int() function is passed a noninteger string.

import time

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return (3 * number) + 1

# The main program loop has been placed inside a function that uses recursion in the
# Except statement so that the user has a chance to enter an integer following an error,
# and in the Try statement to repeat the sequence with different integers.
def getAndShow():
    try:
        number = int(input('Enter a number: '))
        print(number)
        while True:
            number = collatz(number)
            print(number)
            if number == 1:
                time.sleep(1)
                getAndShow()

    except ValueError:
        time.sleep(1)
        print('Please enter an integer')
        time.sleep(1)
        getAndShow()

getAndShow()
