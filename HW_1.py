from datetime import datetime


def get_days_from_today(date):
    now = datetime.now().date()
    given_date = datetime.strptime(date, "%Y-%m-%d").date()
    return (now - given_date).days


date = input('Введіть дату у форматі "РРРР-ММ-ДД":\n')

try:
    print(f'Кількість днів між заданою датою і поточною датою: {get_days_from_today(date)}')
except ValueError:
    print('Невірний формат дати. Введіть у форматі: РРРР-ММ-ДД')
