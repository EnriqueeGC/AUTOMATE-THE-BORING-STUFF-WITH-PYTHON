import random

phrases = [
    'It is certain.',
    'It is decidedly so.',
    'Yes.',
    'Repli hazy try again.',
    'Ask again later.',
    'Concentrate and ask again.',
    'My reply is no.',
    'Outlook not so good.',
    'Very doubtful.'
]

print(phrases[random.randint(0, len(phrases) - 1)])