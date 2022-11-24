from os.path import exists
from filling_csv_file import write_csv
from creating_file import creating

path = 'Phone_dictionary.csv'
valid = exists(path)
if not valid:
    creating()

write_csv()