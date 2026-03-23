#!usr/bin/python3
#Make a magic 8 ball

import random

answers = [
    "It is certain",
    "It is decidedly so",
    "Without a doubt",
    "Yes - definitely",
    "You may rely on it",
    "As I see it, yes",
    "Most likely",
    "Outlook good",
    "Yes",
    "Signs points to yes",
    "Reply hazy, try again",
    "Ask again later",
    "Better not tell you now",
    "Cannot predict now",
    "Concentrate and ask again",
    "Don't count on it",
    "My reply is no",
    "My sources say no",
    "Outlook not so good",
    "Very doubtful"
]

print('  __  __          _____ _____ _____    ___  ')
print(' |  \/  |   /\   / ____|_   _/ ____|  / _ \ ')
print(' | \  / |  /  \ | |  __  | || |      | (_) |')
print(' | |\/| | / /\ \| | |_ | | || |       > _ < ')
print(' | |  | |/ ____ \ |__| |_| || |____  | (_) |')
print(' |_|  |_/_/    \_\_____|_____\_____|  \___/ ')
print('')
print('')
print('')
print('Hello, I am the Magic 8 Ball, What is your name?')

name = input()
print('Hello ' + name)


def Magic8Ball():
    print('Ask me a question. ')
    input()
    print(answers[random.randint(0, len(answers)-1)] )
    print('I hope that helped!')
    
    