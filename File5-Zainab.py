#Create two variables a = 10 and b = 3. Perform and print:  addition(+), subtraction(-), multiplication(*), division(/), modulus(%), exponentiation() and floor division(//).**
a : int = 10
b : int = 3
print("a + b = ", a + b)      #Addition
print("a - b = ", a - b)      #Subtraction
print("a * b = ", a * b)      #Multiplication
print("a / b = ", a / b)      #Division
print("a % b = ", a % b)      #Modulus
print("a % b = ", a ** b)     #Exponentiation
print("a // b = ", a // b)    #Floor Division
#Compare a and b using comparison operators: ==, !=, >, <, >=, <=. Print the result of each comparison.
print("a == b = ", a == b)     #False, equal
print("a != b = ", a != b)     #True not equal
print("a > b = ", a > b)       #True greater than 
print("a < b = ", a < b)       #False less than
print("a >= b = ", a >= b)     #True, greater than or equal
print("a <= b = ", a <= b)     #False, less than or equal
#Create two boolean variables: x = True, y = False. Print and perform result of: x and y, x or y, and not x.
x : bool = True
y : bool = False
print("x and y = ", x and y)    #False
print("x or y = ", x or y)      #True
print("not x = ", not x)        #False
#Create num = 5 and perform assignment operations: +=, -=, =, /=, %=, *=, //=. Print the result after each operation.
x = 5
print("assignment : x = 5 ", x)
x += 2
print("addition assignment : x += 2 ", x)
x -= 3
print("subtraction assignment : x -= 3 ", x)
x *= 1
print("multiplication assignment : x *= 1 ", x)
x /= 4
print("division assignment : x /= 4 ", x)
x //= 2
print("floor division x //= 2 ", x)
#Create m = 100, n = 100. Check if they are the same object using is and is not, and print the result.
m : int = 100
n : int = 100
c = a 
print("m is n : = ", m is n)
print("m is c = ", m is c)
print("m is not n : = ", m is not n)
#Create a string text = "Python Programming". Check if "Python" is in text and if "Java" is not in text.
text : str = ("python programming")
print("python in text = ", "python" in text)
print("jana not in text = ", "java" not in text)
#Write a Python program to print all key word module.
import keyword
print("Python keyword : ")
print(keyword.kwlist)
#Declare: nam = "Ali", age = "20", height = 5.9. Print their values and data types using the type() function.
name : str = "Ali"
age : int = 20
height : float = 5.9
print("name : ", name, "type : ", type(name))
print("age : ", age, "type : ", type(age))
print("height : ", age, "type : ", type(height))
#Write 5 valid names (e.g., user_name, x1, -value, TotalAmount, data123) Also write 3 invalid ones (as comments): 1name, user-name, class. Explain why invalid names are not allowed.
user_name = "Zainab" 
_age = 20
_value = 20
TotalAmount = 1000
data123 = "Valid"
#Create special-naming variables: _hidden = 5, __private = 10, MAX_SIZE = 100. Print their values.
_hidden = 5
__private = 10
MAX_SIZE = 100
print("_hidden : ", _hidden)
print("__private : ", __private)
print("MAX_SIZE : ", MAX_SIZE)
#Assign valus in one line: x = 1, y = 2, z = 3. print them.
x, y, z = 1, 2, 3
print("x:", x, "y:", y, "z:", z)
#Assign same value 0 to a, b, c in one line. Print them.
a = b = c = 0
print("a:", a, "b:", b, "c:", c)
#Create temp = 100, print it, delete it using del, than try to print again and observe the error.
temp = 100
print("temp : ", temp)
del temp
try:
    print(temp)
except NameError as e:
    print("NameError : ", e)
#Create a string using triple single qoutes: "Hello". Print it.
qoute : str = '''Hello'''
print(type(qoute), "qoute = ", qoute)
#**Create a multi-line string using triple double qoutes: """This is line one.\nThis is line two.""" Print it**.
qoute : str = """This is line one.\n This is line two."""
print(type(qoute), "qoute = ", qoute)
#Use type() on various data types.
age_int : int = 5
temp_float : float = 8.9
is_student : bool = True
greeting :str = 'Hello'
print(type(age_int), "age_int = ", age_int)
print(type(temp_float), "temp_float = ", temp_float)
print(type(is_student), "is_student = ", is_student)
print(type(greeting), "greeting = ", greeting)
#Create score = 85. Check: score > 50 and score < 100. Print the result.
score : int = 85
print(type(score), "score > 50 and score < 100 : ", score > 50 and score < 100)
print(type(score), "score < 100 or score > 90 : ", score < 100 or score > 90)
print(type(score), "not(score > 90) : ", not(score > 90))
#Create message = "Welcome to Python". Use in and not in to check for the word "Python". Print the result.
message = "Welcome to Python"
print("python in message : ", "python" in message)
print("python not in message : ", "python" not in message)
#Write a code block using only comments that explains what your program does.
# - Variable assignments
# - Arithmatic and logical operations
# - Identity and mmembership operators
# - Working with string and keywords
#Create data = 123. Use id (data) to print it's memory address.
data = 123
print("Memory address of data:", id(data))