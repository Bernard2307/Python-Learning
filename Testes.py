import math
def area(r):
    return math.pi * (r**2)

raios = [2, 5, 8, 12]

areas = map(area,raios)
print(list(areas))

