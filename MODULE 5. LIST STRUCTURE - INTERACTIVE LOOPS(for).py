# THANH HONG THI NGUYEN
# DATE: 06-09-2024
# MODULE 5: LIST STRUCTURE- INTERACTIVE LOOPS (for)
import math
import random
"""
#EXERCISE 1
# Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the
# sum of the numbers. Use a `for` loop.
dice_sides =[]
user_dice = int(input("How many dices? "))
for roll in range(user_dice):
    #dice_side = random.randint(1, 6)
    #dice_sides.append(dice_side)
    dice_sides.append(random.randint(1, 6))
print(f"the sides of dice are: {dice_sides}")
sum_point = sum(dice_sides)
print(f"Total sides is:{sum_point}")

#EXERCISE 2
# Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the 
# program prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted 
# list items by using the `sort` method with the `reverse=True` argument

num_list = []
i = 0
while True:
    user_number = input("Enter the numbers, enter empty string to exit:")
    if user_number != " ":
        number = float(user_number)
        i = i + 1
    else:
        break
    num_list.append(number)

    for number in num_list:
        sort_greatest = sorted(num_list)
    print(f"The five greatest numbers sorted in descending is:{sort_greatest[0:5]}")

#EXERCISE 3:
# Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are
# number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
user_number = int(input("Enter an integer numbers: "))
i = 0
while True:
    if user_number % 2 == 0 and user_number != 2:  # drop oven number
        print(f"{user_number} is not a prime number.")
    elif user_number == 1 or user_number == 2:
        print(f"{user_number} is a prime number.")
    else:
        for number in range(3, 10, 2):
            # number = int(number)
            if user_number % number == 0:
                print(f"{user_number} is not prime number.")
                break
    if user_number % number != 0:
        print(f"{user_number} is a prime number.")

    user_number = int(input("Enter an integer numbers: "))
    i = i + 1

#EXERCISE 4:
# Write a program that asks the user to enter the names of five cities one by on (use a `for` loop for reading the names)
# and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input. Use a `for` loop for asking the names and a `for/in` loop to iterate through the
#list.
city_list = []
for city in range(5):
    user_city = input("Enter five cities: ")
    city_list.append(user_city)

print(f"The first city is:{city_list[0]}")
print(f"The second city is:{city_list[1]}")
print(f"The third city is:{city_list[2]}")
print(f"The fourth city is:{city_list[3]}")
print(f"The fifth city is:{city_list[4]}")
"""

















