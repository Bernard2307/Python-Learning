usuarios = [
    {"username": "be_o_baiano", "twettes": ["Eu adoro games"]},
    {"username": "tryhard", "twettes": ["Vamos estudar"]},
    {"username": "nakita123", "twettes": []},
    {"username": "spikenot", "twettes": []}
]

t = lambda usuario: len(usuario['twettes']) == 0

inativos = list(filter(t,usuarios))
print(inativos)