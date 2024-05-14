import PySimpleGUI as sg

layout = [
    [sg.Text("Pegar cotação da moeda")],
    [sg.InputText(key ="nome_cotacao")],
    [sg.Button("Pegar cotação"), sg.Button("Cancelar")],
    [sg.Text(key ="texto_cotacao")],
]

janela = sg.Window("Sistema de Cotações", layout)

while True:
    evento,valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Cancelar":
        break

    if evento == "Pegar cotação":
        codigo_cotacao = valores["nome_cotacao"]
        print(f"Cotação do(a) {codigo_cotacao}")

janela.close()

