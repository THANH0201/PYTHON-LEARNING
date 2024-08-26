import math
import random
"""
#EXERCISE 1
#Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs
#to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was.
#A zander must be 42 centimeters or longer to meet the size limit.
zander_length = float(input("Enter the zander length in centimeters please: "))
if zander_length < 42:
    print("The zander length must be is 42 centimeters or longer to meet the size limit.")
else:print("Well done!")

#EXERCISE 2
#Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below.
#You must use an if/elif/else structure in your solution.
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message `Invalid cabin class`.
print("THE CABIN CLASS LIST\n LUX: upper-deck cabin with a balcony.\n A: above the car deck, equipped with a window.\n B: windowless cabin above the car deck.\n C: windowless cabin below the car deck.")
user_code = str(input("Please enter the cabin class code from list:"))
if user_code == "LUX":
        print("Your choice is:LUX: upper-deck cabin with a balcony.")
elif user_code == "A":
        print("Your choice is:A: above the car deck.")
elif user_code == "B":
        print("Your choice is:B: windowless cabin above the car deck.")
elif user_code == "C":
        print("Your choice is:C: windowless cabin below the car deck.")
else:print("Invalid cabin class!")

#EXERCISE 3
#Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
gender = str(input("Please choose your gender FEMALE or MALE: "))
hemoglobin = float(input("Please enter your hemoglobin value(g/l) as a integer number: "))
if gender == "FEMALE":
        if 117 <= hemoglobin <= 155:
                print("Your hemoglobin is normal")
        elif hemoglobin < 117:
                print("Your hemoglobin is low than minimum value")
        else:   print("Your hemoglobin is higher than maximum value")
elif gender == "MALE":
        if 134 <= hemoglobin <= 167:
                print("Your hemoglobin is normal")
        elif hemoglobin < 134:
                print("Your hemoglobin is low than minimum value")
        else:   print("Your hemoglobin is higher than maximum value")
else: print("Please enter the gender as CAPSLOCK text")

#EXERCISE
#Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
#A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are
#also divisible by 400.
year = int(input("Please enter a year: "))
if year % 4 == 0 or (year % 100 == 0 and year % 400 == 0):
    print(str(year), "is a leap year")
else: print(str(year), "is not a leap year")
"""