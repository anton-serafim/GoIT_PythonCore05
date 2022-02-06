from datetime import datetime, timedelta
import collections



users = {
     'Ann': datetime(year=1971, month=5, day=10),
     'Jonny': datetime(year=1990, month=5, day=14),
     'Carla': datetime(year=2010, month=5, day=11),
     'Luiza': datetime(year=1985, month=5, day=12),
     'Carlos': datetime(year=2001, month=5, day=15),
     'Bill': datetime(year=1976, month=5, day=13),
     'Liza': datetime(year=2001, month=5, day=9),
     'Kurt': datetime(year=2004, month=5, day=7),
     'Brandon': datetime(year=2015, month=5, day=5)
 }


def congratulate(users):

    current_datetime = datetime.now()
    change_current_date = current_datetime

    seven_days_delta = timedelta(days=7)
    time_start = None
    friday = 4
    users_birthdays = {}

    for user, date in users.items():
        # заменяем год на текущий
        date_with_current_year = date.replace(year=current_datetime.year)

        # день отсчета пятницу
        time_start = current_datetime + timedelta(days = friday - current_datetime.weekday())

        # заполняем словарь пользователей
        if time_start <= date_with_current_year <= time_start + seven_days_delta:
            users_birthdays[user] = date_with_current_year

    grouped_users = collections.defaultdict(list)
    for user, date in users_birthdays.items():
        if date.weekday() in (5, 6):
            grouped_users['Monday'].append(user)
        else:
            grouped_users[date.strftime('%A')].append(user)

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    sort_dict = collections.OrderedDict(sorted(grouped_users.items(), key=lambda x: days.index(x[0])))

    for day, name in sort_dict.items():
        print('{}: {}'.format(day, ', '.join(name)))

congratulate(users)
