"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime, date, timedelta


def print_days():
    dt_today = date(2021, 2, 24)
    print(dt_today)

    delta_1 = timedelta(days=1)
    dt_yesterday = dt_today - delta_1
    print(dt_yesterday)

    delta_30 = timedelta(days=30)
    dt_30_days_ago = dt_today - delta_30
    print(dt_30_days_ago)

def str_2_datetime(date_string):
    dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_string
    

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
