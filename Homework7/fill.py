from view import get_dict as get

def write_csv():
    dict = str(get())
    with open ('Phone_dictionary.csv', 'a', encoding = 'utf-8') as data:
        print(dict)
        data.write(f'{dict}\n')