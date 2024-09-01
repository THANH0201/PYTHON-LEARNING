# THANH HONG THI NGUYEN
# DATE: 01-09-2024
# MODULE 4: WHILE LOOPS
import math
import random
"""
#EXERCISE 1
#Write a program that uses a `while` loop to print out all numbers divisible by three in the range of 1-1000.

number = 3
while number % 3 == 0 and number <=1000:
    print(number)
    number = number+3
 
#EXERCISE 2
#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
number = float(input("Enter a number: "))
while number >= 0:
    print(f"{number} inches equal {number*2.54} centimeters")
    number = float(input("Enter a number: "))
print(f"This is negative value")

#EXERCISE 3
#Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program
#prints out the smallest and largest number from the numbers it received.
max_num = None
min_num = None
i=0
while True:
    input_number = input("Enter the numbers, enter empty string to exit:")
    if input_number != " ":
        i = i + 1
    else:
        break
    if max_num == None or int(input_number) > max_num:
        max_num = int(input_number)
    if min_num == None or int(input_number) < min_num:
        min_num = int(input_number)
print(f"The smallest number is {min_num}")
print(f"The largest number is {max_num}")

#EXERCISE 4:
#Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until
#they guess the right number. After each guess the program prints out a text: `Too high`, `Too low` or `Correct`.
#Notice that the computer must not change the number between guesses.
random_number = random.randint(1, 10)
while True:
    user_number = int(input("Enter a number: "))
    if user_number == random_number:
        print(f"Well done! The hidden number is {random_number}")
        break
    elif user_number < random_number:
        print("The hidden number is less than the user number")
    else:
        print("The hidden number is greater than the user number")

#EXERCISE 5:
#Write a program that asks the user for a username and password. If either or both are incorrect, the program
#ask the user to enter the username and password again. This continues until the login information is correct or
#wrong credentials have been entered five times. If the information is correct, the program prints out `Welcome`.
#After five failed attempts the program prints out `Access denied`. The correct username is **python** and password
#**rules**.
count = 0
while True:
    user_name = input("Enter your user name: ")
    password = input("Enter your password: ")
    count = count + 1
    if (user_name != "**python**" or password != "**rules**") and count < 5:
        print(f"Wrong username or password, please try again ")
    elif (user_name != "**python**" or password != "**rules**") and count == 5:
        print("Access denied")
        break
    else:
        print(f"Welcome!")
        break
"""
#EXERCISE 6:
"""
#Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit
circle. A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B
is drawn around the unit circle so that circle A is completely inside the square. The corners of the square are now 
(-1,-1), (1, -1), (1, 1), and (-1, 1). If a large number of random points are scattered inside the square, the fraction
of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of 
square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method for calculating an approximation of the value 
of pi: Let's generate a large number of random points, such as one million, inside square B. Let N be the total number
of random points. Each point inside the square is tested for whether it resides inside circle A. Let n be the total 
number of points that fall inside circle A. Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that
asks the user how many random points to generate, and then calculates the approximate value of pi using the method 
explained above. At the end, the program prints out the approximation of pi to the user. (Notice that it is easy to
test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

N = int(input("Enter the number of random points to generate: ")) #random points
n = 0 # the points are inside circle
i = 0 # the number of loops
while i < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2) < 1:
        n = n + 1

    i = i + 1
print(f"The approximation of pi is:{(4*n)/N}, the difference with math is:{math.pi - ((4*n)/N)}")
"""




