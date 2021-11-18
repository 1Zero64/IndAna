import pandas as pd

def generateWeatherData():
    #columnnames:   date, tavg (average temperature), tmin (min. temp.), tmax (max. temp.), 
    #               prcp (overall precipitation/Gesamtniederschlag), snow, wdir (wind direction),
    #               wspd (wind speed), wpgt (wind peak/Spitzenboe), pres (pressure/Luftdruck), 
    #               tsun (time of sunshine)
    path = '../Datasets/Weather/weather_012019-102021.csv'
    data = pd.read_csv(path, header=[0])
    return data