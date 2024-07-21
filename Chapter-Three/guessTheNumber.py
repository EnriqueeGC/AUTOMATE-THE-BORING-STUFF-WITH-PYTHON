import random

secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

for i in range(1, 6):
    number = int(input('Guess the number: '))
    if number > secretNumber:
        print('Your number is too high.')
    elif number < secretNumber:
        print('Your number is too low.')
    else:
        break

if secretNumber == number:
    print(f'Good Job! You guessed my number in {i} guesses.')
else:
    print(f'You lost, the number was {secretNumber}')