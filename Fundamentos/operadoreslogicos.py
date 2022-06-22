print(True or False)
print(7 != 3  and 2 > 3)

# Operação de Negação
not True # False
not False # True

# Desafio
trabalho_terca = True
trabalho_quinta = False
"""
- Confirmando os 2: TV 50' + Sorvete
- Confirmando apenas 1: TV 32' + Sorvete
- Nenhum confirmado: Ficar em casa
"""

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
nenhum = not sorvete
print(f'Tv50={tv_50} Tv32={tv_32} Sorvete={sorvete} Saudável={nenhum}')