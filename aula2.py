
# não é informado tipo da variável
a = 10
b = 5

# operações simples da matemática
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

# O comando print() é utilizado para exibir informações na tela
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(resto)

# print('soma: ' + soma)        -> vai dar erro, pois não vai ser possível concatenar a stringo com um inteiro, é preciso converter o int para string.
print(type(soma))               # O comando 'type()' - retorna o tipo da variável.
soma = str(soma)                # O comando 'str()' - converte o valor para string.
print(type(soma))
print('soma: ' + soma)          # pode ser feito desse jeito também 'print('soma: ' + str(soma))', caso não queira mudar o tipo da variável.

print(type(divisao))
print(int(divisao))             # O comando 'int()' - converte o valor para inteiro - Tomar cuidado, pois alguns valores podem não ser passíveis de conversão - A1.
print(int(soma))
print(type(soma))
soma = int(soma)
print(type(soma))

# x = 'A1'
# y = int(x)                    # Neste exemplo vai retornar um erro, pois não é possível essa conversão!

print('soma: {}' .format(soma)) # A função format é um das mais utilizadas para esse tipo de concatenação

print('Soma: {}. Subtração: {}'.format(soma, subtracao))
# No exemplo de utilização do 'format' acima as variáveis precisar seguir a mesma ordem.

print('Soma: {x}. Subtração: {y}'.format(y=subtracao, x=soma))
# Nesse exemplo acima, podemos inserir um apelido dentro das chaves, 
# assim podemos colocar as variáveis em qualquer ordem, porém é obrigatório, informa qual variável pertence a qual apelido.

# \n - efetua uma quebra de linha
print('Soma: {so}. '
      '\nSubtração: {su}. '
      '\nMultiplicação: {m}. '
      '\nDivisão: {d}. '
      '\nResto: {r}'.format(su=subtracao, 
                            m=multiplicacao,
                            so=soma,
                            d=divisao,
                            r=resto))

# input - O comando input fornece uma interação com o usuário

c = input('Entre com o 1. valor: ')
d = input('Entre com o 2. valor: ')

print(type(c))
print(c)
print(type(d))
print(d)

# Os valores capturados pelo comando input são sempre do tipo string, mesmo o usuário digitando números, 
# para armazená-los com outro tipo é necessário efetuar a conversão dos mesmo.

e = int(input('Entre com o 3. valor: '))
f = float(input('Entre com o 4. valor: '))

print(type(e))
print(e)
print(type(f))
print(f)
