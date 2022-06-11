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
