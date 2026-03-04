import pandas as pd 
from sklearn.preprocessing import LabelEncoder

# Read CSV
df = pd.read_csv("titanic.csv")

# Encode Sex and Embarked
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])
df["Embarked"] = le.fit_transform(df["Embarked"])

# Print the first 5 rows to check
print(df.head())