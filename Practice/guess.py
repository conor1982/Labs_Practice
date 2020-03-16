import random
lower = 1
upper = 100
number = random.randint(lower, upper)
print(number)


max_guesses = 5
number_of_guesses = 5
print('Guess a number between:',lower,'and',upper)

while number_of_guesses >= 1:
    guess = int(input())
    number_of_guesses -= 1
    if guess != number:
        print(number_of_guesses,'guesses left')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))