import logging
from typing import List, Union

import pandas as pd
import mplfinance as mpf
import datetime

import schemas


logger = logging.getLogger(__name__)
# todo
# 1. вытащить все данные из файла
# 2. разбить данные по часам
# 3. в по разбитым часовым данным найти open, high, low, close
# 4. построить график
# 5. по графику построить EMA


def check_date_valid(time: str) -> str | None:
    """
    Функция проверяет дату на корректность значения и формат
    :param time: '2023-07-22 11:41:59.580000000'
    :return: '2023-07-22 11:41:59.580000000' | None
    """
    try:
        date_format = "%Y-%m-%d %H:%M:%S"
        date_parts = time.split(".")
        date_without_microseconds = date_parts[0]
        microseconds = date_parts[1]
        date = datetime.datetime.strptime(date_without_microseconds, date_format)
        if date and microseconds.isdigit():
            return f"{date}.{microseconds}"
    except Exception as error:
        return


def check_data_valid(
    date_and_price: List[str],
) -> Union[List[Union[str, int, float]], None]:
    """
    Функция, которая получает список, проверяет и возвращает корректные данные или None
    :param date_and_price: ['2023-07-23 05:11:47.948000000', '1873.3567938612']
    :return: ['2023-07-23 05:11:47.948000000', 1873.3567938612] | None
    """
    try:
        date, price = date_and_price[0], float(date_and_price[1])
        is_date_valid = check_date_valid(date)
        if is_date_valid and schemas.DatePrice(date=is_date_valid, price=price):
            return [is_date_valid, price]
    except ValueError as error:
        logger.error(f"Некорректные данные: {error}")
    return


def create_plot():
    """
    Функция для построения графика свечи
    :return:
    """
    pass


def create_plot_datas(data: list):
    """
    Функция для обработки данных из файла
    :param data: [['2023-07-02 21:25:59.556000000', '1921.5222860571'],
    ['2023-07-02 21:26:01.556999936', '1921.6082654061'],
    ['2023-07-02 21:26:01.558000128', '1922.1421207547']]
    :return:
    """
    pass


def test_data_plot():
    data = [
        ["2023-07-23 06:30:31.994999808", 1874.94, 1875.12, 1874.82, 1874.95],
        ["2023-07-23 06:33:37.996000000", 1874.95, 1875.08, 1874.90, 1875.00],
        ["2023-07-23 06:33:37.996999936", 1875.00, 1875.15, 1874.90, 1874.95],
        ["2023-07-23 06:35:11.997999872", 1874.95, 1875.10, 1874.90, 1874.98],
        ["2023-07-23 06:37:07.999000064", 1874.98, 1875.00, 1874.75, 1874.80],
    ]

    # Преобразование данных в DataFrame
    df = pd.DataFrame(data, columns=["Date", "Open", "High", "Low", "Close"])

    # Преобразование столбца 'Date' в формат datetime
    df["Date"] = pd.to_datetime(df["Date"])

    # Установка индекса на столбец 'Date'
    df.set_index("Date", inplace=True)

    # Построение графика свечей OHLC
    mpf.plot(df, type="candle", title="График свечей OHLC", ylabel="Цена", volume=False)
