import pandas as pd
import mplfinance as mpf

import validation
import database
import utils


def calculate_ema(df, ema_period) -> None:
    """

    :param df:
    :param ema_period:
    :return:
    """
    # Рассчитываем EMA (период ema_period) и добавляем его в DataFrame
    df["EMA"] = df["Close"].ewm(span=ema_period, adjust=False).mean()


def create_plot_datas(data: list) -> list[dict]:
    """
    Функция для обработки данных из файла
    :param data: [['2023-07-02 21:25:59.556000000', '1921.5222860571'],
    ['2023-07-02 21:26:01.556999936', '1921.6082654061'],
    ['2023-07-02 21:26:01.558000128', '1922.1421207547']]
    :return:
    """

    plot_data = list()
    for i in range(len(data) - 1):
        valid_data = validation.check_data_valid(data[i])
        if valid_data:
            data.pop(i)
            plot_data.append(database.create_ohlc(valid_data))
            break
    for row in data:
        needed_data = plot_data[-1]
        valid_data = validation.check_data_valid(row)
        if valid_data:
            last_close_date = needed_data["close_date"]
            current_close_date, current_price = valid_data[0], valid_data[1]
            less_1_hour = utils.get_time_difference(last_close_date, current_close_date)
            if less_1_hour:
                # plot_data[-1]["close_date"] = last_close_date
                if current_price > plot_data[-1]["high"]:
                    plot_data[-1]["high"] = current_price
                if current_price < plot_data[-1]["low"]:
                    plot_data[-1]["low"] = current_price
            else:
                plot_data[-1]["close_date"] = current_close_date
                plot_data[-1]["close"] = current_price
                plot_row = {}
                plot_row["open_date"] = current_close_date
                plot_row["close_date"] = current_close_date
                plot_row["open"] = current_price
                plot_row["high"] = current_price
                plot_row["low"] = current_price
                plot_row["close"] = current_price
                plot_data.append(plot_row)
    return plot_data


def create_plot_from_datas(data: list[dict]) -> None:
    """

    :param data:
    :return:
    """
    plot_data = []
    for row in data:
        plot_row = []
        date = utils.get_sum_of_date(row["close_date"], row["open_date"])
        plot_row.append(utils.get_date_with_microseconds(date))
        plot_row.append(row["open"])
        plot_row.append(row["high"])
        plot_row.append(row["low"])
        plot_row.append(row["close"])
        plot_data.append(plot_row)

    df = pd.DataFrame(plot_data, columns=["Date", "Open", "High", "Low", "Close"])

    df["Date"] = pd.to_datetime(df["Date"])

    df.set_index("Date", inplace=True)

    ema_period = 1736
    calculate_ema(df, ema_period)

    mpf.plot(
        df,
        type="candle",
        title="График свечей OHLC с EMA",
        ylabel="Цена",
        volume=False,
        addplot=[mpf.make_addplot(df["EMA"], color="blue")],
    )
