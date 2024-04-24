# This adventure game shows a child looking for
# something fun to do with his/her father

option1 = 'hunting'
option2 = 'fishing'
option3 = 'night'
option4 = 'day'
option5 = 'boat'
option6 = 'shore'

name = input('Please enter your name: ')
print()
print(f'Hi {name.capitalize()}, welcome to the adventure game!\n'
      f'In this game, your options are the capitalized words.')
print()
print(f'Imagine having to do something fun with your dad,\n'
      f'what would you choose, HUNTING or FISHING? ')
choice1 = input('Enter your choice: ')
if choice1.lower() == option1:
    print()
    print(f'{option1.capitalize()} is a good choice!\n'
          f'Would you like DAY hunting and NIGHT hunting? ')
    print()
    choice2 = input('Enter you choice: ')
    print('Good choice!')
    print()
    print('End of game.')
elif choice1.lower() == option2:
    print()
    print(f'{option2.capitalize()} is a good choice!\n'
          f'Now choose between BOAT fishing and SHORE fishing: ')
    print()
    choice3 = input('Enter your choice: ')
    print('Good choice!')
    print()
    print('End of game. ')
elif choice1.lower() != option1 or option2:
    print('Wrong choice, try again! ')
else:
    print('Game over! ')
