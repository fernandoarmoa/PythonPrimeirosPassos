# INICIO DA AULA 6

# CONJUNTOS ARITMÉTICO
# Para declarar um conjunto utilzamos o simbolo de chaves {}

conjunto_numerico = {1, 2, 3, 4, 4, 2}  # Não arnazena duplicidade de elemento, o mesmo elemento inserido mais de uma vez, será reconhecido apenas 1.
print(type(conjunto_numerico))
print(conjunto_numerico)

# ADIÇÃO
print('- - - - Médoto .add() adiciona um elemento ao conjunto - - - - \n')
conjunto_numerico.add(5)
print(conjunto_numerico)
print('---------------------------\n')
# REMOÇÃO
print('- - - - Médoto .discard() descarta um elemento do conjunto - - - - \n')
conjunto_numerico.discard(2)
print(conjunto_numerico)
print('---------------------------\n')

# UNIÃO
print('- - - - UNIÃO - - - - \n')
conjunto_A = {1, 2, 3, 4, 5}
conjunto_B = {5, 6, 7, 8}

print('conjunto A = {}'.format(conjunto_A))
print('conjunto B = {}'.format(conjunto_B))
print('A união se dá com o método UNION()')
print('conjunto_C = conjunto_A.union(conjunto_B)')
conjunto_C = conjunto_A.union(conjunto_B)
print('conjunto C = {}'.format(conjunto_C))
print('---------------------------\n')



# INTESECÇÃO
print('A Intersecção se dá com o método INTERSECTION()')
print('conjunto_D = conjunto_A.intersection(conjunto_B)')
conjunto_D = conjunto_A.intersection(conjunto_B)
print('conjunto D = {}'.format(conjunto_D))
print('---------------------------\n')


# DIFERENÇA
print('A diferença se dá com o método DIFFERENCE()')
print('O ordem dos conjuntos interfere no resultado')
print('conjunto_E = conjunto_A.difference(conjunto_B)')
conjunto_E = conjunto_A.difference(conjunto_B)
print('conjunto E = {}'.format(conjunto_E))
print('---------------------------\n')
print('conjunto_E = conjunto_A.difference(conjunto_B)')
conjunto_F = conjunto_B.difference(conjunto_A)
print('conjunto F = {}'.format(conjunto_F))
print('---------------------------\n')



# DIFERENÇA SIMÉTRICA
print('A diferença simétrica se dá com o método SYMMETRIC_DIFFERENCE()')
print('conjunto_E = conjunto_A.symmetric_difference(conjunto_B)')
conjunto_G = conjunto_A.symmetric_difference(conjunto_B)
print('conjunto G = {}'.format(conjunto_G))
print('---------------------------\n')


# FUNÇÃO ISSUBSET - Verifica o um conjunto é subconjunto do outro, retorna um booleano.
print('FUNÇÃO ISSUBSET - Verifica o um conjunto é subconjunto do outro, retorna um booleano.')
conjunto_H = {1, 2, 3}
conjunto_I = {1, 2, 3, 4, 5}
conjunto_subSet_1 = conjunto_H.issubset(conjunto_I)
conjunto_subSet_2 = conjunto_I.issubset(conjunto_H)
print(conjunto_subSet_1)
print(conjunto_subSet_2)
print('---------------------------\n')

# FUNÇÃO ISSUPERSET - Verifica o um conjunto é superconjunto do outro, retorna um booleano.
print('FUNÇÃO ISSUPERSET - Verifica o um conjunto é superconjunto do outro, retorna um booleano.')
conjunto_subSet_3 = conjunto_H.issuperset(conjunto_I)
conjunto_subSet_4 = conjunto_I.issuperset(conjunto_H)
print(conjunto_subSet_3)
print(conjunto_subSet_4)
print('---------------------------\n')


# REMOÇÃO DE DUPLICIDADES DE LISTAS UTILIZANDO CONJUNTOS
lista = ['cachorro', 'gato', 'cachorro', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
print(type(conjunto_animais))
listAnimais = list(conjunto_animais)
print(listAnimais)
print(type(listAnimais))



# FIM DA ATLA 6