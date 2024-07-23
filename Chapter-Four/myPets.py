myPets = ['Spike', 'Benji', 'Dag']

print('Enter a pet name: ')
name = input()

if name not in myPets:
    print(f'I dont have a pet named {name}')
else:
    print(f'{name} is my pet.')