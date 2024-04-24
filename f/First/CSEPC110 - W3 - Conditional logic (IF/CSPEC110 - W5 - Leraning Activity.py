# Working with lists
"""
clients = []
new_client = ''
while new_client != 'quit':
    new_client = input('What is the name of your client? ')
    clients.append(new_client.capitalize())
for client in clients:
    print(clients)
"""

"""
books = []

books.append('1 Nephi')
books.append('2 Nephi')
books.append('Jacob')
books.append('Enos')

print('Your books are:')

for book in books:
    print(book)
"""
"""
receipts = [21.24, 18.50, 4.99, 21.75]
running_total = 0

for receipt in receipts:
#    running_total = running_total + receipt
    running_total += receipt  # this line of code works the same as the one above

print(f'The total is: {running_total:.2f}')
"""
"""
friends = []
name = ''
while name != 'end':
    name = input('What is the name of your friend? ')
    if name != 'end':
        friends.append(name.capitalize())

print('Your friends are:')

for friend in friends:
    print(friend)
"""

"""
print('Please enter the items of the shopping list (type: quit to finish):')

shopping_list = []
item = ''

while item != 'quit':
    item = input('Item: ')

    if item != 'quit':
        shopping_list.append(item.capitalize())
print('\nThe shopping list is: ')
for item in shopping_list:
    print(item)

print('\nThe shopping list with indexes is:')
for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')
print()
index = int(input('Which item would you like to change? '))
new_item = input('What is the new item? ')

shopping_list[index] = new_item.capitalize()

for i in range(len(shopping_list)):
    item = shopping_list[i]
    print(f'{i}. {item}')
"""
numbers = []
running_total = 0
number = -1
print("Enter a list of numbers, type 0 when you are done.")
while number != 0:
    number = int(input('Enter a number: '))
    if number != 0:
        numbers.append(number)
sum = 0

for number in numbers:
    sum += number
print(f'The total is: {sum:.2f}')

count = len(numbers)
average = sum / count
print(f'The average is: {average}')

best_so_far = -1
for number in numbers:
    if number > best_so_far:
        best_so_far = number
print(f'The largest number is: {best_so_far}')

smallest_so_far = 99999999999
for number in numbers:
    # if number > 0 and number < smallest_so_far:
    if 0 < number < smallest_so_far:
        smallest_so_far = number
print(f'The smallest number is: {smallest_so_far}')

sorted_list = sorted(numbers)
print('The sorted list is: ')
for number in sorted_list:
    print(number)

"""
    # To compute total amount
    # while action != 5:
    if action == 4:
        sum = 0
        for price in prices:
            sum += price
        print(f'The total price of items in your shopping cart is: {sum:.2f}')
        print()
    print('Please select one of the following: ')
    for i in range(len(menu)):
        item = menu[i]
        i += 1
        print(f'{i}. {item.capitalize()}')
    action = int(input('Please enter an action: '))

    # To remove item from the list
    if action == 3:
        index = int(input('Which item would you like to remove? '))
        cart[i] = index
        for i in range(len(cart)):
            cart.pop(2)

    else:
        print('Sorry, you have not added items yet.')
        print('Please select one of the following: ')
        for i in range(len(menu)):
            item = menu[i]
            i += 1
            print(f'{i}. {item.capitalize()}')
        action = int(input('Please enter an action: ')



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
if action == 5:
    print('Thank you. Goodbye.')
"""
