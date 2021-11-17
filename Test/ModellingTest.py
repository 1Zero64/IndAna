#Testing related snippets regarding ML Models

import statsmodels.api as m
import pandas
from patsy import dmatrices

dfarticles = sm.datasets.read_csv('Articles').data
#Rdataset
vars =  ['article', 'bestByPeriod', 'Unit']
df = df[vars]

#show footer
df[-5:]

#create 2 design matrices with dmatrices (endog + exog) from patsy module
y, X = dmatrices('matrice identifier', data=df, return_type='dataframe')


