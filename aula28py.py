"""
 Exercício
 Peça ao usuário para digitar o seu nome
 Peça ao usuário para digitar sua idade
 Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios.
"""

nome = 'Wagner Minelo'
idade = 20
print(nome[::-1])
print(len(nome))
print(nome[0:1])
print(nome[12:13])


nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade: 
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    
    if '' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0:1]}')
    print(f'A última letra do seu nome é {nome[12:13]}')
else :
    print('Desculpe, você deixou campos vazio.')
