# python3 GeneratorArticles.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Theresa Herr
# Created Date: Thu November 11 2021
# Version: 1.0
# Description: Generates articles data, saves them to csv file and returns dataframe
# ===========================================================================================

import pandas as pd

def generateArticlesData(hasToBeGenerated=False):
    '''
    Generates articles data, saves them to csv file and returns dataframe

    :param hasToBeGenerated: (bool)
            true: articles data gets freshly generated, default false: use generated .csv
    :return:
        articlesDataFrame: (pandas.dataframe)
            dataframe with articles
    '''
    if hasToBeGenerated:
        columns = ['Article', 'Best By Period', 'Unit']

        # articles not generated but given manually
        articles = [
            ('Apple', 14, 'kg'),
            ('Milk', 7, 'l'),
            ('Toilet Paper', '', 'pcs'),
            ('Salmon', 3, 'kg'),
            ('T-Bone Steak', 6, 'kg'),
            ('Ginger Bread', 21, 'pcs'),
            ('Berliner (Doughnut)', 3, 'pcs'),
            ('Egg', 28, 'pcs'),
            ('Watermelon', 21, 'kg' ),
            ('Soup vegetables', 7, 'kg')
        ]

        articlesDataFrame = pd.DataFrame(columns=columns, data=articles)

        # to start dataframe index at 1
        articlesDataFrame.index = articlesDataFrame.index + 1

        articlesDataFrame.to_csv('../Datasets/Articles/articles.csv', index_label='ID')
    else:
        articlesDataFrame = pd.read_csv('../Datasets/Articles/articles.csv', index_col=False)
    
    return articlesDataFrame