#Code to solve a Quadratic eqn
#Made by U25CYS1022
a = float(input("What is the value of a? "))
b = float(input("What is the value of b?"))
c = float(input("What is the value of c? "))

d = b*b - 4*a*c

if d >= 0:
    x1 = (-b + d**0.5) / (2*a)
    x2 = (-b - d**0.5) / (2*a)
    print(f"The root's are {x1} and {x2}")
else:
    print("No real roots")