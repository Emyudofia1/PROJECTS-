# This adventure game shows a child looking for something fun to do with his/her father
# I gave the game to a counselor in our ward relief society presidency to play,
# after playing she asked, did you write this code by yourself? I answered yes, and
# she was so amazed that I could design that game all by myself within
# just 3 weeks of learning how to write programs

option1 = 'hunting'
option2 = 'fishing'
option3 = 'night'
option4 = 'day'
option5 = 'boat'
option6 = 'shore'
option7 = 'bow'
option8 = 'rifle'
option9 = 'spear'
option10 = 'machete'
option11 = 'diving'
option12 = 'netting'
option13 = 'trap'
option14 = 'angling'
option15 = 'hand'
option16 = 'bare hand'

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
          f'Would you like DAY hunting or NIGHT hunting? ')
    print()
    choice2 = input('Enter you choice: ')
    if choice2.lower() == option3:
        print()
        print(f'{option3.capitalize()} hunting is a good choice!\n'
              f'Would you like to hunt with a BOW, a RIFLE or BARE HAND? ')
        print()
        choice3 = input('Enter your choice: ')
        if choice3.lower() == option7:
            print('Good choice, happy hunting! ')
        elif choice3.lower() == option8:
            print('Good choice, happy hunting! ')
        if choice3.lower() == option16:
            print(f'Oh no {name.capitalize()}! It is not safe to hunt with bare hands at night. ')
        else:
            if choice3.lower() != option7 or option8:
                print('Wrong choice, try again. ')
            else:
                print('End of game')
    elif choice2.lower() == option4:
        print()
        print(f'{option4.capitalize()} hunting is a good choice!\n'
              f'Would you like to hunt with a SPEAR or a MACHETE? ')
        print()
        choice4 = input('Enter your choice: ')
        if choice4.lower() == option9:
            print('Good choice, happy hunting! ')
        elif choice4.lower() == option10:
            print('Good choice, happy hunting! ')
        else:
            print('Wrong choice, try again. ')
    else:
        if choice2 != option3 or option4:
            print('Wrong choice, try again!')
else:
    if choice1.lower() == option2:
        print()
        print(f'{option2.capitalize()} is a good choice!\n'
              f'Would you like BOAT fishing, SHORE fishing or HAND fishing? ')
        print()
        choice5 = input('Enter you choice: ')
        if choice5.lower() == option5:
            print()
            print(f'{option5.capitalize()} fishing is a good choice!\n'
                  f'Would you like fishing by DIVING or NETTING? ')
            print()
            choice6 = input('Enter your choice: ')
            if choice6.lower() == option11:
                print('Good choice, happy fishing!')
            elif choice6.lower() == option12:
                print('Good choice, happy fishing!')
            else:
                print('Wrong choice, try again. ')
        else:
            if choice5.lower() == option6:
                print()
                print(f'{option6.capitalize()} fishing is a good choice!\n'
                      f'Would you like fishing with TRAP or ANGLING? ')
                print()
                choice7 = input('Enter your choice: ')
                if choice7.lower() == option13:
                    print('Good choice, happy fishing!')
                elif choice7.lower() == option14:
                    print('Good choice, happy fishing!')
                else:
                    print('Wrong choice, try again.')
            if choice5.lower() == option15:
                print(f'Oh dear {name.capitalize()}! You probably wont catch any fish while fishing with your hand.')
            else:
                print('Wrong choice, try again. ')
    else:
        print('Wrong choice, try again.')
        