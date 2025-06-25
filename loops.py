print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

def format_with_loops(num):
    i = 0
    message = f"Loops are awesome"
    while i <= num: 
        message = f"{i}." + "*"*i + "Loops are awesome" + "*"*i
        i+=1
    return message

print(format_with_loops(1))
print(format_with_loops(5))