from datetime import date, datetime

Y = 2000
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

def getSeason(date):
    if isinstance(date, datetime):
        date = date.date()
    date = date.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= date <= end)
