import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

# 1️⃣ Shape of data (rows, columns)
print("Shape of dataset:", df.shape)

# 2️⃣ Column names
print("\nColumns:")
print(df.columns)

# 3️⃣ Data types of each column
print("\nData Types:")
print(df.dtypes)

# Dataset info (most important)
print("\nDataset Info:")
df.info()