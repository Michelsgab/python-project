#!/usr/local/bin/python3


def nota_conceito(valor):
    nota = float(valor)
    if nota > 10:
        return 'Nota inválida'
    elif nota >= 9:
        return 'A'
    elif nota >= 8:
        return 'A-'
    elif nota >= 7:
        return 'B'
    elif nota >= 6:
        return 'B-'
    elif nota >= 5:
        return 'C'
    elif nota >= 4:
        return 'C-'
    elif nota >= 3:
        return 'D'
    elif nota >= 2:
        return 'D-'
    elif nota >= 1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota Inválida'


if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)