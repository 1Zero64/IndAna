# python3 ResultsVisualisation.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description: Plots the sales prediction results of the different machine learning models
# ===========================================================================================

from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import datetime as dt

from setuptools.msvc import winreg

import MachineLearning.LinearRegression.LinearRegression as lr
import MachineLearning.LinearRegression.PolynomialRegression as plr

def linearRegressionVisualisation(articleId):
    '''
    Plots the sales data and predictions of the linear regression machine learning model for a article in a 2d plot

    :param articleId: (int)
            identifier for a article
    '''
    sales, realSales, predictions, articleName = lr.linearRegression(articleId)

    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in sales['date']]

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int(len(dates) / 10)))

    plt.scatter(dates, realSales, s=10, label="Verkaufsmenge am Tag")
    plt.plot(dates, predictions, color='red', label='Vorhersage')
    plt.gcf().autofmt_xdate()
    plt.title("Verkaufsverlauf für das Produkt {}".format(articleName))
    plt.xlabel("Datum")
    plt.ylabel("Verkaufsmenge")
    plt.legend(loc="best")
    plt.show()


def linearRegression3dVisualisation(articleId):
    '''
    Plots the sales data and predictions of the linear regression machine learning model for a article in a 3d plot

    :param articleId: (int)
            identifier for a article
    '''
    sales, realSales, predictions, articleName = lr.linearRegression(articleId)

    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in sales['date']]

    ax = plt.axes(projection='3d')
    ax.set_xlabel('Date')
    ax.set_ylabel('Average Temperature')
    ax.set_zlabel('Sales')
    xAxis = range(len(sales['date']))

    # Data for a three-dimensional line
    ax.plot3D(xAxis, sales['tavg'], predictions, 'red')

    # Data for three-dimensional scattered points
    ax.scatter3D(xAxis, sales['tavg'], realSales, alpha=0.3, facecolors='none', edgecolors='blue')

    ax.xaxis.set_ticks(xAxis)
    ax.xaxis.set_ticklabels(dates)

    plt.title("Sales history for the article {}".format(articleName))

    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int(len(dates) / 5)))
    plt.show()


def polynomialRegressionVisualisation(articleId):
    '''
    Plots the sales data and predictions of the polynomial regression machine learning model for a article in a 2d plot

    :param articleId: (int)
            identifier for a article
    '''
    sales, realSales, predictions, articleName = plr.polynomialRegression(articleId)

    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in sales['date']]

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int(len(dates)/10)))

    plt.scatter(dates, realSales, s=10, label="Verkaufsmenge am Tag")
    plt.plot(dates, predictions, color='red', label='Vorhersage')
    plt.gcf().autofmt_xdate()
    plt.title("Verkaufsverlauf für das Produkt {}".format(articleName))
    plt.xlabel("Datum")
    plt.ylabel("Verkaufsmenge")
    plt.legend(loc="best")
    plt.show()


def polynomialRegression3dVisualisation(articleId):
    '''
    Plots the sales data and predictions of the polynomial regression machine learning model for a article in a 3d plot

    :param articleId: (int)
            identifier for a article
    '''
    sales, realSales, predictions, articleName = plr.polynomialRegression(articleId)

    dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in sales['date']]

    ax = plt.axes(projection='3d')
    ax.set_xlabel('Date')
    ax.set_ylabel('Average Temperature')
    ax.set_zlabel('Sales')
    xAxis = range(len(sales['date']))

    # Data for a three-dimensional line
    ax.plot3D(xAxis, sales['tavg'], predictions, 'red')

    # Data for three-dimensional scattered points
    ax.scatter3D(xAxis, sales['tavg'], realSales, alpha=0.3, facecolors='none', edgecolors='blue')

    ax.xaxis.set_ticks(xAxis)
    ax.xaxis.set_ticklabels(dates)
    plt.title("Sales history for the article {}".format(articleName))

    plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=int(len(dates) / 5)))
    plt.show()


def SARIMAXVisualisation(articleId):
    '''
    Plots the sales data and predictions of the SARIMAX machine learning model for a article in a 2d plot

    :param articleId: (int)
            identifier for a article
    '''
    pass


def RNNVisualisation(articleId):
    '''
    Plots the sales data and predictions of the RNN machine learning model for a article in a 2d plot

    :param articleId: (int)
            identifier for a article
    '''
    pass


if __name__ == '__main__':

    # Change for different articles
    wishedArticleId = 1

    linearRegression3dVisualisation(wishedArticleId)
    polynomialRegression3dVisualisation(wishedArticleId)

