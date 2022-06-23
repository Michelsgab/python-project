# while True:
#     print('Laço infinito')
import random
from random import randint


numero_informado = -1
numero_secreto = random.randint(0, 9)


while numero_informado != numero_secreto:
    numero_informado = int(input('Informe o número: '))


print(f'Número secreto {numero_secreto} foi encontrado!')