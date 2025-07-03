#Create a variable called "greeting" and store any message . print it.
greeting = "hello world"
print(greeting)
#Change the value of greeting to a new message. and print the updated message.
greeting = "hello AI"
print(greeting)
#Create a variable of first-name and last-name, then print full name using f-string.
first_name = "Zainab"
last_name = "Shahbaz Ahmad"
full_name = (f"{first_name} {last_name}")
print(full_name)
#Print a famous qoute with author's name using f-string.
author_name = "Thomas Carlyle"
quote = "Speech is Silver, Silence is Gold"
print(f"{author_name} : {quote}")
#Store a name with extra spaces, strip them, and print clean output.
name_with_spaces = "    Zainab   "
name_with_spaces = name_with_spaces.strip()
print(name_with_spaces)
#Take a number add 5, multiply by 2, subtract by 3, and print the result.
a = 20
result = ((a+5) * 2 - 3)
print("result:", result)
#Create a and b; print their sum, difference, product, and quotient.
a = 5
b = 10
print("sum", a+b)
print("subract", a-b)
print("product", a*b)
print("quotient", a/b)
#Find square and cube of a number using ** operator.
y = 20
print("square", y**2)
print("cube", y**3)
#Add three floating-point numbers and print the total.
x = 10.8
y = 230.6
z = 98.5
total = x + y + z
print("total:", total)
#Assign x, y, z in one line and print them.
x = y = z = 20
print(x, y, z)
#Create a list of 5 favorite fruits and print each one separately.
fav_fruits = ["apple", "banana", "cherry", "mango", "pearl"]
for x in fav_fruits:
    print(x)
#Modify the 2nd item in the list and print the updated list.
item_list = ["bread", "sugar", "milk", "eggs", "tea"]
item_list[1] = "orange"
print(item_list)
#Append a new fruit and insert one at the beginning.
fruits_name = ["apple", "grapes", "orange", "cherry"]
fruits_name.append("melon")
fruits_name.insert(0,"watermelon")
print(fruits_name)
#Delete items using del, pop() and remove().
z = ["chilli", "black pepper", "turmeric", "salt"]
del z [0]
print(z)
z.pop(1)
print(z)
z.remove("black pepper")
print(z)
#Use sort() and sorted() to sort the list. Show before and after.
a = [5, 8, 10, 4, 6]
print("before sort():", a)
a.sort()
print("after sort():", a)
b = [4, 6, 8, 2, 9]
print("before sorted():", b)
d = sorted(b)
print("after sorted():", b)
#Create a list of dream travel destinations: -Sort alphabetically  -Reverse the order  -Count total detination
x = ["Bahrain", "Saudia", "Makkah", "Madinah", "Turkey"]
sorted(x)
print("sorted alphabetically:", x)
x.reverse()
print("reverse order:", x)
print("total destination:", len(x))
#Start with an empty guest list:  -Append 3 guests  -Insert 1 at the beginning  -Remove one using pop()  -Print the final list
guest_list = []
guest_list.append("Ayesha")
guest_list.append("Seerat")
guest_list.append("Meerab")
guest_list.insert(1,"Faiza")
guest_list.pop(2)
print(guest_list)
#Access the last 3 elements of a list without negative indexing.
z = [2, 4, 6, 8, 10, 12, 14]
print(z[3 :6])
#From a list of numbers, print only even numbers.
z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in z:
    if num % 2 == 0:
        print(num)
#Print squares of the first 10 natural numbers in a list.
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)