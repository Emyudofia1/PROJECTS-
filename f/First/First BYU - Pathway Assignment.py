# print('Hello world')

'''
color = input('What is your favorite color? ')
# print('Your favorite color is ' + color)
print('Your favorite color is')
print(color)
'''

'''
first_name = 'Emediong'
last_name= 'Udofia'
print('Udofia, ' + first_name + ' ' + last_name)
'''

'''
sentence = 'The dog is named Sammy'
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.count('a'))
'''

'''
first_name = input('What is your first name: ')
last_name = input('WHat is your last name: ')
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())
'''

''''
first_name = input('Please enter you first name: ')
last_name = input('Please enter your last name: ')
print('Hello ' + first_name.capitalize() + ' ' + last_name.capitalize())
'''

'''
first_name = 'Emedion'
last_name = 'Udofia'
# output = 'Hello, ' + first_name + last_name
# output = 'Hello, {} {}'.format(first_name, last_name)
# output = 'Hello, {0} {1}'.format(first_name, last_name)
output = f'Hello, {first_name} {last_name}'
print(output)
'''

'''
words = 'the cat in the hat'
print(words.capitalize())
print(words.title())
print(words.upper())
print(words.lower())
print(words.count("t"))
'''

# Practice formatting string


'''
print('Please enter the following details: ')

# This prints a blank line
print()

first = input('First name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')

# Ask for additional information
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
month = input('Starting month: ')
training = input('Completed additional training? ')

print('\nThe ID Card is:')
print('_____________________________________________')
print(f'{last.upper()}, {first.capitalize()}')
print(job_title.title())
print(f'ID: {id_number}')
print()
print(email.lower())
print(phone)
print()
print(f'Hair: {hair_color:15} Eyes: {eye_color}')
print(f'Month: {month:14} Training: {training}')
print('_____________________________________________')
'''


# Poject: Clever Stories

print('Please enter the following: ')

# This prints a blank line
print()

adjective = input('Enter an adjective: ')
animal = input('Enter any animal: ')
verb1 = input('Please enter a verb: ')
exclamation = input('Please enter an exclamation: ')
verb2 = input('Enter another verb: ')
verb3 = input('Another verb: ')

# Ask for additional information
# hair_color = input('Hair color: ')
#eye_color = input('Eye color: ')
# month = input('Starting month: ')
# training = input('Completed additional training? ')


print('\nYour story is:')
print()
print(f'The other day, I was really in trouble. It all started when I saw a very \n'
      f'{adjective} {animal} {verb1} down the hallway. {exclamation}! I yelled. \n'
      f'But all I could think to do was to {verb2} over and over. Miraculously, \n'
      f'that caused it to stop, but not before I saw it tried to {verb3} \nright before my family.')
# I am adding some finesse to the story
print(f'Then my mom shouted, {exclamation}! {animal}s cannot {verb1} right? \n'
      f'With his really thick voice my dad replied, I have seen it {verb1} before. \n'
      f'No dad, said my younger brother. Research has shown that {animal}s cannot {verb1}, \n'
      f'they can only {verb3}. ')
# print(job_title.title())
# print(f'ID: {id_number}')
# print()
# print(email.lower())
# print(phone)
# print()
# print(f'Hair: {hair_color:15} Eyes: {eye_color}')
# print(f'Month: {month:14} Training: {training}')
# print('_____________________________________________')