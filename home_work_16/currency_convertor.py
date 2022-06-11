import sys

from dateutil import parser
from dotenv import load_dotenv

from api import Api
from entities import CurrencyConversion
from errors import CurrencyNotFound, BadHttpRequest
from extract_params import extract_args

load_dotenv()

if __name__ == "__main__":

    args = sys.argv[1::]

    want = extract_args(args, 0)
    date = extract_args(args, 1)

    api: Api = Api()

    if date:
        parsed_date = parser.parse(date)
        date = parsed_date.strftime("%Y%m%d")

    print(date)
    try:
        currency_conversion: CurrencyConversion = api.currency_converter(want, date)
        print(currency_conversion)
    except (CurrencyNotFound, BadHttpRequest) as e:
        print(e)
