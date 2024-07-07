"""
Fatiamento de strings
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da str
"""
variavel = 'Olá mundo'
print(len(variavel))
print(variavel[-4:-3])
print(variavel[0:len(variavel):1])
print(variavel[0:9:3])
print(variavel[-1:-10:-2])