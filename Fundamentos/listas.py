# Parte 1
lista = []
print(type(lista))

#help(list)

print(len(lista))
lista.append(1)
lista.append(5)
print(lista)
print(len(lista))

nova_lista = ['Ana', 'Bia', 1, 2]
print(nova_lista)
nova_lista.remove(2)
print(nova_lista)
nova_lista.reverse()
print(nova_lista)

# Part 2
lista2 = [1, 5, 'Rebeca', 'Guilherme', 3.1415]
print(lista2.index('Guilherme'))
lista2[2]
1 in lista2
'Receba' in lista2
'Pedro' not in lista2
lista[-1]
lista[-5]