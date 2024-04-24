
secret_word = 'mosiah'
guess = ' '
print('Welcome to this word guessing game! ')
print()
keep_playing = 'yes'

while keep_playing == 'yes':
    user_input = input('What is your guess? ')

    guess_count = 0

    guess = ' '
    while guess.lower() != secret_word:
        guess_count = guess_count + 1
        if guess.lower() != secret_word:
            print('Your guess is incorrect')
            guess = (input('What is your guess? '))

    else:
        if guess.lower() == secret_word:
            print('Congratulations! You guessed it!')
    print(f'It took you {guess_count} guesses.')
    keep_playing = input('Would you like to keep playing (yes/no)? ')
print('Thank you for playing. Goodbye!')
