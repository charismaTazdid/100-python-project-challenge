import random


def guess(x):
    random_number = random.randint(1, x)

    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess A Number 1 to {x}: "))
        if guess < random_number:
            print('Sorry Guess again, too low.')
        elif guess > random_number:
            print("Sorry guess again! it's too high.")
    print(
        f'Ok! finally you guess it! Computer guess the {random_number}. Congratulation.')
guess(10)

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f"Is the number {guess} too high (h), too low (l),or correcet?(c)").lower()
        if feedback == 'h':
            high = guess - 1
        if feedback == 'l':
            low = guess + 1
    print(f"yoooo! The computer guess the number {guess} correctly!")


computer_guess(124)
