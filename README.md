# Movie-list
A python script which creates a list of movies on the basis of their IMDB score.

threshold rating : minimum rate required to sort the movies having an IMDB score equal or above the threshold rating and storing them in a text file.

1.) Install dependencies using 'pip install -r requirements.txt' 
2.) run python script with arg1 = threshhold rating ,arg2=name of movie1 in double quotes ,arg3=name of movie 2 in double quotes ... argN=name of movieN in double quotes

eg . python imdbtest.py 7.5 "the dark knight" "the dark knight rises" "the notebook"

3.) The above script will check IMDB rating of each movie in the argument and will output the movie name and rating for movies above threshold rating in a text file in the same directory with the name 'movies.txt'. 


