import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv("train.csv")

#Initial Exploration
#print(df.head())
#print("Shape of dataset", df.shape)
#print("Columns", df.columns.tolist())
#print(df.isnull().sum())    

#Data Cleaning
df = df.drop(columns=['Cabin'])
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)

print(df.isnull().sum())

y = df['Survived']

X = df.drop(columns=['Survived', 'Name', 'Ticket', 'PassengerId'])

encoder = LabelEncoder()

X['Sex'] = encoder.fit_transform(X['Sex'])
X['Embarked'] = encoder.fit_transform(X['Embarked'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy: ", accuracy)

import pickle

with open("titanic_model.pkl", 'wb') as f:
    pickle.dump(model, f)