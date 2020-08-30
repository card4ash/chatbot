from random import (
    choice,
    randrange,
    sample,
)
from numpy import arange
from datetime import datetime, timedelta
import pytz

utc = pytz.UTC


def create_mock_profile():
    currency = "BDT"
    account_balance = 0

    credit_card_balance = {}
    transaction_history = {"spend": {}, "deposit": {}}

    credit_card_db = [
        "brac bank",
        "platinum",
        "signature",
        "gold",
    ]
    deposit_db = [
        "employer",
        "interest",
    ]
    recipient_db = [
        "md ismail",
        "tarun kumar",
        "nur alam",
        "maksudur rahman",
        "amit ranjan",
        "anup paul",
        "emrul kayes",
        "ashraful alam",
    ]
    vendor_db = [
        "daraz",
        "chaldal",
        "pikaboo",
        "swapno"
    ]

    start_date = utc.localize(datetime(2020, 1, 1))
    end_date = utc.localize(datetime.now())
    number_of_days = (end_date - start_date).days

    for vendor in vendor_db:
        rand_spend_amounts = sample(
            [round(amount, 2) for amount in list(arange(500, 5000, 1.5))],
            number_of_days // 2,
        )

        rand_dates = [
            (
                start_date + timedelta(days=randrange(number_of_days))
            ).isoformat()
            for x in range(0, len(rand_spend_amounts))
        ]

        transaction_history["spend"][vendor] = [
            {"amount": amount, "date": date}
            for amount, date in zip(rand_spend_amounts, rand_dates)
        ]
        account_balance -= sum(rand_spend_amounts)

    for deposit in deposit_db:
        if deposit == "interest":
            rand_deposit_amounts = sample(
                [round(amount, 2) for amount in list(arange(500, 2000, 1.50))],
                number_of_days // 30,
            )
        else:
            rand_deposit_amounts = sample(
                [
                    round(amount, 2)
                    for amount in list(arange(100000, 200000, 1.50))
                ],
                number_of_days // 14,
            )

        rand_dates = [
            (
                start_date + timedelta(days=randrange(number_of_days))
            ).isoformat()
            for x in range(0, len(rand_deposit_amounts))
        ]

        transaction_history["deposit"][deposit] = [
            {"amount": amount, "date": date}
            for amount, date in zip(rand_deposit_amounts, rand_dates)
        ]
        account_balance += sum(rand_deposit_amounts) - sum(rand_spend_amounts)

    for credit_card in credit_card_db:
        credit_card_balance[credit_card] = {
            "minimum balance": 2000,
            "current balance": choice(
                [round(amount, 2) for amount in list(arange(2000, 50000, 1.5))]
            ),
        }

    mock_profile = {
        "account_balance": f"{account_balance:.2f}",
        "currency": currency,
        "transaction_history": transaction_history,
        "credit_card_balance": credit_card_balance,
        "known_recipients": [recipient.title() for recipient in recipient_db],
        "vendor_list": vendor_db,
    }
    return mock_profile
