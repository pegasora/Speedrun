# %%
"""
    example code from in class
"""

# %%
import pandas as pd

# %%
# read dataset into the "wine_df" variable
wine_df = pd.read_csv("winequality-white.csv", sep=";")

# %%
#get overview of data
print(wine_df.head())

# %%
#print the columns - method 1
print("col inx")
print(wine_df.columns)

# %%
#print col - method 2
print("col as list")
print(list(wine_df.columns))

# %%
#describe the data
print("describe data")
print(wine_df.describe())

# %%
#indxing
#return a series with the quality column of dataset 
quality_series = wine_df['quality']
print("quality score")
print(quality_series)

#return a list with the quality column of dataset 
quality_list = wine_df['quality'].values.tolist()
print("quality score")
print(quality_list)

# %%
#using .loc
#get everything in quality
print("entire quality row")
print(wine_df.loc[:, "quality"])

#get the first quality value
print("first quality value")
print(wine_df.loc[0, "quality"])


# %%
#slice
print("first and up to 5-inx quality val")
print(wine_df.loc[0:5, "quality"])

print("everything before and up to 5 idx quality val")
print(wine_df.loc[:5, "quality"])

print("everything after the 4890th idx quality value")
print(wine_df.loc[4890:, ["quality", "sulphates"]])

# %%
#use iloc
print("Row indx 1-2 and col indx 1-4")
print(wine_df.iloc[1:3, 1:5])

print("4th row idx, first item")
print(wine_df.iloc[4, 0])

print("all rows, row idx 4")
print(wine_df.iloc[4, :])

# %%
#selecting a row or rows based on a condition 
print("all rows where wine quality is above a score of 5")
print(wine_df.loc[wine_df["quality"] > 5])

#how many rows is this 
print(len(wine_df.loc[wine_df["quality"] > 5].index))

# %%
print("all rows where quality is above 5 and sulphates are above 0.45")
sub_df = wine_df.loc[(wine_df["quality"] > 5) & (wine_df["sulphates"] < 0.45)]
print(sub_df.head())
print(len(sub_df.index))
#sub_df.reset_index()

# %%
#handling missing data
print(wine_df.isna())
print(wine_df.isna().value_counts())

# %%
#insert a NaN value
print(wine_df.loc[0, "quality"])
new_df = wine_df
new_df.loc[0, "quality"] = None
print(new_df.loc[0, 'quality'])

print("new df missing value counts")
print(new_df.isna().value_counts())

# %%
#drop the Nan 
print("number of rows before dropping NaN")
print(len(new_df.index))
cleaned_df = new_df.dropna()
cleaned_df.reset_index(inplace=True)

print("Number of rows after dropping NaN")
print(len(cleaned_df.index))
print(cleaned_df.loc[0, "quality"])

# %%
#%pip install matplotlib
#%pip install seaborn

# %%
#visualize 
#import matplotlib as plt
import matplotlib.pyplot as plt
import seaborn as sns

# %%
print(wine_df.corr())
plot = sns.heatmap(wine_df.corr())
#plt.show()
#plt.clf()

# %%
#scatter
plt.scatter(wine_df["residual sugar"], wine_df["density"])
#plt.show()
#plt.clf()
#clf() is clear figure function 
# you can use savfig if needed 

# %%



