a = int(input("Input value a: "))
b = int(input("Input value b: "))
c = int(input("Input value c: "))

d = (b**2 - 4*a*c) ** 0.5
x = (-b + d) / (2*a)
y = (-b - d) / (2*a)

print("Therefore, your root values are {x} and {y}")