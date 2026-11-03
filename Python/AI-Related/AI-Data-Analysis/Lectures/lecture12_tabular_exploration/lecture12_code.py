# code from in class 09/11/24 lecture 12

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# models
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier

# import dataset
df = pd.read_csv("fuel_end_use.csv")
print(df.head())
print(df["END_USE"].unique())
outcomes = [
    "Process Heating",
    "CHP and/or Cogeneration Process",
    "Conventional Boiler Use",
]
features = [
    "Coal",
    "Diesel",
    "Natural_gas",
    "Other",
    "Residual_fuel_oil",
    "Temp_degC",
    "Total",
]

# take a random sample of 30,000 rows
df = df.sample(n=30000)

# convert to numeric
for feature in features:
    df[feature] = pd.to_numeric(df[feature], errors="coerce")

# drop the bad values
df = df.dropna()

# take a look at the data by end-use
ph_df = df.loc[df["END_USE"] == outcomes[0]]
chp_df = df.loc[df["END_USE"] == outcomes[1]]
boil_df = df.loc[df["END_USE"] == outcomes[2]]


# Boxplots
def plot_var(variable):
    plt.boxplot([ph_df[variable], chp_df[variable], boil_df[variable]])
    plt.title(variable)
    plt.show()
    plt.clf()


# look at the distrubituomns of our inmputs to teh model
# vased on end use
# for variable in features:
#     plot_var(variable)


def prep_dataset(df, features, outcome):
    feature_df = df[features]
    outcome_df = df[outcome]

    # encode our labels
    encoder = LabelEncoder()
    outcome_df = encoder.fit_transform(outcome_df)
    print("Classes")
    print(encoder.classes_)

    # normalize data
    scaler = MinMaxScaler()
    feature_df = scaler.fit_transform(feature_df)

    # split into a training and test set
    train_in, test_in, train_out, test_out = train_test_split(
        feature_df, outcome_df, test_size=0.2
    )
    return train_in, test_in, train_out, test_out


train_in, test_in, train_out, test_out = prep_dataset(df, features, "END_USE")


def run_model(model, train_in, test_in, train_out, test_out):
    model.fit(train_in, train_out)
    test_accuracy_score = model.score(test_in, test_out)
    training_accuracy_score = model.score(train_in, train_out)

    # printing score
    print(f"Training accuracy: {training_accuracy_score}")
    print(f"Test accuracy: {test_accuracy_score}")
    print("Per Class Accuracy")
    test_predictions = model.predict(test_in)
    matrix = confusion_matrix(test_out, test_predictions)
    class_accuracies = matrix.diagonal() / matrix.sum(axis=1)
    print(class_accuracies)


model = DecisionTreeClassifier()
run_model(model, train_in, test_in, train_out, test_out)

