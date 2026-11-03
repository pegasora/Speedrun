# import os
# os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"
# tf.get_logger().setLEvel("Error")
# from tensorflow import keras
import keras
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# read in faults csvi
df = pd.read_csv("faults.csv")
faults = [
    "Pastry",
    "Z_Scratch",
    "K_Scatch",
    "Stains",
    "Dirtiness",
    "Bumps",
    "Other_Faults",
]

# features - everything but faults
features = df.drop(faults, axis=1)

# outcomes - just the faults
outcomes = df[faults]

print(features.columns)
print(outcomes.columns)
print(features.shape)
print(outcomes.shape)

# data preprocessing

# normalize
scaler = MinMaxScaler()

# normalize features and outcomes
features = scaler.fit_transform(features)
outcomes = scaler.fit_transform(outcomes)

# train test split 20% split
train_x, test_x, train_y, test_y = train_test_split(features, outcomes, test_size=0.2)

# build the model
# start - build the layers we want inside the model
# we are designating hyperparemeters - model structure
input_layer = keras.layers.Input(shape=(train_x.shape[-1],))

# layers 1 and 2 - dense layers
layer_1 = keras.layers.Dense(30, activation="relu")
layer_2 = keras.layers.Dense(15, activation="relu")

# output layer - same number of units as our output class
# going to use the softmax activation
output_layer = keras.layers.Dense(train_y.shape[-1], activation="softmax")

# make the model
model = keras.models.Sequential([input_layer, layer_1, layer_2, output_layer])

# print out a model summary - useful for debugging
print(model.summary())

# compile the model
# add optimizer, metrics, loss
optimizer = keras.optimizers.Adam(learning_rate=1e-3)
loss_function = keras.losses.CategoricalCrossentropy()
metric_list = [keras.metrics.CategoricalAccuracy()]
model.compile(optimizer=optimizer, loss=loss_function, metrics=metric_list)

# callbacks
callback_function = keras.callbacks.EarlyStopping(
    patience=2, monitor="val_loss", mode="min", restore_best_weights=True
)

callback_function_2 = keras.callbacks.ModelCheckpoint(
    "my_model/checkpoint_model.keras",
    monitor="val_loss",
    mode="min",
    save_best_only=True,
)

# train the model - biggest time sinc
epochs = 10
# better for slow computers
batch_size = 16
# batch_size = 32
history = model.fit(
    x=train_x,
    y=train_y,
    batch_size=batch_size,
    epochs=epochs,
    callbacks=[callback_function, callback_function_2],
    validation_split=0.1,
)
# print("Loss")
# print(history.history["loss"])
# print("Accuracy")
# print(history.history["categorical_accuracy"])

# return_dict = true
train_score = model.evaluate(x=train_x, y=train_y, verbose=0)
print("Training score: ", train_score)
test_score = model.evaluate(x=test_x, y=test_y, verbose=0)
print("Test score: ", test_score)

# run a prediction
predictions = model.predict(test_x)
print(predictions)
print(test_y)
pred_y = np.argmax(predictions, axis=1)
out_y = np.argmax(predictions, axis=1)

print(pred_y)
print(out_y)

matrix = confusion_matrix(out_y, pred_y)
class_accuracies = matrix.diagonal() / matrix.sum(axis=1)
print(faults)
print(class_accuracies)

report = classification_report(out_y, pred_y)
print(report)

loss_traces = ["loss", "val_loss"]
accuracy_traces = ["categorical_accuracy", "val_categorical_accuracy"]
for trace in accuracy_traces:
    plt.plot(history.history[trace])

plt.legend(accuracy_traces)
plt.show()
plt.clf()
