# Write a program that ask for a name and password

while True:
    print('Who are you?')
    name = input()
    if name != 'Edgar': 
        continue
    print('Hello, Edgar, what is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')

