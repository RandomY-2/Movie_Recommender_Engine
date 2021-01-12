import pandas as pd
from scipy import sparse

ratings = pd.read_csv('ratings.csv')
movies = pd.read_csv('movies.csv')
ratings = pd.merge(movies,ratings).drop(['genres','timestamp'],axis=1)

userRatings = ratings.pivot_table(index=['userId'],columns=['title'],values='rating')
userRatings.head()
userRatings = userRatings.dropna(thresh=10, axis=1).fillna(0,axis=1)

corrMatrix = userRatings.corr(method='pearson')
corrMatrix.to_csv('item_similarity_df.csv')