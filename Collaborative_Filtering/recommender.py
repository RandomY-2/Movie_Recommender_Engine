# Collaborative Filtering Recommender

import pandas as pd
from scipy import sparse

corrMatrix = pd.read_csv('/dataset/item_similarity_df.csv')

def get_similar(movie_name,rating):
    similar_ratings = corrMatrix[movie_name]*(rating-2.5)
    similar_ratings = similar_ratings.sort_values(ascending=False)
    #print(type(similar_ratings))
    return similar_ratings

nMovie = 0
hasEnoughMovie = False
while True:
  watched_movies = []
  while not hasEnoughMovie:
    print('Please enter some movies you like(give at least three or four please): ')
    movie_title = input('Movie Title: ')
    movie_rating = int(input('Your Rating(1-5): '))
    watched_movies.append((movie_title, movie_rating))
    nMovie += 1
    if nMovie >= 3:
      print('Do you have more movies to add?')
      isEnd = input('Y/N')
      if isEnd == 'N':
        hasEnoughMovie = True
        break

  similar_movies = pd.DataFrame()
  for movie,rating in watched_movies:
      similar_movies = similar_movies.append(get_similar(movie,rating),ignore_index = True)

  top_ten_movies = list(similar_movies.sum().sort_values(ascending=False).head(10).index)
  recommendations = list(corrMatrix.iloc[top_ten_movies].title)

  print('')
  print('Based on your selections, we recommend you the following movies: ')
  print('')
  for movie in recommendations:
    print(movie)
  break

