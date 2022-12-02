import csv

def reading():
    with open ('Phone_dictionary.csv',  encoding = 'utf-8') as data:
        reader = csv.reader(data)
        for row in reader:
            print(' '.join(row)) 