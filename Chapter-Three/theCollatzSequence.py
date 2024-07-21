# Write a function named collatz() that has one parameter named number. If number is even, then the collatz()
#  should print number // 2 and return this value. If the number is odd, then the collatz() should print and return
#  3 * number + 1.

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

try:
    number = int(input('Enter a number: '))
    while number:
        number = collatz(number)
        print(number)
        if number == 1:
            break
except ValueError:
    print('Please, enter a correct number.')