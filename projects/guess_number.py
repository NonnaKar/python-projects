import random

def guess(x):
    random_number = random.randint(1, x)
    num = 0
    while num != random_number:
        num = int(input(f'Guess a number between 1 and {x}: '))
        if num < random_number:
            print('Sorry, guess again. Too low.')
        elif num > random_number:
            print('Sorry, guess again. Too hight.')

    print(f'Yay, congrats. You have guessted the number {random_number} correctly!!!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            num = random.randint(low, high)
        else:
            num = low # could also be high b/c low = high
        feedback = input(f'Is {num} too high (H), too low(L), or correct (C)?').lower()
        if feedback == 'h':
            high = num - 1
        if feedback == 'l':
            low = num + 1

    print(f'Yay! The computer guessed your number, {num}, correctly!')

# guess(10)
computer_guess(1000000)