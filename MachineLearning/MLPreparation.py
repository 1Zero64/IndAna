# python3 LinearRegression.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Filters (if necessary), prepares and splits merged data into train and test data for the machine learning models
# ===========================================================================================

from sklearn.model_selection import train_test_split
import pandas as pd

import DataProcessing.DataPreparation as dp

def prepareForML(seed=42):
    '''
        Filters, prepares and splits merged data into train and test data for the machine learning models

        :param seed: (int)
                seed for randomization of the data
        :return:
            sales: (pandas.dataframe)
                dataframe with dates and summed up sold quantities for all articles
            X_train: (pandas.dataframe)
                trainings data for the features
            X_test: (pandas.dataframe)
                test data for the features
            y_train: (pandas.dataframe)
                training data for the labels
            y_test: (pandas.dataframe)
                test data for the labels
    '''

    def filterSales(sales):
        '''
            Filters the data frame. Not necessary yet

            :param sales: (pandas.dataframe)
                sales data frame
            :return:
                filteredSales: (pandas.dataframe)
                    filtered sales data frame
        '''
        filteredSales = sales
        return filteredSales

    # read merged data frame from csv
    sales = pd.read_csv("../Datasets/merged1.csv")

    # Fill NaN with 0
    sales = sales.fillna(0)

    sales = filterSales(sales)

    # get features (X = date and tavg) and Labels (y = alle article sales data)
    X = sales[['date', 'tavg']]
    y = sales.iloc[:, 4:]

    # split into test and train data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

    # return test and train data, as well as the whole data frame
    return sales, X_train, X_test, y_train, y_test


def prepareArticlesData():
    '''
         Filters the data frame. Not necessary yet

        :return:
            articles: (pandas.dataframe)
            data frame for the articles
    '''
    articles = dp.prepareArticlesData()
    return articles


if __name__ == '__main__':
    # Test
    prepareForML()