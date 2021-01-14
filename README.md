# Movie_Recommender_Engine
 created both content-based and collaborative filtering recommender systems
 
 ## Content-Based Recommender
 
In the 'Content_Based_Recommender' folder I created a content-based recommender system using TMDB 5000 dataset. The system will calculate the cosine similarity between the  between the keyword, casts, genre, and director of the movie user enters and these information from all movies in the TMBD 5000 Movie Dataset and recommend top 10 most similar movies to the user. 

## Collaborative Filtering

In the 'Collaborative_Filtering' folder I created an item to item collaborative filtering recommender system using the MovieLens Dataset. The system will create a movie to movie dataframe and calculate the Pearson correlation between each movies. Then when the user gives a few ratings, the system will recommend the top 10 movies that are most similar to the movies the user gives a positive rating on. 

To use the collaborative filtering system, the user should first run item_similar.py to create the movie to movie dataframe from the MovieLens dataset and then run the recommender.py
