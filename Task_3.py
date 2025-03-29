def magic_date(date_str):
    try:
        day, month, year = map(int, date_str.split('.'))
        return day * month == year % 100
    except ValueError:
        return False
date = input("Введите дату: ")
if magic_date(date):
    print("Магическая дата!")
else:
    print("обычная дата...")