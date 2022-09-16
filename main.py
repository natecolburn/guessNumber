import random

def guess(x):
    random_number = random.randint(1 , x)
    guess = 0
    while guess != random_number:
       guess = int(input(f'Enter a number between 1 and {x}: '))
       if guess < random_number:
           print('incorrect: Number is to low')
       elif guess > random_number:
           print('incorrect: Number is to high')
    print(f'Correct: {random_number} was the correct answer')


guess(10)



