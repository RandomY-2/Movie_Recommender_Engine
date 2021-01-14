# Movie_Recommender_Engine
 created both content-based and collaborative filtering recommender systems
 
 ## Content-Based Recommender
 
In the 'Content_Based_Recommender' folder I created a content-based recommender system using TMDB 5000 dataset. The system will calculate the cosine similarity between the  between the keyword, casts, genre, and director of the movie user enters and these information from all movies in the TMBD 5000 Movie Dataset and recommend top 10 most similar movies to the user. 

## Collaborative Filtering

In the 'Collaborative_Filtering' folder I created a user to user collaborative filtering recommender system using the MovieLens Dataset. The system will calculate the centered cosine similarity between the mvoies and their ratings user enters and the ratings of these movies in the dataset. Then the system will recommend other movies that other users in the dataset that also have a positive rating on the movies the user has a positive ratings. 

To use the collaborative filtering system, the user should first run item_similar.py to create an augmented matrix from the MovieLens dataset and then run the recommender.py
