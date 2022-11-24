import csv

def reading():
    file = 'Phone_dictionary.csv'
    with open (file,  encoding = 'utf-8') as data:
        reader = csv.reader(data)
        for row in reader:
            print(' '.join(row))  