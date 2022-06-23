# Part 1
pessoa = {'nome': 'Gabriel', 'idade': 18, 'cursos': ['Inglês', 'Web']}
print(type(pessoa))
len(pessoa)

pessoa['nome']
pessoa['idade']
pessoa['cursos']
pessoa['cursos'][1]

pessoa.keys()
pessoa.values()
pessoa.items()
pessoa.get('idade')

pessoa.get('tags', [])

# Part 2
pessoa2 = {'nome': 'Prof. Glaciete', 'idade': 63, 'cursos': ['Matemática']}
pessoa2['idade'] = 44
pessoa2['cursos'].append('Geometria')
print(pessoa2)
pessoa2.pop('idade')
print(pessoa2)
pessoa2.update({'idade': 64, 'sexo': 'F'})
del pessoa2['cursos']
print(pessoa2)
pessoa2.clear()
print(pessoa2)