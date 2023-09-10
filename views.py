import logging
from typing import List, Union

import pandas as pd
import mplfinance as mpf
import datetime

import database


logger = logging.getLogger(__name__)
# todo
# 1. вытащить все данные из файла
# 2. разбить данные по часам
# 3. в по разбитым часовым данным найти open, high, low, close
# 4. построить график
# 5. по графику построить EMA


def check_date_valid(time: str) -> bool:
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
            return True
    except Exception as error:
        logger.error(f"Произошла ошибка: {error}")
        return False


def check_price_valid(price: str) -> bool:
    integer_part, decimal_part = price.split(".")
    return integer_part.isdigit() and decimal_part.isdigit()


def check_data_valid(date_and_price: List[str]) -> list | None:
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
    return


def create_ohlc(date_and_price: List[Union[str, int, float]]) -> dict:
    ohlc_dict = {
        "open_date": date_and_price[0],
        "close_date": date_and_price[0],
        "open": date_and_price[1],
        "high": date_and_price[1],
        "low": date_and_price[1],
        "close": date_and_price[1],
    }
    return ohlc_dict


def get_time_difference(last_date: str, current_date: str) -> bool:
    date_format = "%Y-%m-%d %H:%M:%S"
    last_date_1 = last_date.split(".")
    current_date_1 = current_date.split(".")
    last_date_datetime = datetime.datetime.strptime(last_date_1[0], date_format)
    current_date_datetime = datetime.datetime.strptime(current_date_1[0], date_format)
    if (current_date_datetime - last_date_datetime) < datetime.timedelta(hours=1):
        return True
    return False


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
    # data = database.get_data()
    plot_data = []
    for row in data:
        valid_data = check_data_valid(row)
        if valid_data:
            plot_data.append(create_ohlc(valid_data))
            break
    for row in data:
        needed_data = plot_data[-1]
        plot_row = {}
        valid_data = check_data_valid(row)
        if valid_data:
            last_close_date = needed_data["close_date"]
            current_close_date, current_price = valid_data[0], valid_data[1]
            less_1_hour = get_time_difference(last_close_date, current_close_date)
            if less_1_hour:
                plot_row["close_date"] = last_close_date
                current_high_price = needed_data.get("high")
                print(type(current_price))
                if current_price - current_high_price > 0:
                    plot_data[-1]["high"] = current_price
                if current_price < float(plot_data[-1]["low"]):
                    plot_data[-1]["low"] = current_price
            else:
                plot_data[-1]["close_date"] = [current_close_date]
        plot_data.append(plot_row)
    return plot_data


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
