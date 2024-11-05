# dir, hasattr e getattr e, Python
string = 'Wagner'
metodo = 'strip'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)
