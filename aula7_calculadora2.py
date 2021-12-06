class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b
    
    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

calc = Calculadora()

print(calc.soma(10, 2))
print(calc.subtracao(10, 2))
print(calc.divisao(10, 2))
print(calc.multiplicacao(10, 2))
