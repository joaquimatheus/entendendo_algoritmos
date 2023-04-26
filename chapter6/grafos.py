from collections import deque

grafo = {}
grafo['voce'] = ['alice', 'bob', 'claire'];
grafo['bob']  = ['anuj', 'peggy'];
grafo['alice'] = ['peggy'];
grafo['claire'] = ['thom', 'jonny'];
grafo['anuj'] = []
grafo['peggy'] = []
grafo['thom'] = []
grafo['jonny'] = []

fila_de_pesquisa = deque()
fila_de_pesquisa += grafo['voce']

def pessoa_e_vendedor(nome):
    return nome[-1] == 'm'

def pesquisa(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    verificadas = []

    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        if not pessoa in verificadas:
            if pessoa_e_vendedor(pessoa):
                print('pessoa' + ' eh um vendedor de manga!')
                break
            else:
                fila_de_pesquisa += grafo[pessoa]
                verificadas.append(pessoa)


pesquisa('voce')

while fila_de_pesquisa:
    pessoa = fila_de_pesquisa.popleft()
    if pessoa_e_vendedor(pessoa):
        print(pessoa + " e um vendedor de manga!")
        break
    else:
        fila_de_pesquisa += grafo[pessoa]

