# lecture 13 -- 09/13/24 in class code
# SVM 

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

df = pd.read_csv('dates.csv')
print(df.columns)

# plt.scatter(df['date_length'], df['date_diameter'])
# plt.show()
# plt.clf()

date_classes = ["Ajwa", "Medjool"]
df["class_code"] = 0
medjool_indexes = df.loc[df["class"] == "Medjool"].index.tolist()
df.loc[medjool_indexes, "class_code"] = 1
print(df["class_code"])

# creating model input and output
outcome_df = df["class_code"]
feature_df = df.drop(["class", "class_code", "color"], axis=1)

# normalize the model input 
scaler = MinMaxScaler()
feature_df = scaler.fit_transform(feature_df)

training_features, test_features, training_outcomes, test_outcomes, = train_test_split(feature_df, outcome_df, test_size=0.1)

svm = SVC()
svm.fit(training_features, training_outcomes)

# scoring
test_accuracy_score = svm.score(test_features, test_outcomes)
training_accuracy_score = svm.score(training_features, training_outcomes)

# print score
print(f"training accuracy: {training_accuracy_score}")
print(f"test accuracy: {test_accuracy_score}")

# 
print("Predicted features")
print(test_features)
predictions = svm.predict(test_features)
print("Predictions")
print(predictions)
decision_function = svm.decision_function(test_features)

#indicates what side they are on and how far away 
print(decision_function)

