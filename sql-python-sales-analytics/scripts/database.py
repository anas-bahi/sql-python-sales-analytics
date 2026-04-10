import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("sales.db")

# Load dataset
df = pd.read_csv("data/superstore.csv", encoding="latin1")

# Rename columns to match project
df = df.rename(columns={
    "Order Date": "date",
    "Product Name": "product",
    "Category": "category",
    "Sales": "revenue",
    "Quantity": "quantity",
    "Region": "region"
})

# Create price column
df["price"] = df["revenue"] / df["quantity"]

# Keep only needed columns
df = df[["date", "product", "category", "price", "quantity", "revenue", "region"]]

# Save to SQL
df.to_sql("sales", conn, if_exists="replace", index=False)

print("✅ Database created successfully!")

conn.commit()
conn.close()