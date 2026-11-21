import pandas as pd

df = pd.read_csv(r"C:\Users\acer\Videos\Live Weather & Air Quality Intelligence\Chennai_1990_2022_Madras.csv")

print("first 5 rows of the dataset:")
print(df.head())

print("dataset information:")
print(df.info())

print("dataset description:")
print(df.describe())

print("checking for missing values:")
print(df.isnull().sum())

print("checking for duplicate rows:")
print(df.duplicated().sum())    

print("dataset shape:")
print(df.shape)

print(df.columns)

# we are going clean the data set

# Remove exact duplicate rows
df = df.drop_duplicates()

# Convert collected_at into datetime
df["collected_at"] = pd.to_datetime(
    df["collected_at"], errors="coerce"
)

# Convert numeric-looking columns into numeric values
for col in df.columns:
    if col not in ["city", "collected_at", "time"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows without a collection timestamp
df = df.dropna(subset=["collected_at"])

# Fill missing numeric values with their column median
numeric_cols = df.select_dtypes(include="number").columns

for col in numeric_cols:
    if df[col].isnull().any():
        median_value = df[col].median()

        if pd.notna(median_value):
            df[col] = df[col].fillna(median_value)

# Save cleaned dataset
df.to_csv("data/cleaned_weather_air_quality.csv", index=False)

print("DATA CLEANING COMPLETED!")
print(df.head())
print("\nRemaining missing values:")
print(df.isnull().sum())
