# python3 GeneratorArticles.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Theresa Herr
# Created Date: Thu November 11 2021
# Version: 1.0
# Description: This file generates articles data and list them as a dataframe into a csv file
# ===========================================================================================

import pandas as pd

def generateArticlesData():

    columns = ['Article', 'Best By Period', 'Unit']

    articles = [
        ('Apple', 14, 'kg'),
        ('Milk', 7, 'l'),
        ('Toilet Paper', '', 'pcs')
    ]

    articlesDataFrame = pd.DataFrame(columns=columns, data = articles)

    # to start dataframe index at 1
    articlesDataFrame.index = articlesDataFrame.index + 1

    articlesDataFrame.to_csv('../Datasets/Articles/articles.csv', index_label='ID')
    
    # print(articlesDataFrame)
    
    return articlesDataFrame

#generateArticlesData()