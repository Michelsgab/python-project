palavra = 'paralelepípedo'
for letra in palavra:
    print(letra, end=',')


aprovados = ['Gabriel', 'Fabrício', 'Victor', 'Allef']
for nomes in aprovados:
    print(nomes)


for posicao, nomes in enumerate(aprovados):
    print(posicao + 1, '-' + nomes)


dias_semana = ('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')
for dia in dias_semana:
    print(f'Hoje é {dia}')


for letra in set('muito legal'):
    print(letra)


for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)