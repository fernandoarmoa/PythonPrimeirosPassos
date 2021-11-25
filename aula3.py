# INICIO DA AULA 3

# a = int(input('1. valor: '))
# b = int(input('2. valor: '))
# c = int(input('3. valor: '))

# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é {}'.format(b))
# else:
#     print('o maior número é {}'.format(c))

# d = int(input('Entre com um número: '))
# resto_d = d % 2

# if resto_d == 0:
#     print('número é par')
# else:
#     print('número é ímpar')


# e = int(input('Entre com o 1. número: '))
# f = int(input('Entre com o 2. número: '))
# resto_e = e % 2
# resto_f = f % 2

# if resto_e == 0 or not resto_f != 0:
#     print('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')


# ALTERNATIVA 1 DE FAZER - VEFICANDO NO IF TODAS AS NOTAS DIGITADAS
# nota1 = int(input('1. Bimestre: '))
# nota2 = int(input('2. Bimestre: '))
# nota3 = int(input('3. Bimestre: '))
# nota4 = int(input('4. Bimestre: '))
# media = (nota1 + nota2 + nota3 + nota4) / 4

# if nota1 <= 10 and nota2 <= 10 and nota3 <= 10 and nota4 <= 10:
#     print('méida: {}'.format(media))
# else:
#     print('foi informado alguma nota errada')

# ALTERNATIVA 2 DE FAZER
nota1 = int(input('1. Bimestre: '))
if nota1 > 10:
    nota1 = int(input('Você digitou uma nota inválida! 1. Bimestre: '))
nota2 = int(input('2. Bimestre: '))
if nota2 > 10:
    nota2 = int(input('Você digitou uma nota inválida! 2. Bimestre: '))
nota3 = int(input('3. Bimestre: '))
if nota3 > 10:
    nota3 = int(input('Você digitou uma nota inválida! 3. Bimestre: '))
nota4 = int(input('4. Bimestre: '))
if nota4 > 10:
    nota4 = int(input('Você digitou uma nota inválida! 4. Bimestre: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print('méida: {}'.format(media))

print('final do programada')

# FIM DA AULA 3
