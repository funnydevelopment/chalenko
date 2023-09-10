import logging
from typing import List, Union

import datetime


logger = logging.getLogger(__name__)


def check_date_valid(time: str) -> bool:
    """
    Функция проверяет дату на корректность значения и формат
    :param time: '2023-07-22 11:41:59.580000000'
    :return: True | False
    """
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        date_parts = time.split(".")
        date_without_microseconds = date_parts[0]
        microseconds = date_parts[1]
        date = datetime.datetime.strptime(date_without_microseconds, date_format)
        if date and microseconds.isdigit():
            return True
    except Exception as error:
        logger.error(f"Произошла ошибка: {error}")
        return False


def check_price_valid(price: str) -> bool:
    """
    Функция проверяет цену на корректность значения и формат
    :param price: '1873.3567938612'
    :return: True | False
    """
    integer_part, decimal_part = price.split(".")
    return integer_part.isdigit() and decimal_part.isdigit()


def check_data_valid(date_and_price: List[str]) -> Union[list, None]:
    """
    Функция, которая получает список, проверяет и возвращает корректные данные или None
    :param date_and_price: ['2023-07-23 05:11:47.948000000', '1873.3567938612']
    :return: ['2023-07-23 05:11:47.948000000', 1873.3567938612] | None
    """
    try:
        date, price = date_and_price[0], date_and_price[1]
        is_date_valid = check_date_valid(date)
        is_price_valid = check_price_valid(price)
        if is_date_valid and is_price_valid:
            return [date, float(price)]
    except ValueError as error:
        logger.error(f"Некорректные данные: {error}")
    except KeyError:
        pass
    return None
