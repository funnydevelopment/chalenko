import csv
from typing import List, Union


def get_data() -> list:
    """
    Функция для получения всех записей из файла
    :return:[['2023-07-23 06:33:37.996000000', '1874.9483401491'], ...]
    """
    data = []
    with open("prices.csv", newline="", encoding="utf-8") as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            data.append(row)
    return data


def create_ohlc(date_and_price: List[Union[str, int, float]]) -> dict:
    """
    Функция для построение первичного списка для каждого периода
    :param date_and_price: ['2023-07-23 06:33:37.996000000', '1874.9483401491']
    :return: {
    'close': 1869.3016855943,
    'close_date': '2023-05-04 19:23:32.436000000',
    'high': 1876.7313482702,
    'low': 1869.0165488903,
    'open': 1875.979748793,
    'open_date': '2023-05-04 18:21:18.340000000'
  }
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
