import datetime
'''Реализуйте программу, чтобы получить номер недели.
Date: 2015, 6, 16
Output: 25'''
def get_week_number(year, month, day):
    date_obj = datetime.date(year, month, day)
    week_number = date_obj.isocalendar()[1]
    return week_number

result = get_week_number(2015, 6, 16)
print(result)

'''Реализуйте программу, чтобы найти дату первого понедельника данной недели.
Date: 2015, 50
Output: пн 14 декабря 00:00:00 2015'''
def get_first_monday_of_week(year, week_number):
    first_day_of_week = datetime.datetime.strptime(f'{year}-{week_number}-1', "%Y-%W-%w")
    return first_day_of_week

result = get_first_monday_of_week(2015, 50)
print(result)


'''Реализуйте программу, чтобы выбрать все воскресенья определенного года'''
def get_sundays_of_year(year):
    sundays = []
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                date_obj = datetime.date(year, month, day)
                if date_obj.weekday() == 6:
                    sundays.append(date_obj)
            except ValueError:
                pass
    return sundays

result = get_sundays_of_year(2015)
print(result)


'''Реализуйте программу на Python, чтобы добавить год (ы) с заданной датой и отобразить
новую дату.
Example: (addYears - это имя пользовательской функции)
print (addYears (datetime.date (2015,1,1), -1))
print (addYears (datetime.date (2015,1,1), 0))
print (addYears (datetime.date (2015,1,1), 2))
печати (addYears (datetime.date (2000,2,29), 1))
Output:
2014-01-01
2015-01-01
2017-01-01
2001-03-01'''

def add_years(current_date, num_years):
    try:
        new_date = current_date.replace(year=current_date.year + num_years)
        if leap_year(new_date.year):
            if current_date.month == 2 and current_date.day == 29 and new_date.day != 29:
                new_date = new_date.replace(day=28)
        return new_date
    except ValueError:
        return current_date

def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

date1 = datetime.date(2015, 1, 1)
date2 = datetime.date(2000, 2, 29)
print(add_years(date1, -1))
print(add_years(date1, 0))
print(add_years(date1, 2))
print(add_years(date2, 1))
