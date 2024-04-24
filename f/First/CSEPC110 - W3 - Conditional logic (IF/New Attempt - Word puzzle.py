

secret_word = 'mosiah'
guess = ' '
print('Welcome to this word guessing game! ')
print()
print('Your hint is: ', end='')
for i in range(len(secret_word)):
    print('_', end='')
print()
keep_playing = 'yes'

while keep_playing == 'yes':
    user_input = input('What is your guess? ')

    guess_count = 0

    guess = ' '
    while guess.lower() != secret_word:
        guess_count = guess_count + 1
        if len(guess) < len(secret_word) or len(guess) < len(secret_word):
            print('Sorry, your guess must have the same number of letters as the secret word.')
            guess = input('What is your guess? ')
        else:
            print('Your hint is: ', end='')
            for i in range(len(guess)):
                if guess[i] == secret_word[i]:
                    print(guess[i].capitalize(), end='')
                elif guess[i] in secret_word:
                    print(guess[i].lower(), end='')
                else:
                    print('_', end='')
            print()
            guess = input('What is your guess? ')
    else:
        if guess.lower() == secret_word:
            print('Congratulations! You guessed it!')
    print(f'It took you {guess_count} guesses.')
    keep_playing = input('Would you like to keep playing (yes/no)? ')
print('Thank you for playing. Goodbye!')

