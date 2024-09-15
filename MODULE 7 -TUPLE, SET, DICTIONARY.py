#NAME: THANH HONG THI NGUYEN
#DATE: 06-SEP-2024
#MODULE 6: FUNCTION
import random
import math

"""
#EXERCISE 1:
# Write a program that asks the user for a number of a month and then prints out the corresponding season (`spring`,
# `summer`, `autumn`, `winter`). Save the seasons as strings into a tuple in your program. We can define each season to
# last three months, December being the first month of winter.
def print_season(month):
    the_season = ("winter","winter","spring","spring","spring","summer","summer","summer","autumn","autumn", "autumn", "winter")
    return the_season[month-1]

while True:
    month = int(input("Enter the month number (1-12): "))
    if 1<=month<=12:
        season = print_season(month)
        print(f"Month {month} is {season}.")
    else:
        print("Invalid month number.")

#EXERCISE 2:
# Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either prints out `New name` or
# `Existing name` depending on whether the name was entered for the first time. Finally, the program lists out the input names
# one by one, one below another in any order. Use the set data structure to store the names.


names = []
name_set = set(names)

while True:
    name = input("Enter a name, press empty string to finish:")
    if name == " ":
        break
    names.append(name)
    name_set = set(names)
    if len(names)!= len(name_set):
        print("That name is existing name.")
    else:
        print(f"That name is new name")
print(*name_set, sep = "\n")

#EXERCISE 3:
# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch
# the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter
# the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO
# code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can
# choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each
# airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)
"""










