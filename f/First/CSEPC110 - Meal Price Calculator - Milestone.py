# This program takes adults and children meal prices and computes the subtotal
# depending on the number of adults and children entered by the user

num1 = float(input("What is the price of a child's meal?: "))
num2 = float(input("What is the price of an adult's meal?: "))
number_of_children = int(input("How many children are there?: "))
Number_of_adult = int(input("How many adult are there?: "))
total_child_meal = (num1 * number_of_children)
total_adult_meal = (num2 * Number_of_adult)
sub_total = float((total_adult_meal + total_child_meal))
print()
print(f'Subtotal: ${sub_total}')

