# Taking a Scrimba Learn Python course
print('print() is the Python console.log()')
print("You can use double quotes for print()")

# dialects vs different languages
# don't need to worry about new lines with print() 

# Variables in python
failed_subjects="6"
name="Eric"
geography = True
print(name + " is failing " + failed_subjects + " subjects." )
name="Molly"
print(name + " is doing well in school.")

# Datatypes & Typecasting
# integers vs. floats
failed_subjects=2
float_example=3.45

# booleans 
is_failing=False
# you can use double quotes for contractions
contraction_example = "it's"
# the character after the backlash escapes the character
contraction_another_example='it\'s'
print(type(contraction_another_example))
print(type(failed_subjects))
print(type(float_example))

string_failed_subjects = str(failed_subjects)
print(name + " is failing " + string_failed_subjects + " subjects.")

# Typecasting oddities
a = int(1)        # a will be 1
b = int(2.5)      # b will be 2
c = int("3")      # c will be 3
c1 = int(float(("3.4")))   # c1 will be...3
d = float(1)      # d will be 1.0
e = float(2.5)    # e will be 2.5
f = float("3")    # f will be 3.0
g = float("4.23") # g will be 4.23
h = str("80s")    # h will be '80s'
i = str(22)       # i will be '22'
j = str(3.01)     # j will be '3.01'

print([a,b,c,c1, d,e,f,g,h,i,j])

# Arithmetic operations
# a=6
# b=2
a = 10
b = 3
print('Addition : ', a + b)
print('Subtraction : ', a - b)
print('Multiplication : ', a * b)
print('Division (float) : ', a / b)
# rounds the result to a full number
print('Division (floor) : ', a // b)
print('Modulus : ', a % b)
print('Exponent : ', a ** b)

# Strings
msg='welcome to Python 101: Strings'
msg1='welcome to Python 101 it\'s cool: Strings'
print(msg) # welcome to Python 101: Strings
print(msg + msg) # welcome to Python 101: Stringswelcome to Python 101: Strings
print(msg*2) # welcome to Python 101: Stringswelcome to Python 101: Strings
print(msg, msg) # welcome to Python 101: Strings welcome to Python 101: Strings
print(msg.upper()) # whole string will become uppercase
print(msg.lower())
print(msg.capitalize())
print(msg.title())
print(msg1.title()) # It'S

print(len(msg))
# count the number of instances of a letter or word
print(msg.count('Python'))
print(msg.count('o'))
# slicing
print(msg[0])
print(msg[-1])
print(msg[2:])
print(msg[::-1])

print(msg.find('h'))
print(msg.replace('Python', 'Typescript'))
msg1 = msg.replace('Python', 'Typescript')

print('Python' in msg)
print('Typescript' not in msg)

color = 'purple'
msg2 = f'[{name.capitalize()}] loves the color {color.lower()}!'
print(msg2)

# User input 
# name = input('What is your name?: ')
# age = input('How old are you?: ')
# print(f'Hello {name}! You are {age} years old.')

# num1 = float(input('Enter a number: '))
# num2 = float(input('Enter a different number: '))
# print(num1 + num2)

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
# name = input('Enter your name: ').title()
# distance_km = float(input('Enter a distance in km: '))
# distance_mi = distance_km / 1.609
# print(f'Hello {name}. The distance is {distance_km} km which is {round(distance_mi, 2)} mi.')


# Lists
friends = ['John','Michael','Terry','Eric','Graham']

print(friends[1],friends[4])
print(friends[2:4])
print(friends.index('Eric'))
print(friends.count('Eric'))

cars = [911, 130, 328, 535, 740, 308]
# sorting in place
friends.sort()
print(friends)
friends.sort(reverse=True)
print(friends)
friends.reverse()
print(friends)

print(min(cars))
print(max(cars))
print(sum(cars))

friends.append('TerryG')
friends.insert(1, 'TerryG')
print(friends)
friends[1]='TerryG'
print(friends)
friends.extend(cars)
print(friends)

# Remove from a list
friends.remove('TerryG')
print(friends)
# pop  it into memory to use it to something
friends.pop() 
print(friends)

# clear the list
# friends.clear()
print(friends)
del friends[1]

new_friends = friends.copy() # friends[:],  list(friends)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
# new_day = int(input('Enter number of lemonade sold in the new day: '))
# sales_w2.append(new_day)
sales = []
# sales_w1.extend(sales_w2)
# sales.extend(sales_w1)
sales = sales_w1 + sales_w2
# sales.sort() not needed to sort with min and max
print(sales)
best_day_profit = max(sales) * 1.5
worst_day_profit = min(sales) * 1.5
print(f'Best day profit: ${best_day_profit}')
print(f'Worst day profit: ${worst_day_profit}')
print(f'Combined profit: ${best_day_profit + worst_day_profit}')

# Split and Join
msg ='Welcome  to  Python  101: Split  and Join'
csv = 'Eric,John,Michael,Terry,Graham'
friends_list = ['Eric','John','Michael','Terry','Graham']
# list(msg) splits each letter
print(msg.split())
print('-'.join(friends_list))
# print(''.join(msg.split())) accomplishes the same as print(msg.replace(' ', ''))


csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
print(friends_list)
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
friends_list = csv.replace(';', ',').replace(':', ',').split(',')
# friends_list = (','.join(','.join(csv.split(';')).split(':'))).split(',')
print(friends_list)
# replace() doesn't support regex need to import re
import re
friends_list_1 = re.sub(r"[;:]", ",", csv).split(',')
print(friends_list_1)