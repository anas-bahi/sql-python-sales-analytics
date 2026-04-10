import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
from sklearn.linear_model import LinearRegression

# Connect to database
conn = sqlite3.connect("sales.db")

# Load data
df = pd.read_sql("SELECT * FROM sales", conn)

# -------------------------------
# 🧹 DATA CLEANING
# -------------------------------

# Convert date column
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Remove missing values (IMPORTANT FIX)
df = df.dropna()

# -------------------------------
# 📊 ANALYSIS 1: Revenue by Category
# -------------------------------

category_sales = df.groupby("category")["revenue"].sum()

category_sales.plot(kind="bar")

plt.title("Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Revenue")

plt.savefig("outputs/charts/category_sales.png")
plt.close()

# -------------------------------
# 📊 ANALYSIS 2: Monthly Trend
# -------------------------------

monthly = df.groupby(df['date'].dt.to_period("M"))['revenue'].sum()

monthly.plot()

plt.title("Monthly Revenue Trend")

plt.savefig("outputs/charts/monthly_trend.png")
plt.close()

# -------------------------------
# 🤖 MACHINE LEARNING
# -------------------------------

# Sort by date
df = df.sort_values("date")

# Create time index
df["day"] = range(len(df))

X = df[["day"]]
y = df["revenue"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict future
future_day = [[len(df) + 10]]
prediction = model.predict(future_day)

print("📈 Future Revenue Prediction:", prediction)

# Close connection
conn.close()

print("✅ Analysis complete! Charts saved in outputs/charts/")