import pandas as pd

# ----------------------------------
# 1️⃣ Load cleaned CSV file
# ----------------------------------
df = pd.read_csv("cleaned_sales_data.csv")

# ----------------------------------
# 2️⃣ Calculate Revenue column
# ----------------------------------
df["Revenue"] = df["Quantity"] * df["Price"]

print("Revenue column added successfully!")

# ----------------------------------
# 3️⃣ Total revenue
# ----------------------------------
total_revenue = df["Revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# ----------------------------------
# 4️⃣ Revenue per product
# ----------------------------------
product_revenue = df.groupby("Product")["Revenue"].sum()

print("\nRevenue by Product:")
print(product_revenue)

# ----------------------------------
# 5️⃣ Best product (highest revenue)
# ----------------------------------
best_product = product_revenue.idxmax()
best_product_revenue = product_revenue.max()

print("\nBest Product:", best_product)
print("Best Product Revenue:", best_product_revenue)

# ----------------------------------
# 6️⃣ Save updated file
# ----------------------------------
df.to_csv("sales_with_revenue.csv", index=False)

print("\n✅ File saved as sales_with_revenue.csv")
