from openpyxl import load_workbook
import pyautogui

planilha = load_workbook('./AUTOMAÇÃO/PREENCHIMENTO/W4 - CADASTRO FORNECEDORES/vendas_de_produtos.xlsx')
planilha_fornecedores = planilha['vendas']

for linha in planilha_fornecedores.iter_rows(min_row=2,max_row=6,values_only=True):
    cliente, produto, quantidade, categoria = linha 

    pyautogui.click(567,345,duration=0)
    pyautogui.write(cliente)
    pyautogui.click(575,373,duration=0)
    pyautogui.write(produto)
    pyautogui.click(599,402,duration=0)
    pyautogui.write(str(quantidade))
    pyautogui.click(599,424,duration=0)
    pyautogui.write(categoria)
    pyautogui.click(514,453,duration=0) #btn salvar
    pyautogui.click(660,425,duration=1) #btn ok