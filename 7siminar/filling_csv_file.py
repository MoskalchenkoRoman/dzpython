from view import get_dict as get

dict = str(get())
def write_csv():
    file = 'Phone_dictionary.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        print(dict)
        data.write(f'{dict}\n')
