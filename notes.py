# Functions
def greeting(name, age=28):
    print(f"Hello {name}! You are {age} years old.")

name = input("What is your name?: ")
age = input("How old are you?: ")
greeting(name, age)
# default value
greeting("Judith")
