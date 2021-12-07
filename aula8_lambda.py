contador_letras = lambda lista: [len(x) for x in lista]
soma = lambda a, b: a + b
subtracao = lambda a, b: a - b

calc = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b
}

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))
print(soma(5, 10))
print(subtracao(10, 5))

print(type(calc))
somar = calc['soma']
multiplicar = calc['multiplicacao']

print('A soma é: {}'.format(somar(11, 9)))
print('A multiplicação é: {}'.format(multiplicar(11, 9)))


