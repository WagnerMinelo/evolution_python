# try, except, else e finally
try:
    print('Abrir arquivo')
    # 8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
except IndexError as error:
    print('IndexError')
except (NameError, ImportError):
    print('NameErros, ImportError')
else:
    print('Não deu erro')
finally:
    print('Fechar arquivo')
