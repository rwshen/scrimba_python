def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if unavailable, default age is used   
   
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting("brian", 27,"Blue")
# named notation - helps with readability
greeting(age=27, name="brian", color="blue")

def value_added_tax(amount): 
    tax = amount * 0.25
    total_amount = amount * 1.25
    # returns a tuple
    # return amount, tax, total_amount
    return [amount, tax, total_amount]


print(value_added_tax(100))