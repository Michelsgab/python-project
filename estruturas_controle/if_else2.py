#!/usr/local/bin/python3


def faixa_etaria(idade):
    if 0 <= idade < 18:
        return 'Menor de idade'
    elif idade in range(18, 64):
        return 'Adulto'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade >= 100:
        return 'Centenário'
    else:
        return 'Idade inválida'


if __name__ == '__main__':
    for idade in (17, 35, 88, 12, 103, -1):
        print(f'{idade}: {faixa_etaria(idade)}')

