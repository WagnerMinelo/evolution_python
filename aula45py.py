"""
Iterável -> str, range, etc (___iter___)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu interador
"""
# texto = iter('Wagner') # ___iter___

# print(next(texto))
# print(next(texto))

# for letra in texto
texto = 'Wagner' # iterável
iteratador = iter(texto) # iterator

# while True:
 #   try:
  #      letra = next(iteratador)
   #     print(letra)
    # except StopIteration:
     #   break
     
for letra in texto:
    print(letra)


