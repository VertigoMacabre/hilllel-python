import json
import os
import unittest
from pathlib import Path

from dotenv import load_dotenv

from cash_register_system import BalanceService, Currency, BalanceMessage, ExchangeData
from entities import CurrencyConversion

dotenv_path = Path('.env.testing')
load_dotenv(dotenv_path=dotenv_path)


class ExchangeServiceTest(unittest.TestCase):
    initial_state = {"uah": 1000, "usd": 1000}
    preset_date = "2020-10-10"
    preset_rate = 27.50

    def _update_preset(self) -> None:
        with open(os.getenv("BALANCE_STATE"), "w") as file:
            balance_in_string = json.dumps(self.initial_state)
            file.write(balance_in_string)

        self.course = CurrencyConversion(Currency.USD.value, Currency.USD.value, self.preset_date, self.preset_rate)
        self.balance_service = BalanceService(self.course)

    def test_service_should_return_rates_of_currencies(self) -> None:
        self._update_preset()
        self.course = CurrencyConversion(Currency.USD.value, Currency.USD.value, self.preset_date, self.preset_rate)
        self.balance_service = BalanceService(self.course)
        self.assertTrue(self.balance_service.usd_rate, self.course.rate)
        self.assertTrue(self.balance_service.uah_rate, 1 / self.course.rate)

    def test_it_should_return_uah_balance_message(self) -> None:
        self._update_preset()
        preset_sting = f"RATE: {1 / self.preset_rate}, " \
                       f"AVAILABLE {self.initial_state['uah']}"

        balance_message = BalanceMessage(self.balance_service, Currency.UAH)
        self.assertEqual(preset_sting, str(balance_message))

    def test_it_should_return_usd_balance_message(self) -> None:
        self._update_preset()
        preset_sting = f"RATE: {self.preset_rate}, " \
                       f"AVAILABLE {self.initial_state['usd']}"

        balance_message = BalanceMessage(self.balance_service, Currency.USD)
        self.assertEqual(preset_sting, str(balance_message))

    def test_exchange_data_object_should_contain_needed_amount(self) -> None:
        self._update_preset()
        exchange_data: ExchangeData = self.balance_service.is_available_amount(Currency.USD, 5000)
        needed = self.balance_service.get_rate_of_currency(Currency.USD) * 5000
        self.assertEqual(exchange_data.needed_amount, needed)

    def test_exchange_data_object_should_contain_available_amount(self) -> None:
        self._update_preset()
        exchange_data: ExchangeData = self.balance_service.is_available_amount(Currency.USD, 5000)
        self.assertEqual(exchange_data.current_amount, self.initial_state[Currency.USD.value])


if __name__ == "__main__":
    unittest.main()
