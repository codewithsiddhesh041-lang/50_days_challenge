# Write a Python program to demonstrate the difference between a global variable and a local variable inside a function.

c=1000           # global c
def add(a,b):
    if (a>5 or b<4):
        
        #c is a local variable

        c=0
        c=a+b
        print("Addition is",c,"This is a local c")

    else:
        pass

a=int(input("Enter the fisrt number:"))
b=int(input("Enter the second number:"))
add(a,b)

print("Global c =",c)