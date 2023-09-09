import pandas as pd
import mplfinance as mpf
import random
import datetime


def test_data_function():
    # Создаем произвольные данные для Candlestick Chart
    data = []
    date = datetime.datetime(2023, 1, 1)
    for _ in range(30):  # 30 дней
        open_price = random.uniform(100, 200)
        high_price = open_price + random.uniform(0, 10)
        low_price = open_price - random.uniform(0, 10)
        close_price = random.uniform(low_price, high_price)
        data.append([date, open_price, high_price, low_price, close_price])
        date += datetime.timedelta(days=1)

    # Создаем DataFrame из данных
    df = pd.DataFrame(data, columns=['Date', 'Open', 'High', 'Low', 'Close'])
    df.set_index('Date', inplace=True)

    # Вычисляем EMA без TA-Lib
    ema_period = 9
    df['EMA'] = df['Close'].ewm(span=ema_period, adjust=False).mean()

    # Создаем Candlestick Chart с EMA с помощью mplfinance
    mpf.plot(df, type='candle', title='Candlestick Chart с EMA (без TA-Lib)',
             ylabel='Цена', volume=False, addplot=[mpf.make_addplot(df['EMA'])])


def get_data_plot():
    data = [
        ['2023-07-23 06:30:31.994999808', '1874.9483401491'],
        ['2023-07-23 06:33:37.996000000', '1874.9483401491'],
        ['2023-07-23 06:33:37.996999936', '1874.9460261248'],
        ['2023-07-23 06:35:11.997999872', '1874.9460261248'],
        ['2023-07-23 06:37:07.999000064', '1874.8287210745']
    ]

    # Преобразование данных в DataFrame
    df = pd.DataFrame(data, columns=['Date', 'Close'])

    # Преобразование столбца 'Date' в формат datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Установка индекса на столбец 'Date'
    df.set_index('Date', inplace=True)

    # Преобразование столбца 'Close' в числовой тип данных (float)
    df['Close'] = df['Close'].astype(float)

    # Создание фиктивных столбцов "Open", "High" и "Low"
    df['Open'] = df['Close']
    df['High'] = df['Close']
    df['Low'] = df['Close']

    # Вычисление EMA
    ema_period = 5  # Пример: период EMA
    df['EMA'] = df['Close'].ewm(span=ema_period, adjust=False).mean()

    # Построение графика Candlestick Chart с EMA
    mpf.plot(df, type='candle', title='Candlestick Chart с EMA (без TA-Lib)',
             ylabel='Цена', volume=False, addplot=[mpf.make_addplot(df['EMA'])])
