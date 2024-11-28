import pandas as pd
import matplotlib.pyplot as plt

netflix_df = pd.read_csv("")
#Filtering Data to be movies only
movies = netflix_df[(netflix_df["type"] == "Movie")]
movies_1990 = movies[(movies["release_year"] == 1990)]

#Filtering movies to be from 1990 till 2000 only
decade_movies = movies[(movies["release_year"] >=1990) & (movies["release_year"] <= 2000)]

#Plotting a histogram to view most common duration in the decade
decade_movies["duration"].hist(alpha=0.5)
plt.title("Duration of Movies from 1990 till 2000")
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')
plt.show()

action_movies_1990 = movies_1990[(movies_1990["genere"] == "action")]
condition = action_movies_1990["duration"] < 90
short_movies_counter_sum = condition.sum()
print(f"Number of short action movies: {short_movies_counter_sum}")

