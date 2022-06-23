def get_dia_semana(dia):
    dias = {
        1: 'Domingo',
        2: 'Segunda',
        3: 'Terça',
        4: 'Quarta',
        5: 'Quinta',
        6: 'Sexta',
        7: 'Sábado'
    }
    return dias.get(dia, 'Dia inválido')


if __name__ == '__main__':
    for dia in range(0, 9):
        if dia == 1:
            print(f'{dia}: {get_dia_semana(dia)} - Fim de semana')
        if dia == 7:
            print(f'{dia}: {get_dia_semana(dia)} - Fim de semana')
        if dia != 1 and dia != 7:
            print(f'{dia}: {get_dia_semana(dia)}')

