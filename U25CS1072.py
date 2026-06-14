def almighty(a, b, c):
    # Corrected formula using **0.5 for square root
    d = (b**2 - 4*a*c)**0.5
    x = (-b - d) / (2 * a)
    y = (-b + d) / (2 * a)
    
    print(f"The Values of x and y are \nX={x}\nY={y}")

# Example call
almighty(1, -2, 1)

print("\nWhere X is the Negative value of the Almighty Formula")
print("And Y is the Positive value.")
print("-" * 30)
print("By U25CS1072 \nAbdulaziz Halilu Bello \nComputer Science Department")
