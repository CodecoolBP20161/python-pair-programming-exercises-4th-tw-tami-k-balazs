import csv
import sys
from person import Person


def open_csv(file_name):
    with open(file_name, 'rb') as myfile:
        text = myfile.readlines()
        x = [i.strip('\n').split(',')for i in text]
        y = {i[0]: i[1].replace(" ", "").replace("-", "") for i in x}

        print(y)

open_csv("phone_data_1000.csv")
def get_csv_file_name(argv_list):
    return argv_list[0]


def format_output(person):
    # implent this function
    pass  # delete this


def get_person_by_phone_number(person_list, user_input_phone_number):
    # implent this function
    pass  # delete this


def main():
    file_name = get_csv_file_name(sys.argv)
    if file_name is None:
        print('No database file was given.')
        sys.exit(0)

    person_list = open_csv(file_name)
    user_input_phone_number = input('Please enter the phone number: ')
    match_person = get_person_by_phone_number(person_list, user_input_phone_number)

    print(format_output(match_person))

if __name__ == '__main__':
    main()
