"""
tax = float(input('What is the tax rate? '))
while tax < 0:
    print('Sorry, tax cannot be negative. ')
    tax = float(input('What the tax rate? '))
print(f'The tax is ${tax:.2f}')
"""
"""
number = 2
while number < 10:
    number = int(input('What is the number? '))
print('Done with the loop')
"""
"""
number = int(input('Please enter a positive number: '))
while number < 0:
    print('Sorry, that is a negative number. Try again')
    number = int(input('Please enter a positive number: '))
print(f'The number is: {number}')
"""
"""
candy = input('May I have Candy? ')
while candy == 'no':
    candy = input('May I have Candy? ')
print('Thank you! ')
"""

"""
answer = " "
while answer != 'yes':
    answer = input('May I have Candy? ')
print('Thank you! ')
"""

"""
people = ['Paul', 'Mary']
# for name in people:
#    print(name)

index = 0
while index < len(people):
    print(people[index])
    index = index + 1
"""

"""
items =['crayon', 'scissors', 'paper', 'glitter glue', 'markers', 'pens']
for item in items:
    print(f'The item is: {item}')


# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers in range(10)
for number in range(10):
    print(number)
"""

"""
for i in range(100, 200,):  # This prints serially
    print(i)

for i in range(100, 200, 10):  # this prints in groups of 10s
    print(i)
"""

"""
for i in range(5):
    print(i)
print()
for i in range(5):
    print(i)
    for j in range(10, 13):
        print(f'--{j}')
"""

"""
colors = ['red', 'blue', 'green', 'yellow']
for color in colors:
    print(color)
print()
for i in range(1, 9):
    print(i)
print()
for i in range(2, 21, 2):
    print(i)
"""

"""
# looping through strings
first_name = 'Brigham'
for letter in first_name:
    print(f'The letter is: {letter}')

# Accessing letters by position
first_name = 'Brigham'
fourth_letter = first_name[3]
print(fourth_letter)
"""

""""
# iterating through each letter using an index
word = 'book'  # this prints only the index of the word
number_of_letters = 4
for index in range(number_of_letters):
    print(index)
print()
word = 'book'  # this prints the index and the corresponding letter of the word
number_of_letters = 4
for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')
"""

# finding the length of strings

# dog_name = input('What is the name of your dog? ')
# letter_count = len(dog_name)
# print(f'The name of your dog has {letter_count} letters.')
"""
word = 'book'  # this uses the len function to determine the index and the corresponding letter of the word
number_of_letters = len(word)
for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')

# this takes a word from the user, determine the index and the corresponding letter of the word
word = input('Enter a word: ')  
number_of_letters = len(word)
for index in range(number_of_letters):
    letter = word[index]
    print(f'Index: {index} Letter: {letter}')
print(f'Your word has {number_of_letters} letters as shown above')
"""

"""
# using the enumerate function
first_name = 'Brigham'
for i, letter in enumerate(first_name):
    print(f'The letter {letter} is at position {i}')
print()
    
print('This is line one.', end='')
print('This is line two')
"""

"""
word = 'Commitment'
fav_letter = input('What is your favorite letter? ')
# for letter in word:
#    if letter.lower() == fav_letter.lower():
#        print(letter.upper(), end="")
#    else:
#        print(letter.lower(), end="")
#print()

for letter in word:
    if letter.lower() == fav_letter.lower():
        print("_", end="")
    else:
        print(letter.lower(), end="")
print()
"""

# value = 20
# while value < 20:
#    value = value + 1
# print(value)

""""
animal = 'rabbit'
while animal == 'dog':
    print("a")
    animal = "cat"
    print("b")
print("c")
"""

""""
import random
magic_number = random.randint(1, 100)
user_input = int(input('What is the magic number? '))
guess = -1

while guess != magic_number:
    guess = int(input('What is your guess? '))
    if guess < magic_number:
        print('Higher ')
    elif guess > magic_number:
        print('Lower')
    else:
        print('You guessed it!')
"""
"""
keep_playing = 'yes'

while keep_playing == 'yes':
    magic_number = random.randint(1, 100)

    guess_count = 0

    guess = -1

    while guess != magic_number:
        guess_count = guess_count + 1
        guess = int(input('What is your guess? '))
        if guess < magic_number:
            print('Higher ')
        elif guess > magic_number:
            print('Lower')
        else:
            print('You guessed it!')
    print(f'It took you {guess_count} guesses.')
    keep_playing = input('Would you like to keep playing (yes/no)? ')
print('Thank you for playing. Goodbye!')

"""
import random

def choose_word():
    word_list = ["apple", "banana", "orange", "grape", "peach"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def wordle_game():
    max_attempts = 6
    word_to_guess = choose_word()
    guessed_letters = set()

    print("Welcome to Wordle! Try to guess the word.")

    for attempt in range(max_attempts):
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"\nAttempt {attempt + 1}/{max_attempts}")
        print(current_display)

        guess = input("Enter your guess (single letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        guessed_letters.add(guess)

        if set(word_to_guess) == guessed_letters:
            print(f"Congratulations! You guessed the word: {word_to_guess}")
            break

    else:
        print(f"Sorry, you ran out of attempts. The word was: {word_to_guess}")

# if __name__ == "__main__":
#    wordle_game()
