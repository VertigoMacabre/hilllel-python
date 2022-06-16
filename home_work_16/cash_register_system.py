import enum
import json
import sys
from datetime import date

from home_work_16.api import Api
from home_work_16.entities import CurrencyConversion

commands = ['exchange', 'course']
currencies = ["usd", "uah"]


class Command(enum.Enum):
    COURSE = "course"
    EXCHANGE = "exchange"
    STOP = "stop"


class Currency(enum.Enum):
    USD = "usd"
    UAH = "uah"


class ExchangeData:
    can_exchange: bool
    current_amount: float
    needed_amount: float
    currency: Currency

    def __init__(self, can_exchange: bool, current_amount: float, needed_amount: float, currency: Currency):
        self.can_exchange = can_exchange
        self.current_amount = current_amount
        self.needed_amount = needed_amount
        self.currency = currency


class BalanceService:
    usd_rate: float
    uah_rate: float
    exchange_direction_of_currency = {
        Currency.USD: Currency.UAH,
        Currency.UAH: Currency.USD
    }

    def __init__(self, course: CurrencyConversion):
        self.usd_rate = course.rate
        self.uah_rate = 1 / course.rate

        try:
            with open("balance.json") as file:
                balance_data = json.load(file)
            self.uah = balance_data['uah']
            self.usd = balance_data['usd']
        except FileNotFoundError as e:
            print(e)

    def get_rate_of_currency(self, currency: Currency) -> float:
        return getattr(self, f"{currency.value}_rate")

    def is_available_amount(self, currency: Currency, amount: float) -> ExchangeData:

        return ExchangeData(getattr(self, f"{currency.value}") >= amount,
                            self.get_amount_of_currency(currency),
                            amount * self.get_rate_of_currency(currency),
                            currency
                            )

    def get_amount_of_currency(self, currency: Currency) -> float:
        return int(getattr(self, currency.value))

    def exchange(self, currency: Currency, amount: float):
        exchanged_amount = amount * self.get_rate_of_currency(currency)
        self.update_currency_amount(currency, -amount)
        self.update_currency_amount(self.exchange_direction_of_currency[currency], exchanged_amount)
        self._update()

    def update_currency_amount(self, currency: Currency, amount: float):
        current_amount = getattr(self, currency.value)
        setattr(self, currency.value, current_amount + amount)
        self._update()

    def _update(self):
        with open("balance.json", 'w') as file:
            balance_in_string = json.dumps({
                "uah": self.uah,
                "usd": self.usd
            })

            file.write(balance_in_string)

    def get_balance_to_string(self) -> str:
        return f"UAH:{self.get_amount_of_currency(Currency.UAH)} USD:{self.get_amount_of_currency(Currency.USD)}"


class BalanceMessage:

    def __init__(self, balance: BalanceService, currency: Currency):
        self.balance = balance
        self.currency = currency

    def __str__(self):
        return f"RATE: {self.balance.get_rate_of_currency(currency)}, " \
               f"AVAILABLE {self.balance.get_amount_of_currency(self.currency)}"


class InsufficientFundsError(Exception):

    def __init__(self, exchange_data: ExchangeData):
        self.exchange_data = exchange_data

    def __str__(self):
        return f"UNAVAILABLE, REQUIRED BALANCE {exchange_data.currency.value} {exchange_data.needed_amount}," \
               f" AVAILABLE {exchange_data.current_amount}.".upper()


if __name__ == "__main__":
    while True:
        try:
            # запрашиваем курс в while если он поменяется
            api: Api = Api()
            d = date.today().strftime("%Y%m%d")
            course: CurrencyConversion = api.currency_converter(Currency.USD.value, d)
            balanceService: BalanceService = BalanceService(course)

            command_string = input("COMMAND\n")

            if command_string.lower() == Command.STOP.value:
                print("SERVICE STOPPED")
                sys.exit(1)

            com, cur, *amount = command_string.lower().split(" ")
            if com not in [c.value for c in Command]:
                print(f"unknown command {com}")
                raise ValueError

            if cur not in [c.value for c in Currency]:
                print(f"unavailable currency {cur}")
                raise ValueError

            currency: Currency = Currency(cur)
            command: Command = Command(com)

            if command == Command.COURSE:
                print(BalanceMessage(balanceService, currency))

            elif command == Command.EXCHANGE:

                if len(amount) == 0:
                    raise ValueError("amount option need")

                amount = int(amount[0])

                print(BalanceMessage(balanceService, currency))

                exchange_data: ExchangeData = balanceService.is_available_amount(currency, amount)

                if exchange_data.can_exchange:
                    balanceService.exchange(currency, amount)
                    print(
                        f"OPERATION SUCCESS. CURRENT BALANCE IS:\n{BalanceMessage(balanceService, currency)}")
                else:

                    raise InsufficientFundsError(exchange_data)
            print("*" * 100)
        except Exception as e:
            print(e)
