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