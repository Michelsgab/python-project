produto = {'nome': 'Lenovo', 'preco': 2900, 'estoque': 71}


for chave in produto:
    print(chave)


for valor in produto.values():
    print(valor)


for chave, valor in produto.items():
    print(chave, '=', valor)