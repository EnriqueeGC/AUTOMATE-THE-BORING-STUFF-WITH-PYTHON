# When used in conditions, 0, 0.0, and '' (empty string) are considered False, while all other values are considered True.

name = ''

while not name: # This is the same as while name == '':
    print('Enter your name:')
    name = input()

print('How many guest will you have?')
numOfGuests = int(input())

if numOfGuests: # This is the same as if numOfGuests != 0:
    print('Be sure to have enough room for all your guests.')
print('Done')