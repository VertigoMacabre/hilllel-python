class CityNotFoundError(Exception):
    def __str__(self):
        return "There is no one city fond"


class BadHttpRequest(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"Error: {self.code}, {self.message}"


class CurrencyNotFound(Exception):

    def __init__(self, currency_code: str):
        self.currency_code = currency_code

    def __str__(self):
        return f"Error: {self.currency_code} not found"
