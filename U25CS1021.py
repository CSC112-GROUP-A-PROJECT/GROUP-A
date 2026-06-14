# A program to find the roots of a quadratic quation using the quadratic formula
def quad_formula(a, b, c):
    x_1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    x_2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return x_1, x_2
    
x_1, x_2 = quad_formula(1, -5, 6)

print(f'The value for X_1 = {x_1}')
print(f'The value for X_2 = {x_2}')    

print('By U25CS1021 \nOkon Marvellous Iniabasi \nComputer Science Department')
