# VARIABLES AND INTERACTIVE PROGRAMS
import math
import random
"""
#Exercise 1
# Write a program that asks your name and then greets you by your name: Examples:
# If you enter Viivi as your name, the program will greet you with `Hello, Viivi!`.
# If you enter Ahmed as your name, the program will greet you with `Hello, Ahmed!`.
print(f"Helo, {input("Enter your name here please:")}!")

#Exercise 2
# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = int(input("Enter a radius please:"))
print(f"The area of the circle is {math.pi*radius**2:.2f}")

#Exercise 3
#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of
#the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides
rectangle_length = float(input("Enter the rectangle length please:"))
rectangle_width = float(input("Enter the rectangle width please:"))
print(f"The area of the rectangle is {rectangle_length*rectangle_width:.2f}")
print(f"The perimeter of the rectangle is {rectangle_length*2 + rectangle_width*2:.2f}")

#Exercise 4
#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers
num1 = int(input("Enter the first integer number please:"))
num2 = int(input("Enter the second integer number please:"))
num3 = int(input("Enter the third integer number please:"))
print(f"The sum of three integer numbers is: {num1 + num2 + num3}")
print(f"The product of the three integer numbers is {num1 * num2 * num3}")
print(f"The average of the three integer numbers is {(num1 + num2 + num3)/3:.3f}")

#Exercise 5
#Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:
#One talent is 20 pounds.
#One pound is 32 lots.
#One lot is 13,3 grams.
talents = float(input("Enter talents please:"))
print(talents)
pounds = float(input("Enter pound please:"))
print(pounds)
lots = float(input("Enter lots please:"))
print(lots)
total_kg = (0.001*((13.3*lots)+(pounds*32*13.3)+(talents*20*32*13.3)))
print(f"The weight in modern units:)\n {int(total_kg)} kilograms and {((total_kg)-(int(total_kg)))*1000:.2f} grams")

#Exercise 6
# Write a program that draws two random combinations of numbers for a combination lock:
print(f"A 3-digit code where each number is between 0 and 9 is: {random.randint(0,999):03d}")
print(f"A 4-digit code where each number is between 1 and 6 is: {random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}{random.randint(1,6)}")
"""




