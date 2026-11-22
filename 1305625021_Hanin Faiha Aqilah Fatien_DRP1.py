#Menginput dan membaca data csv
import pandas as pd

df = pd.read_csv("PatientInfo.csv")
print(df.shape)
print(df.head())

#Data Cleaning
print("\nMissing values per kolom:\n", df.isna().sum())

for col in ["sex", "age", "country", "province", "city", "infection_case", "state"]:
    df[col] = df[col].astype("string").str.strip()

df = df.drop_duplicates()
print("\nRingkasan data:\n", df.describe(include="all"))