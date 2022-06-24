def soma2(a, b):
    return a + b

def soma3(a, b, c):
    return a + b + c

def somaN(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


if __name__ == '__main__':
    print(soma2(2, 3))
    print(soma3(2, 3, 4))

    # Packing
    print(somaN(1, 3))

    # Unpacking
    tupla_nums = (1, 2, 3)
    print(somaN(*tupla_nums))
    lista_nums = [1, 2, 3]
    print(somaN(*lista_nums))
