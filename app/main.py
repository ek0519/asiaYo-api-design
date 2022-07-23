from enum import Enum

from fastapi import Path

from . import create_app

app = create_app()

currencies = {
    "TWD": {
        "TWD": 1,
        "JPY": 3.669,
        "USD": 0.03281
    },
    "JPY": {
        "TWD": 0.26956,
        "JPY": 1,
        "USD": 0.00885
    },
    "USD": {
        "TWD": 30.444,
        "JPY": 111.801,
        "USD": 1
    }
}


class CurrencyName(str, Enum):
    TWD = 'TWD'
    JPY = 'JPY'
    USD = 'USD'


@app.get("/api/exchange/{amount}/{from_currency}/{to_currency}")
def exchange(
        amount: float = Path(title="Amount of money", gt=0),
        from_currency: CurrencyName = Path(title="Your currency"),
        to_currency: CurrencyName = Path(title="Target currency"),
):
    _currency = currencies.get(from_currency.upper())
    currency_rate = _currency.get(to_currency.upper())

    return {
        "amount": f"{currency_rate * round(amount, 2):,.2f}"
    }
