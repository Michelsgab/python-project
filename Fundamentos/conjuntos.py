a = {1, 2, 3}
print(type(a))

a = set('magna')
print(a)
print('a' in a, 'f' not in a)
{1, 2, 3} == {3, 2, 1, 2} # True

c1 = {1, 2}
c2 = {2, 3}
print(c1.union(c2))
print(c1.intersection(c2))
c1.update(c2)
print(c1)

print(c2 <= c1)

{1, 2, 3} - {2}

# Conjunto não é indexado
# Não garante ordenação
# Não aceita repetição