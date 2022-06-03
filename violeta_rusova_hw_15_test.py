import unittest
from unittest import mock

import violeta_rusova_hw_15
from violeta_rusova_hw_15 import get_weather_by_city, get_current_weather

RESPONSE_PRESET = {
    "coord": {
        "lon": 30.7326,
        "lat": 46.4775
    },
    "weather": [
        {
            "id": 802,
            "main": "Clouds",
            "description": "scattered clouds",
            "icon": "03d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 300.41,
        "feels_like": 300.82,
        "temp_min": 300.41,
        "temp_max": 300.41,
        "pressure": 1018,
        "humidity": 50,
        "sea_level": 1018,
        "grnd_level": 1012
    },
    "visibility": 10000,
    "wind": {
        "speed": 5.56,
        "deg": 14,
        "gust": 6.56
    },
    "clouds": {
        "all": 41
    },
    "dt": 1654266113,
    "sys": {
        "country": "UA",
        "sunrise": 1654222033,
        "sunset": 1654278209
    },
    "timezone": 10800,
    "id": 698740,
    "name": "Odessa",
    "cod": 200
}


def make_mocked_response(*args, **kwargs):
    class MockResponse:
        def __init__(self, data):
            self.data = data

        def json(self):
            return self.data

    return MockResponse( RESPONSE_PRESET)


class TestWeatherApp(unittest.TestCase):

    def test_it_should_return_status_200(self):
        response = get_weather_by_city("ODESSA")
        self.assertEqual(response.status_code, 200)

    def test_url_should_contain_api_query_params(self):
        city_name: str = "CityName"
        complete_url = violeta_rusova_hw_15.BASE_URL + "appid=" + violeta_rusova_hw_15.API_KEY + "&q=" + city_name
        current_url = get_weather_by_city("CityName").url
        self.assertEqual(complete_url, current_url)

        city_name = "CityName1"
        complete_url = violeta_rusova_hw_15.BASE_URL + "appid=" + violeta_rusova_hw_15.API_KEY + "&q=" + city_name
        current_url = get_weather_by_city("CityName").url

        self.assertTrue(complete_url != current_url)

    def test_response_should_has_main_field(self):
        response = get_weather_by_city("ODESSA").json()
        self.assertTrue("main" in response)

    @mock.patch('violeta_rusova_hw_15.requests.get', side_effect=make_mocked_response)
    def test_temp_should_be_in_Celsius(self, mock_get):
        weather = get_current_weather("Kiev")
        temp_in_celsius = round(RESPONSE_PRESET['main']['temp'] - 273.15)
        self.assertEqual(weather['temp'], temp_in_celsius)



if __name__ == '__main__':
    unittest.main()
