import random

target = random.randint(1,100)

while True:
    a= int(input('Guess a number'))

    if a==target:
        print('You won')
        break

    elif a<target:
        print('Number is little less')

    else:
        print('Number is little high')

print('Thanks for playing the game')


