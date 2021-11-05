# author Niko Kauz
# Version 1.0
# Generates sales data and writes it into a json document.
# This json document is located in ../Datasets/Sales/sales.json
# Simple approach: Date instead of DateTime and supermarkets are open at all days

import json
import pandas as pd
import random

# Function to call. Optional parameter @numberOfDataToGenerate --> Default value is 5000
# No return yet.
def generateSalesData(numberOfDataToGenerate=5000):
    # Read all articles as dataframe from articles.csv
    df = pd.read_csv("../Datasets/Articles/articles.csv")

    # List to contain the dictionaries. Will be the json to save in a file later.
    finalJSON = []

    # Generates a list of dateTime. Converts them then into dates.
    dateTimes = pd.date_range(start="2020-01-01", end="2021-11-01")
    onlyDate = dateTimes.date

    print("Starting to generate data...")

    # Loop to create the first layer in json. date and soldArticles
    for sale in range(numberOfDataToGenerate):
        # Selects a random date from date list
        selectedDate = onlyDate[random.randint(0, len(onlyDate) - 1)]

        # Creates dictionary with date and soldArticles list key, value pairs.
        firstLevelJSON = {
            "date": str(selectedDate),
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
            soldArticles = random.randint(1, 5)
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

    print("Data generated. Saving data to a json file...")

    # Sort by date ascending.
    finalJSON.sort(key=lambda date: date["date"])

    # Save data in json in json document.
    with open('../Datasets/Sales/sales.json', 'w') as outfile:
        json.dump(finalJSON, outfile, indent=4)

    print("Data saved in ../Datasets/Sales/sales.json.")
