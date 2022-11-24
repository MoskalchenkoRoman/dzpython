def creating():
    file = 'Phone_dictionary.csv'
    with open(file, 'w', encoding = 'utf-8') as data:
        data.write(f'id Фамилия Имя День_Рождения Место_работы Номер_телефона Доп_телефон\n')