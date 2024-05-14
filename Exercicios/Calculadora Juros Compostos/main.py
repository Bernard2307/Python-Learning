print("CALCULADORA DE JUROS COMPOSTOS")

valor_inicial = float(input("Digite o valor inicial sem R$: "))
taxa_juros = float(input("Digite o valor da taxa de juros anual: "))
periodo_investimento = int(input("Digite o valor do tempo de investimento: "))
taxa_juros_decimal = taxa_juros / 100
valor_final = valor_inicial *(1+taxa_juros_decimal) ** periodo_investimento #M = C *(1 + i) ** t 
juros_acumulado = valor_final - valor_inicial

print(f"O valor do aporte inicial foi de R${valor_inicial}\n")
print(f"O valor do juros acumulados no período de {periodo_investimento} anos foi de {juros_acumulado}\n")
print(f"O valor total do aporte + rendimento foi de R${valor_final}\n")