#import webbrowser to allow trailers to be opened when clicked.
import webbrowser
"""
Class created to allow functionality for individual movies. It will track
title, storyline, poser image url, and youtube url for the trailer.
This project also keeps track of valid ratings for movies on a global
level for the class.
"""
class Movie():
    # class variable to keep track of valid ratings.
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NC-17"]
    # constructor function, allows users to pass in movie title, storyline, poster, and youtube trailer
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        # save all instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    # show_trailer method of the class allows the user to open the trailer for the instance movie.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
