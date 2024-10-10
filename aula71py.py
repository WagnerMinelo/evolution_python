"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x, y , resto)


# def soma(x, y):
#    return x + y

def soma(*args):
    print(args)
    total = 0
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3) 
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6) 
print(soma_4_5_6)

numeros = 3, 5, 293, 59, 30, 304
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)
