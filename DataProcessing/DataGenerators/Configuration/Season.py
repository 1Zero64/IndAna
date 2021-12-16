from datetime import date, datetime
# articleSeasonality: specific 12 month interval season for each product
# (respectively each categorie in future versions)
# articleweight: allocation of article-specific impact of season-factor for each article

def getSeason(date, articleId, isSales=False):
    return ((articleSeasonality[articleId][date.month-1]-1) * articleWeight[articleId])
#   random Wert 50
#   50 + (50*(1.5-1))*0.9 --> 50 + 50 * 0.5 * 0.9
#   x  + x*return
#   50 + 22,5 = 72,5 -> Rundung 72

articleSeasonality = {
        1:   [1.3, 1.1, 1.0, 1.0, 1.0, 1.0, 1.0, 1.2, 1.5, 1.8, 1.5, 1.6], # Apfel
        2:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], # Klopapier
        3:   [1.0, 1.0, 1.0, 1.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Milch
}

#impact of seasonality on outcome article volume (value between 0.0-1.0)
articleWeight = {
    1: 1.0,
    2: 0.0,
    3: 0.6,
}

#tupel list article - saisonality
# list = [
#    ([1, 3], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
#]
#    --> produkt 3 (feuerwerkskörper) : "silvester"
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

