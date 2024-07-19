#This program says hello ands ask for my name.


print('Hello World!')
myName = input('What is your name?\n')

print('It is good to meet you, ' + myName)
print('The length of your name is: ', len(myName))

myAge = input('What is your age?\n')
print(f'You will be {str(int(myAge) + 1)} in a year.')