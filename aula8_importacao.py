from aula7_televisao import Televisao
from aula8_contador_letras import contador_letras

lista = ['cachorro', 'gato', 'elefante']
print('total de letras por palavra da lista: {}'.format(contador_letras(lista)))



tv = Televisao()
print(tv.ligada)
tv.power()
print(tv.ligada)
