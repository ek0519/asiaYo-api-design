import random
import string

from fastapi.testclient import TestClient

from .main import app, currencies

client = TestClient(app)

test_currencies = list(currencies.keys())


def test_exchange():
    _from = random.choice(test_currencies)
    to = random.choice(test_currencies)
    amount = random.randrange(1, 10000, 1) + random.random()
    url = f"/api/exchange/{amount}/{_from}/{to}"
    response = client.get(url)
    assert response.status_code == 200


def test_wrong_from_currency():
    _from = random.choice(test_currencies) + random.choice(string.ascii_letters)
    to = random.choice(test_currencies)
    amount = random.randrange(1, 10000, 1) + random.random()
    url = f"/api/exchange/{amount}/{_from}/{to}"
    response = client.get(url)
    assert response.status_code == 422


def test_wrong_target_currency():
    _from = random.choice(test_currencies)
    to = random.choice(test_currencies) + random.choice(string.ascii_letters)
    amount = random.randrange(1, 10000, 1) + random.random()
    url = f"/api/exchange/{amount}/{_from}/{to}"
    response = client.get(url)
    assert response.status_code == 422


def test_wrong_amount():
    _from = random.choice(test_currencies)
    to = random.choice(test_currencies)
    amount = (random.randrange(1, 10000, 1) + random.random()) * (-1)
    url = f"/api/exchange/{amount}/{_from}/{to}"
    response = client.get(url)
    assert response.status_code == 422
