import psycopg2
import pandas as pd
import os

password = "Ind4N@"

dbConnection = psycopg2.connect(
    host="192.168.178.52",
    database="IndAna",
    user="postgres",
    password=password,
    port="5432"
)

cursor = dbConnection.cursor()

truncateTableStatement = """
            TRUNCATE TABLE article, weather, stockArticle, sales 
            RESTART IDENTITY;
            """

cursor.execute(truncateTableStatement)

csvFileName = '../DataProcessing/Datasets/Articles/articles.csv'
sql = "COPY article FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csvFileName, "r"))

csvFileName = '../DataProcessing/Datasets/Weather/weather_012016-102021.csv'
sql = "COPY weather FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csvFileName, "r"))

csvFileName = '../DataProcessing/Datasets/Stockarticles/stockarticles.csv'
sql = "COPY stockarticle FROM STDIN DELIMITER ',' CSV HEADER"
cursor.copy_expert(sql, open(csvFileName, "r"))

# Prepare and load sales json
salesData = pd.read_json("../DataProcessing/Datasets/Sales/sales.json")
stagingDF = pd.DataFrame(columns=["ID", "date", "articleID", "quantity"])
counter = 1

for i in range(salesData.shape[0]):
    date = pd.Timestamp(salesData.iloc[i][0]).date()
    for j in range(len(salesData.iloc[i][1])):
        row = {'ID':counter, 'date':date, 'articleID':salesData.iloc[i][1][j]["articleId"], 'quantity':salesData.iloc[i][1][j]["quantity"]}
        stagingDF = stagingDF.append(row, ignore_index=True)
        counter += 1

print(stagingDF)

cursor.close()
dbConnection.commit()
dbConnection.close()
