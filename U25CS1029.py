a = 1; b = -3; c = 2

def almighty (a, b, c):
  x = (-b + ((b ** 2) - 4*a*c)**0.5) / (2 * a)
  y = (-b - ((b ** 2) - 4*a*c)**0.5) / (2 * a)

  print(f"\nWhen a = {a}, b = {b}, and c = {c}, the roots of the equation are: \nx = {round(x, 2)} or x = {round(y, 2)}")

almighty(a, b, c)
print(" ====> By Fatima Abubakar. \n ====> U25CS1029, Computer Science Department.")

