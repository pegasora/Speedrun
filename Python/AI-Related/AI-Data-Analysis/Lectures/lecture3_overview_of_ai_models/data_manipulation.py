"""
    example code from in class
"""

import pandas as pd

# read dataset into the "wine_df" variable
wine_df = pd.read_csv("winequality-white.csv", sep=";")

#get overview of data
print(wine_df.head())

#print the columns - method 1
print("col inx")
print(wine_df.columns)

#print col - method 2
print("col as list")
print(list(wine_df.columns))

#describe the data
print("describe data")
print(wine_df.describe())

#indxing
#return a series with the quality column of dataset 
quality_series = wine_df('quality')
print("quality score")
print(quality_series)

#return a list with the quality column of dataset 
quality_list = wine_df('quality').values.tolist()
print("quality score")
print(quality_list)

#using .loc
#get everything in quality
print("entire quality row")
print(wine_df.loc[:, "quality"])

#get the first quality value
print("first quality value")
print(wine_df.loc[0, "quality"])

#slice
print("first and up to 5-inx quality val")
print(wine_df.loc[0:5, "quality"])

print("everything before and up to 5 idx quality val")
print(wine_df.loc[:5, "quality"])

print("everything after the 4890th idx quality value")
print(wine_df.loc[4890:, ["quality", "sulphates"]])
