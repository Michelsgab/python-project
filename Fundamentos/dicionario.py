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