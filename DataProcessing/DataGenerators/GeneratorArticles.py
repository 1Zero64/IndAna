import pandas as pd
import numpy 
import random

def generateArticlesData():

    articles = {
        # Article: [BestByPeriod, Unit]
        'Apple': [14, 'kg'],
        'Milk': [7, 'l'],
        'Toilet Paper': ['', 'pcs']
    }

    columns = ['ID', 'Article', 'BestByPeriod', 'Unit']

    df = pd.DataFrame(columns=columns)

    for i in range(3):
        article = random.choice(list(articles.keys()))
        bestByPeriod = articles[article][0]
        unit = articles[article][1]

        df.loc[i] = [i, article, bestByPeriod, unit]

        df.to_csv('articles_dummyData.csv')

return df