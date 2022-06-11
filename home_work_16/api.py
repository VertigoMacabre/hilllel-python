import os

import requests

from entities import City, Country, Currency, CurrencyConversion
from errors import BadHttpRequest, CityNotFoundError, CurrencyNotFound


class Api:

    def __init__(self):
        self.request = requests.Session()

    def find_cities(self, city_names: list[str]) -> list[City]:
        self.request.headers.update({'X-Api-Key': os.getenv("API_NINJAS_KEY")})

        cities_list: list[City] = []

        for city_name in city_names:
            api_url = os.getenv("API_NINJAS_CITY_URL") + city_name
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
        self.request.headers.update({'X-Api-Key': os.getenv("API_NINJAS_KEY")})

        api_url = os.getenv("API_NINJAS_COUNTRY_URL") + country_code
        country_response = self.request.get(api_url)

        if country_response.status_code != 200:
            raise BadHttpRequest(country_response.status_code, f"{country_response.text}, {country_code}")

        currency: Currency = Currency(name=country_response.json()[0]['currency']['name'],
                                      code=country_response.json()[0]['currency']['code'])

        return Country(name=country_response.json()[0]['name'], code=country_response.json()[0]['iso2'],
                       currency=currency)

    def currency_converter(self, want: str, date: str) -> CurrencyConversion:

        api_url = os.getenv("RAPID_CURRENCY_CONVERTER_URL")

        request_params = {
            "valcode": want,
            "date": date,
            "json": True
        }

        currency_convention_response = self.request.get(api_url, params=request_params)

        if currency_convention_response.status_code != 200:
            raise BadHttpRequest(currency_convention_response.status_code,
                                 f"{currency_convention_response.text}, {currency_convention_response}")

        if len(currency_convention_response.json()) == 0:
            raise CurrencyNotFound(want)

        if "cc" not in currency_convention_response.json()[0]:
            raise BadHttpRequest(code=currency_convention_response.status_code,
                                 message=currency_convention_response.text)

        currency_convention_response_json = currency_convention_response.json()[0]

        return CurrencyConversion(
            name=currency_convention_response_json['txt'],
            code=currency_convention_response_json['cc'],
            exchange_date=currency_convention_response_json['exchangedate'],
            rate=currency_convention_response_json['rate'],
        )
