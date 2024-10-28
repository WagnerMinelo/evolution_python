# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
# print(a, b)

# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)

# for chave, valor in pessoa.items():
#    print(chave, valor)

pessoa = {
    'nome': 'Wagner',
    'sobrenome': 'Minelo',    
}

dados_pessoa = {
    'idade': 20,
    'altura': 1.7,
}


pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já visto)
# kwargs - keyword arguments (argumentos nomeados)

def mostro_arguementos_nomeados(*args, **kwargs):
    print('Não nomeados: ', args)


    for chave, valor in kwargs.items():
        print(chave, valor)



# mostro_arguementos_nomeados(1, 2, nome='Wagner', qlq=123)
# mostro_arguementos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_arguementos_nomeados(**configuracoes)
