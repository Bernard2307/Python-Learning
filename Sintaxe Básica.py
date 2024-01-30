nome = 'Bernard'
altura = 1.74
sexo = 'Homem'

#f + {variavel} -> F-STRING funciona para passarmos variaveis de qualquer valor
print(f"Olá {nome}, sua altura é {altura} e seu sexo é {sexo}")

#logica IF
if(sexo == 'Masculino'):
    print("Você é homem")
else:
    print("Você é mulher")

#casting/cast
inteiro = 50
casting_inteiro = int("50")
casting_inteiro2 = '50'

#printando os tipos de variaveis
print(type(inteiro))
print(type(casting_inteiro))
print(type(casting_inteiro2))

#operações aritimeticas nativas
#numero maximo e minimo
n_maximo = max(4,10) 
n_minimo = min(4,10)
print(n_maximo)
print(n_minimo)

#numero arredondado
flutuacao_ibovespa = 0.5144356
flutuacao_ibovespa_arredondado = round(0.5144356, 3)
print(flutuacao_ibovespa)
print(flutuacao_ibovespa_arredondado)

#coletando dados
#we use INPUT to collect data
nome = input("Qual o teu nome?: ")
print(f"Olá {nome}, seja bem vindo(a)")

#MATEMÁTICA
#para trazer o resto de um número usamos o % 
5 % 2 
#para trazer um inteiro do npumero usamos //
print(5 // 2) #retorna um valor inteiro mais próximo da divisão
print(int(5/2)) #retorna um valor inteiro mais próximo da divisão

#para fazer um cast usamos o -> res = tipo(var que quer converter)

#para usar booleam 
ativado = True 
desativado = False

#OBS = Podemos aplicar a lógica das preposições 

print(not ativado)
print(not desativado)

#Funções
#Quando atribuimos um valor à um parâmentro da função, o parâmetro passar a ser opcional
def soma(p1,p2=2):
    return p1*p2 

#list comprehension
#consiste em pegar uma lista e simplificar o seu reajuste

lista_produtos:['Celular','Tablet','Laptop']
lista_precos_produtos:[100,200,300]
lista_reajuste_preco_produtos:[preco*1.1 for preco in lista_precos_produtos]

#podemos aproveitar uma lista para gerar outra lista ou manipular com outros comandos, como por exemplo uma função
list_of_numbers = [2,4,6,8]
def elevation(valor):
    return valor * valor

res = [elevation(number) for number in list_of_numbers]
print(res)

#if direto
faturamento = 200
bonus = 100 if faturamento > 500 else 50 
print(bonus)

#switch case do python
x = 1
match x:
    case 1:
        print("Domingo")
    case 2:
        print("Segunda")
    case _:
        print("Qualquer dia")

#uso de ARGS 
#podemos passar qualquer tipo de dado dentro nessa função
def names(*args):
    return args

print(names())

#numero pares e impares com comprehension 
list_of_numbers = [1,2,3,4,5,6,7,8]

pares = [numeros for numeros in list_of_numbers if numeros % 2 == 0]
impares = [numeros for numeros in list_of_numbers if numeros % 2 != 0]

print(pares)
print(impares)

#dictionary comprehension 
numeros = {'A':2, 'B':3, 'C':4}
numeros_quadrados = {chave:valor **2 for chave,valor in numeros.items()}
print(numeros_quadrados)

#strip and title
#strip para tirar espaços do inicio e final
#title para colocar a primeira letra em caixa alta
name = str(input("Qual o seu nome?: "))
print(nome.strip().title())

#Lambida e Map
#Map retorna dados
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

#Filter
#Filtra dados de uma coleção
#Nesse caso ele está filtrando apenas os dados que existem
#retorna booleam
paises = ['','Brasil', 'Argentina', 'Coreia', '', 'Chile', '']
res = filter(None, paises)
print(list(res))

usuarios = [
    {"username": "be_o_baiano", "twettes": ["Eu adoro games"]},
    {"username": "tryhard", "twettes": ["Vamos estudar"]},
    {"username": "nakita123", "twettes": []},
    {"username": "spikenot", "twettes": []}
]

t = lambda usuario: len(usuario['twettes']) == 0

inativos = list(filter(t,usuarios))
print(inativos)