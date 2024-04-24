
# I have added  creativity where I asked the user if they want to continue playing the game.
# If the response is yes, the games goes on and if the response is no the game ends.
secret_word = 'mosiah'
guess = ' '
print('Welcome to this word guessing game! ')
print()
print('Your hint is: ', end='')
for i in range(len(secret_word)):
    print('_ ', end='')
print()
keep_playing = 'yes'

while keep_playing == 'yes':
    guess = input('What is your guess? ')

    guess_count = 0
    while guess.lower() != secret_word:
        if len(secret_word) > len(guess) or len(secret_word) < len(guess):
            print('Sorry, your guess must have the same number of letters as the secret word.')
            guess = input('What is your guess? ')
        else:
            guess_count = guess_count + 1
            print('Your hint is: ', end='')
            for i in range(len(guess)):
                if guess[i] == secret_word[i]:
                    print(guess[i].capitalize(), end=' ')
                elif guess[i] in secret_word:
                    print(guess[i].lower(), end=' ')
                else:
                    print('_', end=' ')
            print()
            guess = input('What is your guess? ')
    else:
        if guess.lower() == secret_word:
            print('Congratulations! You guessed it!')
    print(f'It took you {guess_count} guesses.')
    keep_playing = input('Would you like to keep playing (yes/no)? ')
print('Thank you for playing. Goodbye!')

