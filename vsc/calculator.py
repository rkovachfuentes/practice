
def add(x,y):
    x = float(x)
    y = float(y)
    z = x + y
    print(z)
    return(z)
def subtract(x,y):
    x = float(x)
    y = float(y)
    z = x - y
    print(z)
    return(z)
def multiply(x,y):
    x = float(x)
    y = float(y)
    z = x * y
    print(z)
    return(z)
def divide(x,y):
    x = float(x)
    y = float(y)
    z = x / y
    print(z)
    return(z)
def absolute(x):
    x = abs(float(x))
    print(x)
    return(x)

x = input("First value: ")
op = input("Operation: ")
if op != "abs":
    y = input("Second value: ")

if(op == "+"):
    add(x,y)
elif(op == "-"):
    subtract(x,y)
elif(op == "abs"):
    absolute(x)
else:
    print("Invalid operation")
