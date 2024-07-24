frase = 'O Python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais_vezes = 0
letra_que_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]


    if letra_atual == ' ':
        i += 1
        continue

    quantas_vezes_letra_apareceu_atual = frase.count(letra_atual)

    if apareceu_mais_vezes < quantas_vezes_letra_apareceu_atual:
        apareceu_mais_vezes = quantas_vezes_letra_apareceu_atual
        letra_que_apareceu_mais_vezes = letra_atual

    i += 1

print(
    'A letra que apareceu mais vezes foi '
    f'"{letra_que_apareceu_mais_vezes}" que apareceu '
    f'{quantas_vezes_letra_apareceu_atual}x'
)
