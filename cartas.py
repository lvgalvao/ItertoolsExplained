

naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
valores = list(range(2,11)) + ['J', 'Q', 'K', 'A']

from itertools import product

baralho = product(valores,naipes)

for carta in baralho:
    print(carta)