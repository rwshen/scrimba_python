# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
def convert_to_fahrenheit(num_1):
    return num_1*9/5 + 32

def calculator(num_1, operator, num_2, celsius=True):
    if operator == '+': 
        if celcius == False:
            return convert_to_fahrenheit(float(num_1 + num_2))
        return float(num_1 + num_2)
    elif operator == '-':
        if celcius == False:
            return convert_to_fahrenheit(float(num_1 - num_2))
        return float(num_1 - num_2)
    elif operator == '*':
        if celcius == False:
            return convert_to_fahrenheit(float(num_1 * num_2))
        return float(num_1 * num_2)
    else:
        if celcius == False:
            return convert_to_fahrenheit(float(num_1 / num_2))
        return float(num_1 / num_2)

num_1 = float(input('Enter a number: '))
operator = input('Enter an operator: ')
num_2 = float(input('Enter another number: '))
convert = input('Do you want to turn to F?: ')
if convert.title() == 'Yes' or convert.title() == 'Y':
    celcius = False
celcius = True
print(calculator(num_1, operator, num_2, celcius))