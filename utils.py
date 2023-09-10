import datetime


def get_time_difference(last_date: str, current_date: str) -> bool:
    """

    :param last_date:
    :param current_date: True | False
    :return:
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

    :param date_time_1:
    :param date_time_2:
    :return:
    """
    date_format = "%Y-%m-%d %H:%M:%S"
    date_1, date_2 = date_time_1.split("."), date_time_2.split(".")
    date1 = datetime.datetime.strptime(date_1[0], date_format)
    date2 = datetime.datetime.strptime(date_2[0], date_format)
    sum_of_dates = date1 + (date2 - date1) / 2
    return str(sum_of_dates)


def get_date_with_microseconds(date: str) -> str:
    return date.split(".")[0]
