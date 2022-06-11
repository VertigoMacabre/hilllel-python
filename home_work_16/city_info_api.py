import sys

from dotenv import load_dotenv

from entities import City
from errors import CityNotFoundError, BadHttpRequest
from api import Api

load_dotenv()


def render_table(cities: list[City]):
    if len(cities) == 0:
        return

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
        " " * (max_city_name - len(city_label)) if max_city_name - len(city_label) >= 0 else max_city_name)
    header = header + city_header
    header = header + " | "

    country_header = country_label + (" " * (max_country_name - len(country_label)) if max_country_name - len(
        country_label) >= 0 else max_country_name)

    header = header + country_header
    header = header + " | "

    population_header = population_label + (
            " " * (max_city_population - len(population_label) if max_city_population - len(
        population_label) >= 0 else max_city_population))

    header = header + population_header

    header = header + " | "

    currency_header = currency_label + (" " * (
        max_currency_name - len(currency_label) if max_currency_name - len(currency_label) >= 0 else max_currency_name))
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
    # python city_info_api.py odessa, kyiv, lviv
    useless_param, *cities = sys.argv
    api: Api = Api()

    try:
        cities = api.find_cities(cities)

        # for city in cities:
        #     print(city)

        render_table(cities)

    except (CityNotFoundError, BadHttpRequest) as err:
        print(err)
