catNames = []

while True:
    print(f'Enter the name of cat {str(len(catNames) + 1)} (Or nothing to stop.): ')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]

print(f'The cat names are: ')
for name in catNames:
    print(f' {name}')