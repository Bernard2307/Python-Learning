import PySimpleGUI as sg

sg.theme('Reddit')
layout = [
    [sg.Text('Usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('Login')],
    [sg.Text('',key='mensagem')],
]

window = sg.Window('Login',layout=layout)

while True:
    event, values = window.read() #enquanto não estiver logado, leia
    if event == sg.WIN_CLOSED: #se apertar o X, finaliza o programa
        break
    elif event == 'Login':

        #teste
        correct_password = '23072002'
        correct_user = 'Bernard'
        
        user_name = values['usuario']
        user_password = values['senha']

        if user_password == correct_password and user_name == correct_user:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Senha ou usuario incorreto')