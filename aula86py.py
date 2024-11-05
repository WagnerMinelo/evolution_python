# Dictionary Comprehension e Set Comprehension
produto = {
    'nome': 'Borracha',
    'preco': 4.5,
    'categoria': 'Escolar',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, (int, str)) else valor
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

lista = [
    ('a', 'valor a'),
    ('b', 'valor a'),
    ('b', 'valor a'),
]
#dc = {
 #   chave: valor 
 #   for chave, valor in lista
    
#}

# print(dict(lista))

s1 = {2 ** i for i in range(10)}
print(s1)
# print(set(range(10)))