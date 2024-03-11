import pandas as pd

# Load movie data from CSV file (replace 'movies.csv' with your file path)
movie_data = pd.read_csv('movies.csv')

# Create a DataFrame showing movies with a high rating (above 8) and a short runtime (under 90 minutes)
high_rated_short_movies = movie_data[
    (movie_data['rating'] > 8) & (movie_data['runtime_minutes'] < 90)]

# Group movies by genre and calculate the average runtime
average_runtime_by_genre = movie_data.groupby('genre')['runtime_minutes'].mean()

# Find the genre with the longest average runtime
longest_runtime_genre = average_runtime_by_genre.idxmax()

# Print results
print("High Rated Short Movies:")
print(high_rated_short_movies[['title', 'rating', 'runtime_minutes']])

print("\nAverage Runtime by Genre:")
print(average_runtime_by_genre.to_string())

print(f"\nGenre with the Longest Average Runtime: {longest_runtime_genre}")
