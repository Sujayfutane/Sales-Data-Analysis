import pandas as pd

# ----------------------------------
# 1️⃣ Load CSV file
# ----------------------------------

df = pd.read_csv("sales_data.csv")

print("Original Data Shape:", df.shape)

# ----------------------------------
# 2️⃣ Check missing values
# ----------------------------------
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# ----------------------------------
# 3️⃣ Handle missing values
# ----------------------------------

# Fill numeric columns with mean
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

# Fill categorical columns with 'Unknown'
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = df[col].fillna("Unknown")

# ----------------------------------
# 4️⃣ Remove duplicate rows
# ----------------------------------
df = df.drop_duplicates()

# ----------------------------------
# 5️⃣ Reset index
# ----------------------------------
df.reset_index(drop=True, inplace=True)

# ----------------------------------
# 6️⃣ Final dataset info
# ----------------------------------
print("\nAfter Cleaning:")
print(df.info())

print("\nFinal Data Shape:", df.shape)

# ----------------------------------
# 7️⃣ Save cleaned data
# ----------------------------------
df.to_csv("cleaned_sales_data.csv", index=False)

print("\n✅ Cleaned file saved as cleaned_sales_data.csv")
