"""
Exercício
Exiba os índices da lista
"""
lista = ['Maria', 'Helena', 'Wagner']
lista.append('João')


indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))