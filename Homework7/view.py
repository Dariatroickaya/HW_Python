import sys
from controller import file_none


def get_dict():
    print('''Введите команду из списка:
        1 просмотр файла
        2 добавить запись''')

    x = int(input('Ваш выбор: '))
    if x == 1:
        file_none()
        sys.exit()

    elif x == 2:
    
        dict = ''
        id = input ('Введите порядковый номер: ')
        dict += id + ' '
        surname = input('Введите фамилию: ')
        dict += surname + ' '
        name = input('Введите имя: ')
        dict += name + ' '
        birth_day = input('Введите дату рождения в формате ДДММГГ: ')
        dict += birth_day + ' '
        work_pl = input('Введите название организации: ')
        dict += work_pl + ' '
        ph_numb1 = input('Введите номера телефона через , : ')
        dict += ph_numb1 + ' '
        return dict
    
    else:
        print('Такого варианта нет')