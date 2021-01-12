# Content-based Recommender System

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def get_title_from_index(df, index):
	return df[df.index == index]["title"].values[0]

def get_index_from_title(df, title):
	return df[df.title.str.lower() == title]["index"].values[0]

movie_data = pd.read_csv('movie_dataset.csv')

features = ['keywords', 'cast', 'genres', 'director']

for feature in features:
  movie_data[feature] = movie_data[feature].fillna('')

movie_data['combine_sentence'] = movie_data['keywords'] + ' ' + movie_data['cast'] + ' ' + movie_data['genres'] + ' ' + movie_data['director']

cv = CountVectorizer()
count_matrix = cv.fit_transform(movie_data['combine_sentence'])

cosine_sim = cosine_similarity(count_matrix)

print("Start Chatting!")

while True:
  movie_user_likes = input("")
  movie_user_likes = movie_user_likes.lower()
  movie_index = get_index_from_title(movie_data, movie_user_likes)

  similar_movies = list(enumerate(cosine_sim[movie_index]))
  sorted_list = sorted(similar_movies, key=lambda x: x[1], reverse=True)

  i = 0
  for movie in sorted_list:
    if get_title_from_index(movie_data, movie[0]).lower() != movie_user_likes:
      print(get_title_from_index(movie_data, movie[0]))
    i = i + 1
    if i > 10:
      break
  print("")
