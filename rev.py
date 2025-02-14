import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
# Replace 'your_data.csv' with your actual file path or use 'pd.read_excel' for Excel files
df=pd.read_excel('DataSet.xlsx')

# Data Cleaning
# Check for missing values
missing_data = df.isnull().sum()
print(f"Missing Values:\n{missing_data}")

# Handle missing values (impute or drop)
df = df.dropna()  # Or use df.fillna() for imputation

# Ensure correct data types
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce')
df['Shipping Cost'] = pd.to_numeric(df['Shipping Cost'], errors='coerce')

# Drop duplicates
df = df.drop_duplicates()

# Exploratory Data Analysis (EDA)
# Descriptive Statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Correlation Analysis (Correlation Matrix)
correlation_matrix = df[['Sales', 'Quantity', 'Profit', 'Shipping Cost']].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig('coorelation analysis.jpg')
# plt.show()

# Visualizations
# 1. Sales vs. Profit Scatter Plot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Sales', y='Profit', data=df, color='blue')
plt.title('Sales vs Profit')
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.savefig('Sales vs. Profit.jpg')
# plt.show()

# 2. Sales by Region
plt.figure(figsize=(10, 6))
sales_by_region = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=sales_by_region.index, y=sales_by_region.values, palette='viridis')
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.savefig('Sales by Region.jpg')
# plt.show()

# 3. Sales by Ship Mode
plt.figure(figsize=(8, 6))
sales_by_ship_mode = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=sales_by_ship_mode.index, y=sales_by_ship_mode.values, palette='Set2')
plt.title('Total Sales by Ship Mode')
plt.xlabel('Ship Mode')
plt.ylabel('Total Sales')
plt.savefig('Sales by ship mode.jpg')
# plt.show()

# 4. Profit by Category
plt.figure(figsize=(12, 6))
profit_by_category = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
sns.barplot(x=profit_by_category.index, y=profit_by_category.values, palette='coolwarm')
plt.title('Total Profit by Product Category')
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.savefig('Profit by Category.jpg')
# plt.show()

# Time-based Analysis (e.g., Sales over Time)
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month_name()

# Monthly Sales Trend
monthly_sales = df.groupby('Month')['Sales'].sum().reindex([
    'January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December'
])
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.savefig('Monthly Sales Trend.jpg')
# plt.show()

# Customer Segmentation: Top 10 High-Value Customers by Sales
top_customers = df.groupby('Customer Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10, 6))
top_customers.plot(kind='bar', color='orange')
plt.title('Top 10 High-Value Customers by Sales')
plt.xlabel('Customer Name')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.savefig('Top 10 High-Value Customers by Sales.jpg')
# plt.show()

# Profit Margin Analysis: Profit Margin by Product Category
df['Profit Margin'] = df['Profit'] / df['Sales']
profit_margin_by_category = df.groupby('Category')['Profit Margin'].mean().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
sns.barplot(x=profit_margin_by_category.index, y=profit_margin_by_category.values, palette='Blues')
plt.title('Average Profit Margin by Product Category')
plt.xlabel('Category')
plt.ylabel('Profit Margin')
plt.savefig('Profit Margin by Category.jpg')
# plt.show()

# Shipping Cost vs Profit
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Shipping Cost', y='Profit', data=df, color='purple')
plt.title('Shipping Cost vs Profit')
plt.xlabel('Shipping Cost')
plt.ylabel('Profit')
plt.savefig('Shipping Cost vs Profit.jpg')
# plt.show()

# Top 10 Most Profitable Products
top_profitable_products = df.groupby('Product Name')['Profit'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_profitable_products.plot(kind='bar', color='red')
plt.title('Top 10 Most Profitable Products')
plt.xlabel('Product Name')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)
plt.savefig('Top 10 Most Profitable Products.jpg')
# plt.show()

# Shipping Mode vs Profit (Boxplot)
plt.figure(figsize=(10, 6))
sns.boxplot(x='Ship Mode', y='Profit', data=df, palette='coolwarm')
plt.title('Shipping Mode vs Profit')
plt.xlabel('Ship Mode')
plt.ylabel('Profit')
plt.savefig('Shipping Mode vs Profit.jpg')
# plt.show()

# Customer Segmentation Analysis (Profit by Customer)
customer_profit = df.groupby('Customer Name')['Profit'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
customer_profit.plot(kind='bar', color='pink')
plt.title('Top 10 Customers by Profit')
plt.xlabel('Customer Name')
plt.ylabel('Profit')
plt.xticks(rotation=45)
plt.savefig('Customer Segmentation Analysis.jpg')
# plt.show()
