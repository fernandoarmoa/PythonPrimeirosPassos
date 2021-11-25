# INICIO DA AULA 4

# LAÇO DE REPETIÇÃO FOR COM RANGE

# RANGE([POSIÇÃO INICIAL] - Opcional, POSIÇÃO FINAL - 1)

# for x in range(100):    # PODE SER ESPECIFICA APENAS O LIMITE, NESTE SERÃO 100 NÚMEROS, INICIANDO DO 0, SERÁ MOSTRADO DO 0 ATÉ 99
#     print(x)

# for x in range(1, 100):    # PODE SER ESPECIFICA DE ONDE QUEREMOS PARTIR E O LIMITE, NESTE SERÃO 99 NÚMEROS, INICIANDO DO 1, SERÁ MOSTRADO DO 0 ATÉ 99
#     print(x)

# for x in range(90, 100):    # NESTE SERÃO 10 NÚMEROS, INICIANDO DO 90, SERÁ MOSTRADO DO 90 ATÉ 99
#    print(x)

# EXERCÍCIO PARA DESCOBRI E MOSTRAR APENAS OS NÚMEROS PRIMOS ( DIVISÍVEL APENAS PELO 1 E POR SI MEMSO)

# IMPRIME TODOS OS NÚMEROS PRIMOS EXISTENTES NO RANGE

# x = int(input('Entre com um número: '))

# qtdeDePrimos = 0

# for num in range(x + 1):
#     div = 0
#     for x in range(1,num + 1):
#         resto = num % x
#         if resto == 0:
#             div += 1
         

#     if div == 2:
#         qtdeDePrimos += 1
#         print('número {} é primo'.format(num))

# print('A quantidade de números primos existente entre 1 e {valor} é de: {qtde}'.format(qtde=qtdeDePrimos, valor=x))
    # else:
    #    print('número {} não é primo'.format(num))


# VERIFICA SE UM DADO NÚMERO É PRIMO
# y = int(input('Entre com o número: '))
# div = 0

# for x in range(1, y + 1):
#     resto = y % x
#     if resto == 0:
#         div += 1

# if div == 2:
#     print('número {} é primo'.format(y))
# else:
#     print('número {} não é primo'.format(y))

# LAÇO DE REPEITÇÃO WHILE
# ENQUANTO DETERMINADA CONDIÇÃO FOR VERDADEIRA EXECUTA, A CONDIÇÃO FALSA SAI DO LOOP

n1=0
n2=0
n3=0
n4=0
notasDigitadas = 1

while (notasDigitadas <= 4):

    count = 1

    if notasDigitadas == 1:

        notaDigitada = int(input('Entre com a 1. nota: '))

        while (notaDigitada < 0 or notaDigitada > 10):
            print('Nota inválida, digite apenas valores de 0 à 10.')
            notaDigitada = int(input('Entre com a 1. nota: '))

        n1 = notaDigitada
        notasDigitadas += 1

    elif notasDigitadas == 2:

        notaDigitada = int(input('Entre com a 2. nota: '))

        while (notaDigitada < 0 or notaDigitada > 10):
            print('Nota inválida, digite apenas valores de 0 à 10.')
            notaDigitada = int(input('Entre com a 2. nota: '))

        n2 = notaDigitada
        notasDigitadas += 1

    elif notasDigitadas == 3:

        notaDigitada = int(input('Entre com a 3. nota: '))
        
        while (notaDigitada < 0 or notaDigitada > 10):
            print('Nota inválida, digite apenas valores de 0 à 10.')
            notaDigitada = int(input('Entre com a 3. nota: '))

        n3 = notaDigitada
        notasDigitadas += 1

    else:

        notaDigitada = int(input('Entre com a 4. nota: '))
        
        while (notaDigitada < 0 or notaDigitada > 10):
            print('Nota inválida, digite apenas valores de 0 à 10.')
            notaDigitada = int(input('Entre com a 4. nota: '))

        n4 = notaDigitada
        notasDigitadas += 1
    
    count += 1

media = (n1 + n2 + n3 + n3) / 4
print('Nota 1: {}'.format(n1))
print('Nota 2: {}'.format(n2))
print('Nota 3: {}'.format(n3))
print('Nota 4: {}'.format(n4))
print('Média : {}'.format(media))

# FIM DA AULA 4