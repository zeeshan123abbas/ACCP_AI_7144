# lab1_prepare_data.py - Lab 1: get the churn data ready for machine learning
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("customer_churn.csv")

# Task 1: explore the label - are the classes balanced?
print(df["churn"].value_counts(normalize=True).round(2))

# Task 2: models need numbers, so turn text columns into 0/1 columns (one-hot encoding)
X = pd.get_dummies(df.drop(columns="churn"), columns=["city", "package"], drop_first=True)
y = (df["churn"] == "Yes").astype(int)          # 1 = customer left, 0 = stayed
print("\nFeature columns:", list(X.columns))

# Task 3: split with stratify so both sets keep the same churn rate
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=7, stratify=y)
print("\nTrain:", X_train.shape, "Test:", X_test.shape)
print("Churn rate train/test:", round(y_train.mean(), 2), round(y_test.mean(), 2))

# Task 4: save the prepared sets for the next labs
X_train.assign(churn=y_train).to_csv("train.csv", index=False)
X_test.assign(churn=y_test).to_csv("test.csv", index=False)
print("Saved train.csv and test.csv")
