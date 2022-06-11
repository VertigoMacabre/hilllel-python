import os

import requests

from entities import City, Country, Currency
from errors import BadHttpRequest, CityNotFoundError


class Api:

    def __init__(self):
        self.request = requests.Session()
        self.request.headers.update({'X-Api-Key': os.getenv("API_KEY")})

    def find_cities(self, city_names: list[str]) -> list[City]:

        cities_list: list[City] = []

        for city_name in city_names:
            api_url = os.getenv("API_CITY_URL") + city_name
            cities_response = self.request.get(api_url)

            if cities_response.status_code != 200:
                raise BadHttpRequest(cities_response.status_code, f"{cities_response.text}, {city_name}")

            for c in cities_response.json():
                country = self.find_county(c['country'])
                city = City(name=c['name'], population=c['population'], country=country, is_capital=c['is_capital'])
                cities_list.append(city)

        if len(cities_list) == 0:
            raise CityNotFoundError

        return cities_list

    def find_county(self, country_code) -> Country:
        api_url = os.getenv("API_COUNTRY_URL") + country_code
        country_response = self.request.get(api_url)

        if country_response.status_code != 200:
            raise BadHttpRequest(country_response.status_code, f"{country_response.text}, {country_code}")

        currency: Currency = Currency(name=country_response.json()[0]['currency']['name'],
                                      code=country_response.json()[0]['currency']['code'])

        return Country(name=country_response.json()[0]['name'], code=country_response.json()[0]['iso2'],
                       currency=currency)
