import requests
import csv
from datetime import datetime

PEOPLE_API = 'https://swapi.dev/api/people/'


def handler():  # taken from the API
    res = requests.get(PEOPLE_API)
    return res


def generate_filename():
    today = datetime.today()
    filename = today.strftime('%Y%d%m%H%M%S%f')[:-5]  # removing redundant characters - purpose to make a file unique

    return f'{filename}.csv', today


def download_data_from_api():
    data = handler().json()
    path = 'data/'
    filename, download_date = generate_filename()
    file = f'C:/Users/miad/PycharmProjects/starwars/starwars/core/utils/{path}{filename}'

    try:
        file = open(file, 'w')
        print('FILE WAS OPENED')
        for line in data['results']:
            file.write(
                f'{line["name"]},'
                f'{line["height"]},'
                f'{line["mass"]},'
                f'{line["hair_color"]},'
                f'{line["skin_color"]},'
                f'{line["eye_color"]},'
                f'{line["birth_year"]},'
                f'{line["gender"]},'
                f'{line["homeworld"]}')
            file.write('\n')
        print("SUCCESSED WRITING")
    except Exception as e:
        print(e)
        raise Exception('Error during writing to csv file')

    '''Metadata.objects.create(
        filename=filename,
        download_date=download_date
    )'''

    return filename, download_date
