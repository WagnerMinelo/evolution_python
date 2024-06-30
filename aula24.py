# Operadores in e not in
# Strings são iteráveis
# 0 1 2 3 4 5
# W a g n e r
# -6-5-4-3-2-1

nome = 'Wagner'
# print(nome[2])
# print(nome[-6])

# Operador in

# print('a' in nome)
# print('vi' in nome)
# print('ner' in nome)


# Operador not in
# print(10 * '-')
# print('ner' not in nome)
# print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')