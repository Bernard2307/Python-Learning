import os #importamos funcionalidades do sistema operacional
import time #biblioteca para sleep

mensagens = [] #lista vazia para armazenar mensagens 

nome = input("Nome de usuario: ")
print(f"\nBem vindo ao chat {nome}, respeite as diretrizes do nosso grupo e boa interação")
time.sleep(5)

while True:

    os.system('cls')
    if len(mensagens) > 0:
        for l in mensagens:
            print(l['nome'], "-", l['texto'])

    print("________________")

    texto = input("mensagem: ").lower()
    if texto == "fim":
        time.sleep(3)
        print(f"\n{nome} saiu do chat\n")
        break
        

    mensagens.append({
        "nome":nome,
        "texto":texto
    })