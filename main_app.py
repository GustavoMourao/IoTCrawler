import os
import sys
import requests
import time
import logging
from datetime import datetime
from dotenv import load_dotenv
from Database.Database import Database
from Database.cidades import Cidades
from Database.meteorologia import Meteorologia


def collect_raw_data(log_info, api_key, base_url, city_name):
    """
    Collect environment variables from specified city based on
    openweathermap api.
    Args:
    ---------
        log_info: object used to storage log information
        api_key: login api key
        base_url: url of api
        city_name: name of the city
    Return:
    ---------
        nothing..
    """
    final_url = base_url + "appid=" +\
        api_key + "&q=" + city_name

    weather_data = requests.get(final_url).json()

    cities = []
    cities.append(
        Cidades(
            city_name,
            weather_data['coord']['lat'],
            weather_data['coord']['lon']
        )
    )

    # INSERE SOMENTE UMA VEZ: REFATORAR!
    db = Database()
    # db.insert(cities)
    cidades = db.read(Cidades)

    # De tempos em tempos, ler os dados e povoar a base (a cada minuto)!
    start_time = time.time()
    while True:
        log_info.warning('Collecting data...')
        weather_data = requests.get(final_url).json()
        mtr_data = []
        mtr_data.append(
            Meteorologia(
                cidades[0].Id,
                datetime.now(),
                weather_data['clouds']['all'],
                weather_data['main']['humidity'],
                weather_data['main']['pressure'],
                weather_data['main']['temp'],
                weather_data['main']['feels_like'],
                weather_data['wind']['deg'],
                weather_data['wind']['speed']
            )
        )
        db.insert(mtr_data)

        time.sleep(60.0 - ((time.time() - start_time) % 60.0))


if __name__ == '__main__':
    """
    Main function.
    """
    logging.basicConfig(
        filename='LogExtractorClass.log',
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    log = logging.getLogger('LogExtractorClass.log')

    load_dotenv()
    try:
        api_key = os.getenv('OPENWEATHERMAP_API_KEY')
        base_url = os.getenv('BASE_URL')
    except Exception as ex:
        log.warning(ex)
        sys.exit(1)

    collect_raw_data(
        log,
        api_key,
        base_url,
        "Joinville"
    )
