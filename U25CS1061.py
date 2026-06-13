def projectile(v, angle, g):
    t = (2 * v * math.sin(math.radians(angle))) / g
    h = (v**2 * (math.sin(math.radians(angle)))**2) / (2 * g)
    print(f"The Values of t and h are \nt={t}\nh={h}")
projectile(15, 60, 9.8)
print("Where t is the total Time of flight of the projectile \nAnd h is the maximum Height reached")
print("By U25CS1061 \nZayyad Sadiq \nComputer Science Department")