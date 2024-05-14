import PySimpleGUI as sg

sg.theme('Dark2')

style = [
    [sg.Text('Cliente'),sg.Input(key='1')],
    [sg.Text('Produto'),sg.Input(key='2')],
    [sg.Text('Quantidade'),sg.Input(key='3')],
    [sg.Text('Pagamento'),sg.Input(key='4')],
    [sg.Button('Salvar')],
    [sg.Text('',key='mensagem')],
]

janela = sg.Window('Sistema de cadastro BLDAN', layout=style)

while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Salvar':
        sg.popup('Fornecedor cadastrado')
        janela['1'].update('')
        janela['2'].update('')
        janela['3'].update('')
        janela['4'].update('')
    

