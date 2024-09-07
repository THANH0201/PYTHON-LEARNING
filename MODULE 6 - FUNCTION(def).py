#NAME: THANH HONG THI NGUYEN
#DATE: 06-SEP-2024
#MODULE 6: FUNCTION
import random
import math

"""
#EXERCISE 1:
# Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters.
# Write a main program that rolls the dice until the result is 6. The main program should print out the result of
# each roll.

def dice_roll():
    return random.randint(1,6)
while True:
    dice = dice_roll()
    print(f"The dice point is: {dice}")
    if dice == 6:
        break

#EXERCISE 2:
# Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified
# function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that
# the dice rolling in the main program continues until the program gets the maximum number on the dice, which
# is asked from the user at the beginning

def dice_roll(side):
    return random.randint(1,side)
side = int(input("Enter the number of sides: "))
while True:
    dice = dice_roll(side)
    print(f"The dice point is: {dice}")
    if dice == side:
        break

#EXERCISE 3:
# Write a function that gets the quantity of gasoline in American gallons and returns the number converted to
# litres. Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a negative
# value.
def convert_to_litre(gallon):
    return 3.785412 * gallon
while True:
    gallon = int(input("Enter the volume in gallon: "))
    if gallon >= 0:
        print(f"{gallon} gallons equals {convert_to_litre(gallon)} litres")
    else:
        print(f"The volume in gallon must be greater than 0")
        break

#EXERCISE 4:
# Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in
# the list. For testing, write a main program where you create a list, call the function, and print out the value it
# returned

def sum(num_list):
    total = 0
    for i in num_list:
        total += i
    return total
num_list = []
for number in range(10):
    num_list.append(random.randint(1,10))
print(f"This list contains {num_list}")

for i in range(len(num_list)):
    print(num_list[i], end= " ")
    
print(f"\nThe sum of num_list is {sum(num_list)}")

#2/ USER CREATE NUMBER LIST
def sum(num_list):
    total = 0
    for i in num_list:
        total += i
    return total
num_list = []
i = 0
while True:
    user_number = input("Enter the numbers, enter empty string to exit:")
    if user_number != " ":
        number = float(user_number) # type of number(can change)
        i = i + 1
    else:
        break
    num_list.append(number)
print(f"This list contains {num_list}")
print(f"The sum of your number list is {sum(num_list)}")

#EXERCISE 5:
# Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise
# the same as the original list except that all uneven numbers have been removed. For testing, write a main program
# where you create a list, call the function, and then print out both the original as well as the cut-down list

def oven(int_list):
    oven_list = []
    for i in int_list:
        if i % 2 == 0:
            oven_list.append(i)
    return oven_list

def print_list(message, int_list):
    print(message, end=" ")
    for i in range(len(int_list)):
        print(int_list[i], end=" ")

vd_list = []
for n in range(10):
    vd_list.append(random.randint(1, 10))
print_list("Original list", vd_list)
new_list = oven(vd_list)
print_list("\nThis new list contains", new_list)


#EXERCISE 6:
# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of
# the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program
# asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for
# money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

def calculate(d,price):
    return price/((math.pi*(d/2)**2)/100)
def compare(pizza1,pizza2):
    if pizza1 < pizza2:
        print("Chose pizza 1")
    else:
        print("Chose pizza 2")

d1= float(input("Enter the diameter of first pizza(in centimeters): "))
price1 = float(input("Enter the price of first pizza(in euros): "))
d2= float(input("Enter the diameter of second pizza(in centimeters): "))
price2 = float(input("Enter the price of second pizza(in euros): "))
pizza1 = calculate(d1,price1)
pizza2 = calculate(d2,price2)
compare(pizza1,pizza2)
"""








