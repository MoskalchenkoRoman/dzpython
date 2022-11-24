from bazabd import *
import logging

logging.basicConfig(filename="newfile.log", level='INFO')
logger=logging.getLogger() 



def uzers():
    conn = create_bd()
    cur = conn.cursor()
    create_schema_db(cur, conn)
    while True:
        print("""Выберите команду
            1 - Просмотреть БД
            2 - Добавить записть
            3 - Удалить запись
            4 - Изменить запись
            0 - ВЫХОД""")
        
        x = int(input('Ваш выбор : '))
        if x == 1:
            print (vizual(cur))
        elif x == 2:
            femili, name, telehon = input_data()
            add_us(cur, conn, femili, name, telehon)
        elif x == 3:
            num = int(input('Введите ID для удаления : '))
            delit(cur, conn, num)
        elif x == 4:
            num = int(input('Введите ID для замены : '))
            femili, name, telehon = input_data()
            delit(cur, conn, num)
            add_us(cur, conn, femili, name, telehon)
        elif x == 0:
            break
    print('Были не очень то и рады')
    exit()


def input_data():
    femili = input('Введите Фамилию :')
    name = input('Введите Имя :')
    telehon = input('Введите телефон :')
    logger.info(f'new fameli =  {femili}')
    return femili, name, telehon

