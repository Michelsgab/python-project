from random import randint


# for i in range(1, 11):
#     if i == 6:
#         break
#     print(i)
# else:
#     print('Fim!')


def sortear_dados():
    return randint(1, 6)


for i in range(1, 7):
    if i % 2 == 1:
        continue
    if sortear_dados() == i:
        print('ACERTOU!', i)
        break
else:
    print('Não acertou o número')

