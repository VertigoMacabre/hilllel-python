class CityNotFoundError(Exception):
    def __str__(self):
        return "There is no one city fond"


class BadHttpRequest(Exception):

    def __init__(self, code, message):
        self.code = code
        self.message = message

    def __str__(self):
        return f"Error: {self.code}, {self.message}"
