"""
Functions that operate on csv files
"""

import requests
import csv
from datetime import datetime
import os
import petl as etl

PEOPLE_API = 'https://swapi.dev/api/people/'
CSV_FILES_DIR = f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/utils/data/'
CSV_HEADERS = ['name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'homeworld']


def handler():  # taken from the API
    res = requests.get(PEOPLE_API)
    return res


def generate_filename():
    today = datetime.today()
    filename = today.strftime('%Y%d%m%H%M%S%f')[:-5]  # removing redundant characters - purpose to make a file unique

    return f'{filename}.csv', today


def get_homeworld(url):
    res = requests.get(url)
    return res.json()['name']


def download_data_from_api():
    """Download data from starwars api and save it to file"""
    data = handler().json()
    filename, download_date = generate_filename()
    file = f'{CSV_FILES_DIR}{filename}'

    try:
        file = open(file, 'w')
        for line in data['results']:
            file.write(
                f'{line["name"]},'
                f'{line["height"]},'
                f'{line["mass"]},'
                f'{line["hair_color"].replace(",", "_")},'
                f'{line["skin_color"].replace(",", "_")},'
                f'{line["eye_color"].replace(",", "_")},'
                f'{line["birth_year"]},'
                f'{line["gender"]},'
                f'{get_homeworld(line["homeworld"])}')
            file.write('\n')
    except Exception as e:
        print(e)
        raise Exception('Error during writing to csv file')

    return filename, download_date


def convert_from_csv(filename):
    """Converts data from csv to easy to use format"""
    filepath = f'{CSV_FILES_DIR}{filename}'
    file = open(filepath, "r")
    data = list(csv.reader(file, delimiter=","))
    file.close()

    return data


def get_value_count(filename):
    dict_values = {}
    data = convert_from_csv(filename)
    data.insert(0, CSV_HEADERS)
    value_count = etl.valuecounter(data, 'homeworld')
    for person in value_count:
        dict_values[person] = value_count[person]
    return dict_values
