# author Niko Kauz
# Version 1.2
# Generates sales data and writes it into a json document.
# This json document is located in ../Datasets/Sales/sales.json
# Simple approach: Date instead of DateTime and supermarkets are open at all days
# Updates:
# Updated start and end date as discussed in meeting
# Function returns a dataframe now with date and soldArticles
# Improved performance

import json
import pandas as pd
import random

# Function to call. Optional parameter @numberOfDataToGenerate --> Default value is 5000
# Returns dataframe with date and soldArticles list

def generateSalesData(hasToBeGenerated=False, numberOfDataToGenerate=5000):

    if hasToBeGenerated:
        # Read all articles as dataframe from articles.csv
        df = pd.read_csv("../Datasets/Articles/articles.csv")

        # List to contain the dictionaries. Will be the json to save in a file later.
        finalJSON = []

        # Generating dataframe with columns date and soldArticles
        columns = ['date', 'soldArticles']
        salesDataFrame = pd.DataFrame(columns=columns)

        # Generates a list of dateTime. Converts them then into dates.
        # Starts a 01. January 2020 and ends at 31. Oktober 2021
        dates = pd.date_range(start="2020-01-01", end="2021-10-31").date

        print("Generating data and adding it to the dataframe...")

        # Loop to create the first layer in json. date and soldArticles
        for sale in range(numberOfDataToGenerate):

            # Creates dictionary with random date and soldArticles list key, value pairs.
            firstLevelJSON = {
                "date": str(dates[random.randint(0, len(dates) - 1)]),
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
            # Fill in dataframe with json data dependent on json length
            salesDataFrame.loc[sale] = [firstLevelJSON['date'], firstLevelJSON["soldArticles"]]

        print("Data and dataframe generated. Saving data to a json file...")

        # Sort by date ascending.
        finalJSON.sort(key=lambda date: date["date"])
        salesDataFrame = salesDataFrame.sort_values("date").reset_index(drop=True)

        print(salesDataFrame)

        # Save data in json in json document.
        with open('../Datasets/Sales/sales.json', 'w') as outfile:
            json.dump(finalJSON, outfile, indent=4)
        print("Data saved in ../Datasets/Sales/sales.json.")
    else:
        salesDataFrame = pd.read_json("../Datasets/Sales/sales.json")

    return salesDataFrame