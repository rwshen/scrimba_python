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
name = input('What is your name?: ')
age = input('How old are you?: ')
print(f'Hello {name}! You are {age} years old.')

num1 = float(input('Enter a number: '))
num2 = float(input('Enter a different number: '))
print(num1 + num2)