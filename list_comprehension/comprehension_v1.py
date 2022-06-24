# [ expressão for item in list of condicional ]

dobros = [i * 2 for i in range(10)]
print(dobros)

# Sem comprehension
dobro = []
for i in range(10):
    dobro.append(i * 2)
print(dobro)