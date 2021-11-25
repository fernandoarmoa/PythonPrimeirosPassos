# INICIO DA AULA 5

# LISTAS E TUPLAS

# LISTAS
# AS LISTAS SÃO MUTÁVEIS
# As listas são declaradas com o simbolo de colchete []
# As listas em Python podem armazenar qualquer tipo de variável, mas não é recomendável!
# as posições dos elementos iniciam sempre na posição 0

print(' - - - LISTAS - - - ')
lista = [11, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'aranha', 'galinha']
lista_mista = [2, 'pato', 'ganço', 1.99]

print(lista)
print(type(lista))
print(lista_animal)
print(type(lista_animal))
print(lista_mista)
print(type(lista_mista))

for x in lista_animal:
    print(x)

print('------------------')

print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print('------------------')

soma = 0
for x in lista:
    soma += x
print('Total  : {} - (utilizando o for para percorer a lista)'.format(soma))
print('------------------')

print('Total  : {} - (utilizando o método sum)'.format(sum(lista)))
print('------------------')

print('Maior  : {} - (utilizando o método max)'.format(max(lista)))
print('------------------')

print('Menor  : {} - (utilizando o método min)'.format(min(lista)))
print('------------------')

print('Tamanho: {} - (utilizando o método len)'.format(len(lista)))
print('------------------')

# Os métodos min e max tb funcionam com strings, no caso ele retorna o valor de acordo com a ordem alfabetíca
print('Primeiro na ordem alfabética: {} - (utilizando o método min)'.format(min(lista_animal)))
print('------------------')

print('Último na ordem alfabética  : {} - (utilizando o método max)'.format(max(lista_animal)))
print('------------------')

print('Lista original: ' + str(lista))
lista.sort()
print('Lista ordenada: ' + str(lista))
lista.reverse()
print('Lista reversa : ' + str(lista))
print('------------------')

print('Lista original: {}'.format(lista_animal))
lista_animal.sort()
print('Lista ordenada: {}'.format(lista_animal))
lista_animal.reverse()
print('Lista reversa : {}'.format(lista_animal))
print('------------------')


if 'gato' in lista_animal:
    print('Existe gato na lista.')

if not 'papagaio' in lista_animal:
    print('Não existe papagaio na lista.')
    lista_animal.append('papagaio')         # método append() - inseri um elemento na última posição da lista
    print(lista_animal)

lista_animal.pop()                          # método pop() sem argumento - retira o elemento da última posição da lista
print(lista_animal)

lista_animal.pop(1)                         # método pop(0) com argumento - retira o elemento da posição indicada no argumento
print(lista_animal)

lista_animal.remove('elefante')             # método remove(arg) - retira o elemento de acordo com o argumento passado.
print(lista_animal)


# TUPLAS
# AS TUPLAS SÃO IMUTÁVEIS
# As listas são declaradas com o simbolo de parenteses ()
print('\n\n--------------------------------\n')
print(' - - - TUPLAS - - - \n')

print(lista_animal)
lista_animal[0] = 'macaco'
print(lista_animal)
print('A lista aceitou a alteração.')

tupla = (1, 10, 12, 14)
print(tupla)
print(tupla[0])
# tupla[0] = 13
print('Nesse caso (tupla[0] = 13) vai dar um erro, pois o tipo tupla não aceita alteração.')

print('--------------')
print('Convertendo uma lista em tupla')
print(lista_animal)
print(type(lista_animal))
tupla_animal = tuple(lista_animal)
print(tupla_animal)
print(type(tupla_animal))
print('--------------')
print('Convertendo uma tupla em lista')
print(tupla)
print(type(tupla))
lista_numerica = list(tupla)
print(lista_numerica)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)


# FIM DA AULA 5