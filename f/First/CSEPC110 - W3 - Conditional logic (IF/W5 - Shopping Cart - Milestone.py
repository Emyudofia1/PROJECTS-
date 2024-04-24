# shopping cart milestone project

print('Welcome to the shopping cart Program!')
print()
cart = []
item = ''
menu = ['Add item', 'View Cart', 'Remove Item', 'Compute Total', 'Quit']
print('Please select one of the following: ')
for i in range(len(menu)):
    item = menu[i]
    i += 1
    print(f'{i}. {item}')
action = int(input('Please enter an action: '))

while action != 2:
    if action == 1:
        item = input('What item would you like to add? ')
        cart.append(item)
        print(f"'{item.capitalize()}' has been added to the cart. ")
        print()
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: '))

while action != 3:
    if action == 2:
        print('Your shopping cart contains the following items: ')
        for i in range(len(cart)):
            item = cart[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        print()
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: '))
        if action == 5:
            print('Thank you. Goodbye.')





