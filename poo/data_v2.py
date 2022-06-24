class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.ano}'


d1 = Data(5, 12, 2022)
# d1.dia = 5
# d1.mes = 12
# d1.ano = 2022
print(d1)

d2 = Data(24, 6, 2022)
# d2.dia = 24
# d2.mes = 6
# d2.ano = 2022
print(d2)
