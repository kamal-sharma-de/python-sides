import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans  # Optional, for clustering

# Sample data (replace with your actual dataset)
data = {
    'customer_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'product_category': ['Electronics', 'Electronics', 'Clothing', 'Home', 'Electronics', 'Sports', 'Home', 'Food', 'Clothing', 'Food'],
    'purchase_amount': [1000, 500, 200, 1500, 800, 300, 1200, 400, 600, 700]
}

# Create pandas DataFrame
df = pd.DataFrame(data)

# Data cleaning and pre-processing (adjust as needed)
# Handle missing values (e.g., df.fillna(0))
# Encode categorical data (e.g., one-hot encoding using pd.get_dummies())

# Feature engineering (create new features if necessary)
# Example: Combine purchase_amount and product_category
df['category_spend'] = df['purchase_amount'] * df['product_category'].map({'Electronics': 2, 'Clothing': 1, 'Home': 1.5, 'Sports': 1, 'Food': 0.5})

# Exploratory data analysis
print(df.describe())  # Summary statistics

# Group by product category and calculate average purchase amount
avg_purchase_category = df.groupby('product_category')['purchase_amount'].mean()
print(avg_purchase_category)

# Visualization (example: bar chart)
plt.bar(avg_purchase_category.index, avg_purchase_category.values)
plt.xlabel('Product Category')
plt.ylabel('Average Purchase Amount')
plt.title('Average Purchase Amount by Product Category')
plt.show()

# Customer segmentation (optional, using KMeans clustering)
# Assuming 'category_spend' is a good representative feature
X = df[['category_spend']].to_numpy()
kmeans = KMeans(n_clusters=3, random_state=42)  # Choose appropriate number of clusters
kmeans.fit(X)

# Assign cluster labels to each customer
df['cluster'] = kmeans.labels_

# Analyze customer segments based on cluster membership and product category
print(df.groupby('cluster')['product_category'].value_counts())

# Recommendation based on cluster and product category spending patterns (example)
cluster_1_fav = df[df['cluster'] == 0]['product_category'].mode().iloc[0]
print(f"Recommendation for cluster 1: Promote {cluster_1_fav} products more.")

# Customize further based on your specific requirements and data
