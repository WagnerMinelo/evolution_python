# Exercicio com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável
def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
        return total
    
 
multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)
# print(10*2*3*4*5)




# Crie uma função fala se um número é par ou impar.
# Retorne se o número é par ou impar.

def par_impar(numero):
   # return numero % 2 == 0
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar' 

outro_par_impar = par_impar
dois_e_par = outro_par_impar(2)

print(dois_e_par)
print(par_impar(5))
print(par_impar(23))
print(par_impar(30))

print(par_impar is outro_par_impar)