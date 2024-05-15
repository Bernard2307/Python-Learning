import PySimpleGUI as sg

sg.theme('Dark2')

style = [
    [sg.Text('Fornecedor',size=(20)),sg.Input(key='1',size=(20))], #fornecedor
    [sg.Text('Produto',size=(20)),sg.Input(key='2',size=(20))], #produto
    [sg.Text('Quantidade',size=(20)),sg.Input(key='3',size=(20))], #quantidade
    [sg.Text('Categoria',size=(20)),sg.Input(key='4',size=(20))], #categoria
    [sg.Text('Pagamento',size=(20)),sg.Input(key='5',size=(20))], #pagamento
    [sg.Button('Salvar',size=(20))],#btn-salvar
    [sg.Button('Excluir',size=(20))],#btn-excluir
]

janela = sg.Window('Cadastro De Fornecedor',layout=style)

while True:
    events,values = janela.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Salvar':
        sg.popup('Fornecedor cadastrado')
        janela['1'].update('')
        janela['2'].update('')
        janela['3'].update('')
        janela['4'].update('')
        janela['5'].update('')