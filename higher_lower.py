import random

number = int(input("What should the answer be? "))
if number == -1:
    '''if they say "1",pick randomly.'''
    number = random.randrange(1, 101)
times = int(input("How many guesses? "))
while times != 0:
    '''using while loop to make sure the guesses' times is controlled.'''
    times -= 1
    guess_number = int(input("Guess a number: "))
    if guess_number == number:
        print("You win!")
        exit()
    elif guess_number < number:
        print("The number is higher than that.")
    elif guess_number > number:
        print("The number is lower than that.")
if times == 0:
    '''when the times run out, output the result.'''
    print("You lose; the number was", number)
