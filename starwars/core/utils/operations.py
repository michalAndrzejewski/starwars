"""
Functions that operate on csv files
"""

import requests
import csv
from datetime import datetime
import os

PEOPLE_API = 'https://swapi.dev/api/people/'
CSV_FILES_DIR = f'{os.path.abspath(os.path.dirname(os.path.dirname(__file__)))}/utils/data/'


def handler():  # taken from the API
    res = requests.get(PEOPLE_API)
    return res


def generate_filename():
    today = datetime.today()
    filename = today.strftime('%Y%d%m%H%M%S%f')[:-5]  # removing redundant characters - purpose to make a file unique

    return f'{filename}.csv', today


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
                f'{line["homeworld"]}')
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
