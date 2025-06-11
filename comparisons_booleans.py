a = 7
b = 3
print(a < b)
print('o' in 'John')

c = [3,7,42]
d = c
print(c == d)
print(c is d)
print(id(c), id(d))
# bool values can be converted to 0 and 1
print(bool('Parrot'))

# Conditionals

is_raining = True
is_cold = True
print("Good Morning!")
# or and
if is_raining and is_cold:
    print("Bring an umbrella and jacket")
elif is_raining and not(is_cold): 
    print("Bring umbrella!")
elif not(is_raining) and is_cold: 
    print("Bring jacket!")
else:
    print("Shirt is fine")