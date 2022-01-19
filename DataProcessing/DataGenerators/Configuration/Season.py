from datetime import date, datetime
# articleSeasonality: specific 12 month interval season for each product
# (respectively each categorie in future versions)
# articleweight: allocation of article-specific impact of season-factor for each article

def getSeason(date, articleId, isSales=False):
    return ((articleSeasonality[articleId][date.month-1]-1) * articleWeight[articleId])
#   random Wert 50
#   50 + (50*(1 - AR.py.5 - SARIMA-1 - AR.py))*0.9 --> 50 + 50 * 0.5 - SARIMA * 0.9
#   x  + x*return
#   50 + 22,5 - SARIMA = 72,5 - SARIMA -> Rundung 72

articleSeasonality = {
        1:   [1.5, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4, 1.7, 2.0, 1.6, 1.9], # Apfel
        2:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], # Klopapier
        3:   [1.0, 1.0, 1.0, 1.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Milch
        4:   [1.0, 1.0, 1.0, 1.5, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Salmon
        5:   [1.0, 1.0, 1.0, 0.4, 0.8, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.6], # T-Bone steak
        6:   [1.7, 0.8, 0.3, 0.1, 0.0, 0.0, 0.1, 0.2, 0.6, 1.0, 1.8, 3.0], # Ginger Bread
        7:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.8, 0.7, 0.9, 1.1, 1.2, 1.4], # Berliner (Doughnut)
        8:   [1.0, 1.0, 1.0, 1.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Egg
        9:   [0.8, 0.9, 1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 1.7, 1.3, 1.0, 0.8], # Watermelon
        10:   [1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.2, 1.3, 1.4], # Soup vegetables
}

#impact of seasonality on outcome article volume (value between 0.0-1 - AR.py.0)
articleWeight = {
    1: 1.0,
    2: 0.0,
    3: 0.6,

    4: 0.4,
    5: 0.5,
    6: 1.5,
    7: 0.5,
    8: 0.7,
    9: 0.7,
    10: 0.8,
}

#tupel list article - saisonality
# list = [
#    ([1 - AR.py, 3 - ARMA.py], [1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py, 1 - AR.py])
#]
#    --> produkt 3 - ARMA.py (feuerwerkskörper) : "silvester"
#      [silvester][month(today)]
#     menge feuerwerkskörper x = x * [silvester][month(today)]



# approach
# getSeason(sellDate, article.category, articleId)
# ==> categorySeasonality + articleSeasonality + Grundform

# deprecated
#def getSeason(date):
#    if isinstance(date, datetime):
#        date = date.date()
#    date = date.replace(year=Y)
#    return next(season for season, (start, end) in seasons
#                if start <= date <= end)

