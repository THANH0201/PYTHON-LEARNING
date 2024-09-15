#NAME: THANH HONG THI NGUYEN
#DATE: 15-SEP-2024
#MODULE 8:

import mariadb
import random
import math
import geopy
from geopy import distance

connection = mariadb.connect(
        host='127.0.0.1',
        port=3307,
        database='flight_game',
        user='root',
        password='123456',
        autocommit=True
        )
"""
#EXERCISE 1:
# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out the corresponding
# airport name and location (town) from the airport database used on this course. The ICAO codes are stored in the ident column of the airport table.

def get_airport_by_icao(icao):
    dt = (f"select name, municipality from airport where ident = '{icao}';")
    print(dt)
    cursor = connection.cursor()
    cursor.execute(dt)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for row in result:
            print(f" The airport name is {row[0]} and it's town is {row[1]} ")
    else:
        print("invalid ICAO code")

icao = input("Give the ICAO code(ident) of the airport: ")
get_airport_by_icao(icao)

# EXERCISE 2:
# Write a program that asks the user to enter the area code (for example `FI`) and prints out the airports located in that country
# ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports and so on.

def get_airport_by_area_code(code):
    dt = (f"select name, type from airport where iso_country = '{code}' order by type;")
    print(dt)
    cursor = connection.cursor()
    cursor.execute(dt)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for row in result:
            print(f" The airport {row[0]} is {row[1]} ")
    else:
        print("invalid area code")
def count_type(code):
    dt1 = (f"select count(type), type from airport where iso_country = '{code}' group by type order by TYPE;")
    cursor = connection.cursor()
    cursor.execute(dt1)
    result = cursor.fetchall()
    print(result)
    if cursor.rowcount > 0:
        for row in result:
            print(f"Finland has {row[0]} airport are {row[1]}")
    else:
        print("invalid area code")
code = input("Give the area code(country code) of the airport ( 2 letters): ")
get_airport_by_area_code(code)
count_type(code)

#EXERCISE 3:
# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the distance between the two
# airports in kilometers. The calculation is based on the airport coordinates fetched from the database. Calculate the distance using
# the `geopy` library:  https://geopy.readthedocs.io/en/stable/. Install the library by selecting **View / Tool Windows / Python Packages**
# in your PyCharm IDE, write `geopy` into the search field and finish the installation.

def get_airport1_location_by_ICAO_code(icao1):
    dt1 = (f"select latitude_deg,longitude_deg from airport where ident = '{icao1}';")
    #print(dt)
    cursor = connection.cursor()
    cursor.execute(dt1)
    result1 = cursor.fetchall()
    #print(result1)
    if cursor.rowcount > 0:
        for row in result1:
            air1 = [row[0], row[1]]
            return air1
    else:
        print("invalid area code")
icao1 = input("Give the code(ident:00A) of the airport 1: ")
airport1 = get_airport1_location_by_ICAO_code(icao1)

def get_airport2_location_by_ICAO_code(icao2):
    dt2 = (f"select latitude_deg,longitude_deg from airport where ident = '{icao2}';")
    #print(dt)
    cursor = connection.cursor()
    cursor.execute(dt2)
    result2 = cursor.fetchall()
    #print(result2)
    if cursor.rowcount > 0:
        for row in result2:
            air2 = [row[0], row[1]]
            return air2
    else:
        print("invalid area code")
icao2 = input("Give the code(ident:00AA) of the airport 2: ")
airport2 = get_airport2_location_by_ICAO_code(icao2)

print(f" The airport 1 has coordinate is {airport1} ")
print(f" The airport 2 has coordinate is {airport2} ")
print(f" The distance of two airports is: {distance.distance(airport1,airport2).km} km")
"""




