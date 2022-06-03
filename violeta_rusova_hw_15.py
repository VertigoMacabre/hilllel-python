from typing import Dict, Any

import requests

BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'
STATUS_CODE = 404
ZERO_BY_FAHRENHEIT = 273.15


def get_weather_by_city(city_name: str) -> requests.Response:
    return requests.get(BASE_URL, params={
        "appid": API_KEY,
        "q": city_name
    })


def get_current_weather(city_name) -> dict[str, Any] | None:
    # complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    r_data = get_weather_by_city(city_name).json()

    if r_data["cod"] != str(STATUS_CODE):
        y = r_data['main']
        current_t = y['temp']
        current_p = y["pressure"]
        z = r_data["weather"]
        weather_description = z[0]["description"]

        return {
            "temp": round(current_t - ZERO_BY_FAHRENHEIT),
            "pressure": current_p,
            "description": weather_description
        }
    else:
        return None


if __name__ == '__main__':
    while True:
        city_name: str = input('Please fill up your city \n')
        weather: dict = get_current_weather(city_name)

        if weather:
            print(
                f"Current weather is : {weather['temp']} degrease, {weather['pressure']} p,"
                f" {weather['description']}")

        else:
            print('City not found')
