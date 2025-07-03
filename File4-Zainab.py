#Declare a variable student_id with value 101 (integer) and a variable grades with a list: [85, 90, 92].
student_id : int = 101
grades : list = [85, 90, 92]
print(type(student_id), "student id is", student_id)
print(type(grades), "grades are", grades)
#Create a variable price with value 19.99 (integer) and a variable dimensions with a tuple: (5.5, 3.2).
price : float = 19.99
dimension : tuple = (5.5, 3.2)
print(type(price), "price is", price)
print(type(dimension), "dimension is", dimension)
#Declare a variable complex_value with a complex number 2 + 3j, and a variable numbers with range (1,5).
complex_value : complex = 2 + 3j
numbers : range = range(1,5)
print(type(complex_value), "complex_value is", complex_value)
print(type(numbers), "numbers are", list(numbers))
#Create a variable is_active with boolean value True, and a variable unique_ids with a set: {1, 2, 3}.
is_active : bool = True
unique_ids : set = {1, 2, 3}
print(type(is_active), "is_active is", is_active)
print(type(unique_ids), "unique_ids are", unique_ids)
#Declare a variable status with a string 'Active' using single qoutes, and a variable fixed_colors with a frozenset containing "red" and "blue".
status : str = 'Active'
fixed_colors = frozenset(['red' , 'blue'])
print(type(status), "status is", status)
print(type(fixed_colors), "fixed colors are", fixed_colors)
#Create a variable country with a string "Canada" using double qoutes, and a variable cities with a list ["Toronto" , "Vancouver"].
country : str = "Canada"
cities : list = ['Toronto' , 'Vancouver']
print(type(country), "country is", country)
print(type(cities), "cities are", cities)
#Declare a variable motto with the string 'Keep it simple' using triple single qoutes, and a variable coordinate with a tuple: (10, 20, 30).
motto : str = '''Keep it simple'''
coordinates : tuple = (10, 20, 30)
print(type(motto), "motto is", motto)
print(type(coordinates), "coordinates are", coordinates)
#Create a variable quantity with value 50 (integer), and a variable tags with a set: {"urgent" , "new"}.
quantity :int = 50
tags : set = {'urgent', 'new'}
print(type(quantity), "quantity is", quantity)
print(type(tags), "tags are", tags)
#Declare a variable distance with a float value 42.5, and a variable steps with range (0, 10, 2).
distance : float = 42.5
steps : range = range(0, 10, 2)
print(type(distance), "distance is", distance)
print(type(steps), "steps are", steps)
#Create a variable note with a multi-line string using triple double qoutes:  Meeting at 9 AM  Bring Notebook  and a variable locked_values with a frozenset: {100,200,300}.
note : str = """
Meeting at 9 AM
Bring Notebook"""
locked_values = frozenset([100, 200, 300])
print(type(note), "note", note)
print(type(locked_values), "locked_values", locked_values) 