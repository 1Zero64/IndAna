# python3 GeneratorSales.py
# -*- coding: utf-8 -*-
# ===========================================================================================
# Created by: Niko Kauz
# Description:
# # Generates sales data and writes it into a json document.
# # This json document is located in ../Datasets/Sales/sales.json
# ===========================================================================================

import json
import pandas as pd
import random
import time

import DataProcessing.DataGenerators.Configuration.Season as seas

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Print total progess in console
    :param
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

def generateSalesData(hasToBeGenerated=False, numberOfDataToGenerate=10000):
    '''
    Generates articles data, saves them to csv file and returns dataframe

    :param hasToBeGenerated: (bool)
            true: articles data gets freshly generated, default false: use generated .json
    :param numberOfDataToGenerate: (int)
            defines number of sales to generate, default: 10000
    :return: salesDataFrame: (pandas.dataframe)
                dataframe with date and soldArticles list
    '''

    if hasToBeGenerated:

        # Read all articles as dataframe from articles.csv
        df = pd.read_csv("../Datasets/Articles/articles.csv")

        # List to contain the dictionaries. Will be the json to save in a file later.
        finalJSON = []

        # Generating dataframe with columns date and soldArticles
        columns = ['date', 'soldArticles']
        salesDataFrame = pd.DataFrame(columns=columns)

        # Generates a list of dateTime. Converts them then into dates.
        # Starts a 01. January 2016 and ends at 31. Oktober 2021
        dates = pd.date_range(start="2016-01-01", end="2021-09-30").date

        print("Generating data and adding it to the dataframe...")

        # progress bar
        printProgressBar(0, numberOfDataToGenerate, prefix='Progress:', suffix='Complete', length=100)
        # Loop to create the first layer in json. date and soldArticles
        for sale in range(numberOfDataToGenerate):
            # Update Progress Bar
            time.sleep(0.1)
            printProgressBar(sale + 1, numberOfDataToGenerate, prefix='Progress:', suffix='Complete', length=50)

            # Creates dictionary with random date and soldArticles list key, value pairs.
            date = dates[random.randint(0, len(dates) - 1)]
            firstLevelJSON = {
                "date": str(date),
                "soldArticles": []
            }

            # Creates a random number of sold articles.
            numberOfSoldArticles = random.randint(1, df.shape[0])
            # List of used articles, so there are no duplicate articles in one sale.
            # Clears the list for every new first layer
            usedArticleIds = []

            # Create numberOfSoldArticles soldArticles elements for the soldArticles list.
            for number in range(numberOfSoldArticles):
                # Pick random articleID from dataframe.
                articleId = int(df.iloc[random.randint(0, df.shape[0] - 1)]["ID"])
                # Create a random quantity for that article.
                soldArticles = random.randint(5, 8)
                seasonWeight = seas.getSeason(date, articleId)
                soldArticles = int(soldArticles + soldArticles * seasonWeight)
                # Check if article ist already used.
                if articleId in usedArticleIds:
                    # If yes repeat the loop instance.
                    number -= 1
                    continue
                else:
                    # If not append articleId with quantity to soldArticles list in first Layer.
                    firstLevelJSON.get("soldArticles").append({
                        "articleId": articleId,
                        "quantity": soldArticles
                    })
                    # Append articleId to usedArticleIds list.
                    usedArticleIds.append(articleId)

            # Append generated first layer to finalJson list and continue with next loop instance.
            finalJSON.append(firstLevelJSON)
            # Fill in dataframe with json data dependent on json length
            salesDataFrame.loc[sale] = [firstLevelJSON['date'], firstLevelJSON["soldArticles"]]


        print("Data and dataframe generated. Saving data to a json file...")

        # Sort by date ascending.
        finalJSON.sort(key=lambda date: date["date"])
        salesDataFrame = salesDataFrame.sort_values("date").reset_index(drop=True)

        # Save data in json document.
        with open('../Datasets/Sales/sales.json', 'w') as outfile:
           json.dump(finalJSON, outfile, indent=4)
        print("Data saved in ../Datasets/Sales/sales.json.")
    else:
        salesDataFrame = pd.read_json("../Datasets/Sales/sales.json")

    return salesDataFrame

if __name__ == '__main__':
    generateSalesData(True, numberOfDataToGenerate=40000)