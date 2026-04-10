import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")

# Total revenue
q1 = "SELECT SUM(revenue) AS total_revenue FROM sales"

# Revenue by category
q2 = """
SELECT category, SUM(revenue) AS revenue
FROM sales
GROUP BY category
ORDER BY revenue DESC
"""

df1 = pd.read_sql(q1, conn)
df2 = pd.read_sql(q2, conn)

print("\n📊 Total Revenue:")
print(df1)

print("\n📊 Revenue by Category:")
print(df2)

conn.close()