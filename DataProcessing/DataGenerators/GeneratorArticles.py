# python3 GeneratorArticles.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Theresa Herr
# Created Date: Thu November 11 2021
# Version: 1.0
# Description: This file generates articles data and list them as a dataframe into a csv file
# ===========================================================================================

import pandas as pd

def generateArticlesData(hasToBeGenerated=False):
    if hasToBeGenerated:
        columns = ['Article', 'Best By Period', 'Unit']

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