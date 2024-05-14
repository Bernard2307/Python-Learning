import openpyxl
import openpyxl.workbook

wb = openpyxl.open('Estoque.xlsx')
frutas = wb['Frutas']

banana = frutas['B17']
maca = frutas.cell(9,3)
morango = frutas['12']

print(maca.value)

#percorrer os valores da celula morango
for celula in morango:
    print(celula.value)

#intervalo de linhas 
intervalo_rows = frutas [2:11] #de um até outro
for linha in intervalo_rows:
    for celula in linha:
        print(celula.value)

#todos os valores 
for linha in frutas.iter_rows(values_only=True): #min-rows e max-rows pode ser usado aqui 
    for celula in linha:
        print(celula)