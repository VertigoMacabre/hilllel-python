import json
import sys
import requests
import os
from dotenv import load_dotenv

load_dotenv()


class Currency:
    code: str
    name: str

    def __init__(self, code: str, name: str):
        self.name = name
        self.code = code

    def __str__(self):
        return f"{self.name}({self.code})"


class Country:

    def __init__(self, name: str, code: str, currency: Currency):
        self.name = name
        self.currency = currency
        self.code = code

    def __str__(self):
        return self.name


class City:

    def __init__(self, name: str, population: int, country: Country, is_capital: bool):
        self.name = name
        self.population = population
        self.country = country
        self.is_capital = is_capital

    def __str__(self):
        return f"{self.name} is {'capital' if self.is_capital else 'city'} of {self.country} " \
               f"with population {self.population} people " \
               f"official currency is {str(self.country.currency)}"


class CityNotFoundError(Exception):
    def __str__(self):
        return "There is no one city fond"


class BadHttpRequest(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"Error: {self.code}, {self.message}"


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


def render_table(cities: list[City]):
    max_city_name: int = len(max(cities, key=lambda c: c.name).name)
    max_country_name: int = len(max(cities, key=lambda c: c.country.name).country.name)
    max_city_population: int = len(str(max(cities, key=lambda c: c.population).population))
    max_currency_name: int = len(max(cities, key=lambda c: c.country.currency.name).country.currency.name)

    city_label = "City"
    country_label = "Country"
    population_label = "Population"
    currency_label = "Currency"

    header = "  | "

    city_header = city_label + (
        " " * (max_city_name - len(city_label)) if max_city_name - len(city_label) > 0 else max_city_name)
    header = header + city_header
    header = header + " | "

    country_header = country_label + (" " * (max_country_name - len(country_label)) if max_country_name - len(
        country_label) > 0 else max_country_name)

    header = header + country_header
    header = header + " | "

    population_header = population_label + (
            " " * (max_city_population - len(population_label) if max_city_population - len(
        population_label) > 0 else max_city_population))

    header = header + population_header

    header = header + " | "

    currency_header = currency_label + (" " * (
        max_currency_name - len(currency_label) if max_currency_name - len(currency_label) > 0 else max_currency_name))
    header = header + currency_header
    divider = "-" * len(header)
    print(header)
    print(divider)

    row_number = 0

    for city in cities:
        row_number += 1
        row = str(row_number) + " | "
        row = row + city.name + (" " * (len(city_header) - len(city.name)))

        row = row + " | "
        row = row + city.country.name + (" " * (len(country_header) - len(city.country.name)))

        row = row + " | "
        row = row + str(city.population) + (" " * (len(population_header) - len(str(city.population))))

        row = row + " | "
        row = row + city.country.currency.name + (" " * (len(country_header) - len(city.country.currency.name)))

        print(row)
        print(divider)


if __name__ == "__main__":
    # python get_city_info.py odessa, kyiv, lviv
    useless_param, *cities = sys.argv
    api: Api = Api()

    try:
        cities = api.find_cities(cities)

        # for city in cities:
        #     print(city)

        render_table(cities)

    except (CityNotFoundError, BadHttpRequest) as err:
        print(err)
