'''
PART 1

SISTEMA DEVE CONTER: 
- LOGIN COMPLETO (LOGIN, SENHA E CRIAR CONTA)
- MEU PRINCIPAL COM OPÇÕES (ACESSAR SUBMENUS: COMPRAS, CALCULOS MATEMATICOS E CHAT)
- CADA SUBMENU DEVE CONTER LÓGICAS ESPECIFICAS 

SUBMENU COMPRA (INICIAR CARRINHO DE COMPRAS - GERENCIAR CARRINHO(ADD OR REMOVE ITEM, ESVAIZAR O CARRINHO) 

SUBMENU CALCULOS MATEMATICOS (CONVERSÃO DE TEMPERATURAS - FINANCEIROS - CALCULOS SIMPES)

SUBMENU CHAT (NOME DE USUARIO, SENHA)
---------------------------------------------------------------------------------------------------------
PART2

CRIAR ACESSO PARA MASTER PARA QUE ELE POSSA MANIPULAR CADA MENU 

COMPRAS - ELE PODERÁ GERENCIAR O ESTOQUE 
CALCULOS - ELE PODERÁ ADICIONAR NOVOS CALCULOS DE TEMPERATURA - NOVOS CALCULOS FINANCEIROS E SIMPLES
CHAT - ELE PODERÁ EXCLUIR A LISTA DE USUARIOS
'''

#declaração de váriaveis --- declaration of variables
line = 30
answer = ''
password = ''

print(f"-"*line)
print("SISTEMA DE LOGIN")
print(f"-"*line)

answer = input("Digite o seu login: ")
password = input("Digite a sua senha: ")

print(f"Login: {answer} \nSenha: {password}")
