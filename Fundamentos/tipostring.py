# Part 1
dir(str)

nome = 'Gabriel Michels'
# print(nome[0]) - String são imutáveis

# marca 'dÁgua
print("Dias D'Avilla" == 'Dias D\'Avilla')

texto = 'Texto entre apostrófes pode ter "aspas"'
texto2 = "Texto em aspas pode ter 'apostrófes'"

print(texto, texto2)

print("""
Esse texto está
utilizando múltiplas linhas
em python
""")

print('Outra forma de utilizar múltiplas\nlinhas')

# Part 2
nome = "Nathalie"
print(nome[0])
print(nome[6])
print(nome[-3])
print(nome[:])
print(nome[::-1])

numeros = '1234567890'
print(numeros[::])
print(numeros[::2])
print(numeros[1::2])
print(numeros[::-1])
print(numeros[::-2])

# Part 3
frase = 'Python é uma excelente linguagem de programação'
print('Py' in frase)
print(len(frase))
print(frase.upper())
print(frase.lower())

print(frase.split())
print(frase.split('e'))

# Part 4
a = '123'
b = 'de Oliveira 4'
print(a.__add__(b))
print(str.__add__(a, b))

len(a)
print(a.__len__())
print('1' in a)
print(a.__contains__('1'))