import PySimpleGUI as sg

#estilo
sg.theme('Reddit')

#tela do sistema
layout = [
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('Password'), sg.Input(key='password')],
    [sg.Button('Login')],
    [sg.Text('',key='mensage')],
]

#iniciando a janela
janela = sg.Window('Login',layout=layout)

while True:
    events, values = janela.read()
    if events == sg.WIN_CLOSED:
        break
    elif events == 'Login':
        correct_pass = '12345'
        correct_user = 'Bernard'

        user_name = values['usuario']
        password_name = values['password']

        if user_name == correct_user and password_name == correct_pass:
            janela['mensage'].update('Login feito com sucesso')
        else:
            janela['mensage'].update('Senha ou usuario incorreto')