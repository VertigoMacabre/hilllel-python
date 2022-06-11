import sys

from dotenv import load_dotenv

from api import Api
from cities_table_render import render_table
from errors import CityNotFoundError, BadHttpRequest

load_dotenv()

if __name__ == "__main__":
    # python city_info.py odessa, kyiv, lviv
    useless_param, *cities = sys.argv
    api: Api = Api()

    try:
        cities = api.find_cities(cities)

        # for city in cities:
        #     print(city)

        render_table(cities)

    except (CityNotFoundError, BadHttpRequest) as err:
        print(err)
