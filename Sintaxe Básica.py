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

#tratamento de erro com raise

def colore (texto, cor): 
    cores = {'verde', 'preto', 'amarelo', 'azul'}
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    print(f"O texto {texto} será impresso na cor {cor}")

    if cor not in cores:
        raise ValueError(f'Cor não existe na lista\nPrecisa estar entre {cores}')

colore('Pablo','Verde')

#tratando erro com TRY and EXCEPT 
try:
    bernard()
except:
    print("Houve um erro")