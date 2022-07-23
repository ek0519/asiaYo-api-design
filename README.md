# Currency exchange API

## 1. Run docker

```shell
docker-compose up
```

## 2. Interactive API docs

Now go to [http://127.0.0.0:8001/docs](http://127.0.0.1:8001/docs)

You will see interactive API documentation (Swagger UI).

## 3. API docs

or got to [http://127.0.0.0:8001/redoc](http://127.0.0.1:8001/redoc)


## 4. Test

When step1 running

```shell
docker-compose exec fastapi pytest
```

## 1 minute quick know

### API path

**[GET]** `/api/exchange/:amount/:from_currency/:to_currency`

### Parameter

* **amount**
  * integer or float
  * greater than 0
* **from_currency**
  * currency
  * must be one of [USD, TWD, JPY] 
* **to_currency**
  * currency
  * must be one of [USD, TWD, JPY] 

### Success response

`status code 200`
```json
{
    "amount": "3.28"
}
```

### Fail response

* when amount was not number.
```json
{
    "detail": [
        {
            "loc": [
                "path",
                "amount"
            ],
            "msg": "value is not a valid float",
            "type": "type_error.float"
        }
    ]
}
```

* when amount less or equal to 0
```json
{
    "detail": [
        {
            "loc": [
                "path",
                "amount"
            ],
            "msg": "ensure this value is greater than 0",
            "type": "value_error.number.not_gt",
            "ctx": {
                "limit_value": 0
            }
        }
    ]
}
```
* when from currency no in range.
```json
{
    "detail": [
        {
            "loc": [
                "path",
                "from_currency"
            ],
            "msg": "value is not a valid enumeration member; permitted: 'TWD', 'JPY', 'USD'",
            "type": "type_error.enum",
            "ctx": {
                "enum_values": [
                    "TWD",
                    "JPY",
                    "USD"
                ]
            }
        }
    ]
}
```
* when to currency no in range.
```json
{
    "detail": [
        {
            "loc": [
                "path",
                "to_currency"
            ],
            "msg": "value is not a valid enumeration member; permitted: 'TWD', 'JPY', 'USD'",
            "type": "type_error.enum",
            "ctx": {
                "enum_values": [
                    "TWD",
                    "JPY",
                    "USD"
                ]
            }
        }
    ]
}
```