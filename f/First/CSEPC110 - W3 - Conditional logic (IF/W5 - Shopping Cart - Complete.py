# shopping cart milestone project

print('Welcome to the shopping cart Program!')
print()
cart = []
prices = []
item = ''
price = -1
running_total = 0
menu = ['Add item', 'View Cart', 'Remove Item', 'Compute Total', 'Quit']
print('Please select one of the following: ')
for i in range(len(menu)):
    item = menu[i]
    i += 1
    print(f'{i}. {item}')
action = int(input('Please enter an action: '))

# adding items to cart

while action != 5:
    if action == 1:
        item = input('What item would you like to add? ')
        cart.append(item)
        price = float(input('Enter the price: '))
        prices.append(price)
        print(f"'{item.capitalize()}' has been added to the cart. ")
        print()
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: '))


    # Viewing items in the cart
# while action != 3:
    if action == 2:
        print('Your shopping cart contains the following items: ')
        for i in range(len(cart)):
            item = cart[i]
            price = prices[i]
            i += 1
            print(f'{i}. {item.capitalize()} - ${price:.2f}')
        print()
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: '))

    if action == 4:
        sum = 0
        for price in prices:
            sum += price
        print(f'The total price of items in your shopping cart is: ${sum:.2f}')
        print()
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: '))

    if action == 3:
        index = int(input('Which item would you like to remove? '))
        index -= 1
        cart.pop(index)
        prices.pop(index)
        print('Item has been removed. ')
        print()
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: '))

print('Thank you for shopping with us, goodbye! ')
