import csv
from typing import List, Union


def get_data() -> list:
    data = []
    with open("prices.csv", newline="", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            data.append(row)
    return data


def create_ohlc(date_and_price: List[Union[str, int, float]]) -> dict:
    """

    :param date_and_price:
    :return:
    """
    ohlc_dict = {
        "open_date": date_and_price[0],
        "close_date": date_and_price[0],
        "open": date_and_price[1],
        "high": date_and_price[1],
        "low": date_and_price[1],
        "close": date_and_price[1],
    }
    return ohlc_dict