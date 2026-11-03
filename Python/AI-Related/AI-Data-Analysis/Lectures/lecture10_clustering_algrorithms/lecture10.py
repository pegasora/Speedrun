# clustering algorithms and normalization


# normalization

# feature 1

# a b c d

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN, KMeans
from sklearn.preprocessing import MinMaxScaler

# import csv file into df
df = pd.read_csv("abalone.csv")
df = df.iloc[0:100]
print("Features")
print(df.columns)
outcome = "Rings"
features = [
    "Length",
    "Diameter",
    "Height",
    "Whole weight",
    "Shucked weight",
    "Viscera weight",
    "Shell weight",
]
feature_df = df[features]

# look at the ages here
# plt.scatter(df.index, df["Rings"])
# plt.show()
# plt.clf()

# normalize the data
scaler = MinMaxScaler()
feature_df = scaler.fit_transform(feature_df)

n_clusters = 2
eps = 0.1
min_samples = 3
clustering = DBSCAN(eps=eps, min_samples=min_samples).fit(feature_df)
# clustering = KMeans(n_clusters=n_clusters).fit(feature_df)

plt.scatter(df.index, clustering.labels_)
plt.show()
plt.clf()
