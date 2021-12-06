from typing import OrderedDict


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 5

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumentaCanal(self):
        if self.ligada:
            self.canal += 1

    def diminuiCanal(self):
        if self.ligada:
            self.canal -= 1

tv = Televisao()
print('A TV está ligada? {}'.format(tv.ligada))
tv.power()
print('A TV está ligada? {}'.format(tv.ligada))
tv.power()
print('A TV está ligada? {}'.format(tv.ligada))
tv.power()
tv.aumentaCanal()
tv.aumentaCanal()
print('Cana: {}'.format(tv.canal))
tv.diminuiCanal()
print('Cana: {}'.format(tv.canal))
