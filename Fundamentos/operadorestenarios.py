esta_chuvendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas.')[not esta_chuvendo])


print('Hoje estou com as roupas ' + ('molhadas.' if esta_chuvendo else 'secas.'))