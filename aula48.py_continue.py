"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Wagner'
# noutra_variavel = nome
# nome = 'João'
# print(nome)
# print(noutra_variavel)
''''''''''''''''''''''''
lista_a = ['Wagner', 'João', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)


