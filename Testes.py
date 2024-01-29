import math
def area(r):
    return math.pi * (r**2)

raios = [2, 5, 8, 12]

areas = map(area,raios)
print(list(areas))

#criar uma lambida e passar função para converter Celsius em Fhereient 
# f = 9/5 * c + 32 

cidades = [('berlim',29), ('san francisco',34), ('dacota johnson',31), ('limona',21)]
c_para_f = lambda dado: (dado[0].title(), (9/5) * dado[1] + 32)

print(list(map(c_para_f,cidades)))