import sys

# Generator expression, iterables e iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
# print(next(iterator))
lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

print(generator)

# for n in generator:
 #   print(n)
