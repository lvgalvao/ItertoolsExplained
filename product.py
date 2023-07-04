tamanhos = ['P', 'M', 'G', 'GG']
cores = ['preta', 'azul', 'vermelha', 'verde']

# for tam in tamanhos:
#     for cor in cores:
#         print(f'{cor=} e {tam=}')

from itertools import product

prods = product(tamanhos, cores)
print(next(prods))

for prod in prods:
    print(prod)