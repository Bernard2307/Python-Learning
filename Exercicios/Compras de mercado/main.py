import os
import subprocess

''''comits

Se a fruta/alimento que for removido não tiver sido adicionado, retorna informação para o usuario

    comits
'''

#DICTIONARY
alimentos = {'Carne': 50, 'Arroz': 20, 'Feijão': 20, 'Queijo': 35}
frutas = {'Maçã': 10, 'Pêra': 20, 'Uva': 25}

#GROCERY LIST
lista_compras = []

# ESTOQUE DOS ALIMENTOS - - - FOOD STOCK
def estoque(tipo):

    if tipo == 'alimentos':
        print("ESTOQUE DE ALIMENTOS:")
        for alimento, quantidade in alimentos.items():
            print(f"{alimento}: {quantidade}")
    elif tipo == 'frutas':
        print("ESTOQUE FRUTAS:")
        for fruta, quantidade in frutas.items():
            print(f"{fruta}: {quantidade}")
    else:
        print("Valor inválido")

#SYSTEM OF PROGRAM
def sistema():
    os.system('cls')
    op_user = int(input("ESCOLHA UMA OPÇÃO ABAIXO\n\n1-VERIFICAR ESTOQUE\n2-ADICIONAR ALIMENTO\n3-REMOVER ALIMENTO\n4-VERIFICAR PREÇO DO ALIMENTO\n5-VER CARRINHO DE COMPRAS\n6-SAIR\n\nOPÇÃO ESCOLHIDA: "))

    while op_user != 6: 
        match op_user:
            case 1: # check stock 
                op_vef_estoque = int(input("1-VERIFICAR ESTOQUE ALIMENTOS\n2-VERIFICAR ESTOQUE FRUTAS\nOPÇÃO ESCOLHIDA: "))

                if op_vef_estoque == 1:
                    estoque('alimentos')
                elif op_vef_estoque == 2:
                    estoque('frutas')
                else:
                    print("Opção inválida")
            
            case 2: #add food
                op_add_food = int(input("1-FRUTAS\n2-ALIMENTO\nOPÇÃO ESCOLHIDA: "))
                if op_add_food == 1:
                    op_fruits = int(input("1-Maçã\n2-Pêra\n3-Uva\nOPÇÃO ESCOLHIDA: "))

                    if op_fruits == 1:
                        lista_compras.append('Maçã')
                    elif op_fruits == 2:
                        lista_compras.append('Pêra')
                    elif op_fruits == 3:
                        lista_compras.append('Uva')
                    else:
                        print("Opção invalida")
                    print(f"{lista_compras}")

                elif op_add_food == 2:
                    op_alimentos = int(input("1-Carne\n2-Arroz\n3-Feijão\n4-Queijo\nOPÇÃO ESCOLHIDA: "))

                    if op_alimentos == 1:
                        lista_compras.append('Carne')
                    elif op_alimentos == 2:
                        lista_compras.append('Arroz')
                    elif op_alimentos == 3:
                        lista_compras.append('Feijão')
                    elif op_alimentos == 4:
                        lista_compras.append('Queijo')

                else:
                    print("Opção inválida, digite uma opção valida")

            case 3: #remove food
                op_pop_food = int(input("1-FRUTAS\n2-ALIMENTO\nOPÇÃO ESCOLHIDA: "))
                if op_pop_food == 1:
                    pop_food = int(input("1-Maçã\n2-Pêra\n3-Uva\nOPÇÃO ESCOLHIDA: "))

                    if pop_food == 1:
                        lista_compras.remove('Maçã')
                    elif op_pop_food == 2:
                            lista_compras.remove('Pêra')
                    elif op_pop_food == 3:
                            lista_compras.remove('Uva')
                    else:
                        print("Opção invalida")
                    print(f"{lista_compras}")
            
            case 4: #verify price
                op_verify = int(input("1-FRUTAS\n2-ALIMENTO\nOPÇÃO ESCOLHIDA: "))
                if op_verify == 1:
                    for fruta, valor in frutas.items():
                        print(f"\n{fruta} -- R${valor}")
                elif op_verify == 2:
                    for alimento, valor in alimentos.items():
                        print(f"\n{alimento} -- R${valor}")
                else:
                    print("Opção invalida")
            
            case 5:
                print(lista_compras)

            case 6:
                os.system("cls")
                print("PRGORAMA ENCERRADO")
                subprocess.run("exit", shell=True)

        input("Aperte enter para continuar...")
        os.system("cls")        
        op_user = int(input("ESCOLHA UMA OPÇÃO ABAIXO\n\n1-VERIFICAR ESTOQUE\n2-ADICIONAR ALIMENTO\n3-REMOVER ALIMENTO\n4-VERIFICAR PREÇO DO ALIMENTO\n5-VER CARRINHO DE COMPRAS\n6-SAIR\n\nOPÇÃO ESCOLHIDA: "))

#MAIN
sistema()
