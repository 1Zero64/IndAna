# python3 Season.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Kevin Hilzinger & Niko Kauz
# Description:
# Returns a season weight of a article (calculated by articleSeasonality and articleWeight)
# articleSeasonality: specific 12 month interval season for each product
# articleWeight: allocation of article-specific impact of season-factor for each article
# ===========================================================================================

def getSeason(date, articleId):
    '''
    calculates and returns the season weight for a article

    :param date: (date)
            date to get the article seasonality
            articleId: (int)
            identifier of the article to get the article seasonality and article weight
    :return:
        articleSeasonWeight: (float)
            season weight for a article
    '''
    articleSeasonWeight = ((articleSeasonality[articleId][date.month-1]-1) * articleWeight[articleId])
    return articleSeasonWeight


# Seasonality weight for a product for each month
articleSeasonality = {
        1:   [1.5, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4, 1.7, 2.0, 1.6, 1.9], # Apfel
        2:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0], # Milch
        3:   [1.0, 1.0, 1.0, 1.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Klopapier
        4:   [1.0, 1.0, 1.0, 1.5, 1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Salmon
        5:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.6], # T-Bone steak
        6:   [1.7, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.8, 3.0], # Ginger Bread
        7:   [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.2, 1.4], # Berliner (Doughnut)
        8:   [1.0, 1.0, 1.0, 1.4, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.4], # Egg
        9:   [1.0, 1.0, 1.0, 1.1, 1.3, 1.5, 1.7, 1.9, 1.7, 1.3, 1.0, 1.0], # Watermelon
        10:   [1.2, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.1, 1.2, 1.3, 1.4], # Soup vegetables
}

# impact of seasonality on outcome article volume (value between 0.0 and 2.0)
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
