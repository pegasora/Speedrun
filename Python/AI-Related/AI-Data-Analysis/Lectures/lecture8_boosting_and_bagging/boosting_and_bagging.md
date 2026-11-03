# Boosting and Bagging Models 
Boosting and Bagging are two ways to increase the power of some of the model types we have been going over, especially for this tabular-type data. In this guide we'll explore what each of these techinques are and how to use them. 

## Bagging 
Bagging involves training smaller models on subsets of the dataset, and then averaging their answers together (or having some sort of answer voting scheme) to get a final answer. 

Bagging Models in Sci-kit learn follow the same API as the other models we have worked on. The base model they work on is the Decision Tree. In this way, boosting models are very similar to Random Forests. You can change API parameters like the number of models and how many training examples each receive to train on. 

## Boosting 
Boosting involves iteratively training the model to improve the performance. There are many different ways of doing this. Some models take the examples the first model performed poorly on and retrain the model to better classify them. 

For example, AdaBoost fits a classifier on the data and then fits additional classifiers on the data that the first model classified poorly in order to arrive at an improved final classification. 

Gradient Boosting uses the gradient of the loss function to improve the model's performance. We will be going over gradient calculations and how they are used in machine learning in more detail later in this course. 

## Summary 
For now, know that:

Bagging - uses subsets of the data to train multiple models. It puts together multiple 'weak' models to create a better one. 

Boosting - uses improvement methods over the originial model to add performance. This could be focusing on improving wrongly-classified examples or it could be using the gradient of the loss function, etc. 

## Code file. 
Let's explore a few of these. We are going to be using the same model API as before, with the faults dataset (available on canvas).

I am providing the code file here. I have three models, one bagging, two boosting. Try commenting them in and play around with what training and test accuracy metrics they give you. 

    import pandas as pd
    from sklearn.model_selection import train_test_split 
    from sklearn.ensemble import BaggingClassifier, AdaBoostClassifier, GradientBoostingClassifier
    #https://scikit-learn.org/stable/modules/tree.html 

    faults = ["Pastry", "Z_Scratch", "K_Scatch", "Stains", "Dirtiness", "Bumps", "Other_Faults"]

    def read_in_dataset(faults):
        df = pd.read_csv("faults.csv")
        df['fault'] = 0 
        #Lets create a categorical variable for each fault 
        #In the new "fault" column 
        for i in range(0, len(faults)):
            #index list
            true_fault_indexes = df.loc[df[faults[i]] == 1].index.tolist()
            df.loc[true_fault_indexes, "fault"] = i+1
            #Create our dataset 
        return df

    df = read_in_dataset(faults)
    #Create the training and test set 
    drop_features = ["fault"] + faults
    features = df.drop(drop_features, axis=1)
    outcomes = df["fault"]
    training_features, test_features, training_outcomes, test_outcomes = train_test_split(features, outcomes, test_size=0.1)



    #model = AdaBoostClassifier()
    #model = GradientBoostingClassifier()
    #model = BaggingClassifier()

    model.fit(training_features, training_outcomes)
    test_accuracy_score = model.score(test_features, test_outcomes)
    training_accuracy_score = model.score(training_features, training_outcomes)
    print(f"Training accuracy {training_accuracy_score}")
    print(f"Test accuracy {test_accuracy_score}")



