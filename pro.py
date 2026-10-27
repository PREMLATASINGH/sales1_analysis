import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
np.random.seed(42)

# Create dataset
n = 1000

data = {
    'order_id': np.arange(1, n+1),
    'order_date': pd.date_range(start='2023-01-01', periods=n, freq='D'),
    'region': np.random.choice(['East', 'West', 'North', 'South'], n),
    'product': np.random.choice(['Laptop', 'Mobile', 'Tablet', 'Headphones', 'Camera'], n),
    'category': np.random.choice(['Electronics', 'Accessories'], n),
    'quantity': np.random.randint(1, 10, n),
    'unit_price': np.random.randint(50, 1500, n),
    'discount': np.random.choice([0, 5, 10, 15, 20], n)
}

df = pd.DataFrame(data)

# Calculate total sales
df['total_sales'] = df['quantity'] * df['unit_price'] * (1 - df['discount']/100)

df.head()
print(df.head())
print(df.tail())
print(df.isnull().sum())
print(df.duplicated().sum())
df['order_date'] = pd.to_datetime(df['order_date'])
print(df['order_date'].head(10))
region_sales = df.groupby('region')['total_sales'].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region')
plt.ylabel('Sales Amount')
plt.xlabel('Region')
plt.show()
df['month'] = df['order_date'].dt.month

monthly_sales = df.groupby('month')['total_sales'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trend')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.grid(True)
plt.show()
product_sales = df.groupby('product')['total_sales'].sum().sort_values(ascending=False).head(5)

plt.figure(figsize=(8,5))
product_sales.plot(kind='bar', color='orange')
plt.title('Top 5 Products by Sales')
plt.ylabel('Sales Amount')
plt.show()

category_sales = df.groupby('category')['total_sales'].sum()

plt.figure(figsize=(6,4))
category_sales.plot(kind='pie', autopct='%1.1f%%', colors=['lightblue','lightgreen'])
plt.title('Sales by Category')
plt.ylabel('')
plt.show()
