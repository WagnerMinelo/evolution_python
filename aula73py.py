"""
Higher Order Functions
Funções de primeira classe
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Wagner')
)

print(
    executa(saudacao, 'Bom dia', 'Bruno')
)



# v = executa(saudacao, 'Bom dia', 'Wagner')
# print(v)




# v = saudacao_2('Bom dia')
# print(v)
