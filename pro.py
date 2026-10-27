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