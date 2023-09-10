import datetime


def get_time_difference(last_date: str, current_date: str) -> bool:
    """
    Функция проверяет разницу времени, прошел ли один час
    :param last_date: '2023-05-04 19:23:32.436000000'
    :param current_date: '2023-05-04 20:29:08.467000064'
    :return: True | False
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    last_date_1, current_date_1 = last_date.split("."), current_date.split(".")
    last_date_datetime = datetime.datetime.strptime(last_date_1[0], date_format)
    current_date_datetime = datetime.datetime.strptime(current_date_1[0], date_format)
    if (current_date_datetime - last_date_datetime) < datetime.timedelta(hours=1):
        return True
    return False


def get_sum_of_date(date_time_1: str, date_time_2: str) -> str:
    """
    Функция считает среднее время для заданного участка
    :param date_time_1: '2023-05-04 19:23:32.436000000'
    :param date_time_2: '2023-05-04 20:29:08.467000064'
    :return: '2023-05-04 19:56:20'
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    date_1, date_2 = date_time_1.split("."), date_time_2.split(".")
    date1 = datetime.datetime.strptime(date_1[0], date_format)
    date2 = datetime.datetime.strptime(date_2[0], date_format)
    sum_of_dates = date1 + (date2 - date1) / 2
    return str(sum_of_dates)


def get_date_without_nanoseconds(date: str) -> str:
    """
    Функция время без наносекунд для построения графика
    :param date: '2023-05-04 19:23:32.436000000'
    :return: '2023-05-04 19:23:32'
    """
    return date.split(".")[0]
