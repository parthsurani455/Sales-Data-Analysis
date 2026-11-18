
import pandas as pd
import matplotlib.pyplot as plt

# Load sales dataset
df = pd.read_csv("sales_data.csv")

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Calculate total sales and profit
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order_ID"].nunique()

print("SALES DATA ANALYSIS")
print("-------------------")
print("Total Sales: Rs.", total_sales)
print("Total Profit: Rs.", total_profit)
print("Total Orders:", total_orders)

# Monthly sales
df["Month"] = df["Date"].dt.month_name()
monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Product-wise sales
product_sales = df.groupby("Product")["Sales"].sum()

print("\nProduct-wise Sales:")
print(product_sales)

# Region-wise sales
region_sales = df.groupby("Region")["Sales"].sum()

print("\nRegion-wise Sales:")
print(region_sales)

# Create sales chart
monthly_sales.plot(kind="bar", title="Monthly Sales Analysis")

plt.xlabel("Month")
plt.ylabel("Sales (Rs.)")
plt.tight_layout()
plt.show()
