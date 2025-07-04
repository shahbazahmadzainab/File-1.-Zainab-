#Write a program that checks if a number is positive or negative.
num = int(input("Enter a number : "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")
#Input a number from the user and print whether it is even or odd.
num = int(input("Enter a number : "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
#Ask the user to enter their age. If age is 18 or above, print "Eligible for vote". Else print "Not eligible".
age = int(input("Enter your age : "))
if age >= 18:
    print("Eligible for vote")
else:
    print("Not eligible")
#Enter a number and check whether is is divided by: 3, 5, and both. Print an appropriate message.
num = int(input("Enter a number to check divisibility : "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
elif num % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3 or 5")
#**Ask for a student's marks and assign a grade: 90+ = "A+", 80+ = "A", 70+ =  "B", otherwise = "Fail"**
marks = int(input("Enter student's marks : "))
if marks >= 90:
    print("Grade : A+")
elif marks >= 80:
    print("Grade : A")
elif marks >= 70:
    print("Grade : B")
else:
    print("Fail")
#**Take a temperature input: Above 40 = "Too hot", Below 10 = "Too cold", otherwise = "Moderate weather"**
temp = int(input("Enter the temperature : "))
if temp > 40:
    print("Too hot")
elif temp < 10:
    print("Too cold")
else:
    print("Moderate")
#Ask the user to enter a year. Check whether it is a leap year or not.
year = int(input("Enter a year : "))
if (year % 4 == 0 and year % 100 != 0) or (year %400 == 0):
    print("Leap year")
else:
    print("Not a leap year")
#Input three numbers and print the largest one.
a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))
if a >= b and a >= c:
    print("Largest number : ", a)
elif b >= a and b>= c:
    print("Largest number : ", b)
else:
    print("Largest number : ", c)
#Ask the user to enter a password. If password matches "admin123" then print "Access granted", else "Access denied".
password = input("Enter the password : ")
if password == "admin123":
  print("Access granted")
else:
    print("Access denied")
#**Take an integer input. If number > 0, check if it's less than 100. Print appropriate message for both checks**.
num = int(input("Enter an integer : "))
if num > 0:
    print("Positive number")
    if num < 100:
        print("It is less than 100")
    else:
       print("It is 100 or more")
else:
    print("Not a positive number")