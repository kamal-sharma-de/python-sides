import pandas as pd
import matplotlib.pyplot as plt

# Replace 'movies.csv' with your actual file path
movie_data = pd.read_csv('movies.csv')

# Count the number of movies in each genre
genre_counts = movie_data['genre'].value_counts()

# Create a bar chart
plt.figure(figsize=(8, 6))  # Adjust figure size as desired
plt.bar(genre_counts.index, genre_counts.values)
plt.xlabel("Movie Genre")
plt.ylabel("Number of Movies")
plt.title("Movie Genre Distribution")
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Display the chart
plt.show()
