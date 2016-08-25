"""
Importing media to be used in this file.
media is a class I created with a class inside it called Movie.
fresh_tomoatoes was provided by Udacity in order to put the python project onto the web.
"""
import fresh_tomatoes
import media

"""
Below are a list of all movies used in the project. Each including:
Title
Description
Movie Poster
Movie Trailer from You Tube
"""
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg", "https://www.youtube.com/watch?v=4KPTXpQehio")
rocky = media.Movie("Rocky", "A story of a man, trying to beat the odds", "https://upload.wikimedia.org/wikipedia/en/thumb/1/18/Rocky_poster.jpg/220px-Rocky_poster.jpg", "https://www.youtube.com/watch?v=3VUblDwa648")
ferris = media.Movie("Ferris Bueller's Day Off", "A story of a boy who doesn't go to school.", "https://upload.wikimedia.org/wikipedia/en/thumb/9/9b/Ferris_Bueller%27s_Day_Off.jpg/220px-Ferris_Bueller%27s_Day_Off.jpg", "https://www.youtube.com/watch?v=ik0y8yWw7jU")
shawshank = media.Movie("Shawshank Redemption", "A story of a man wrongly imprisoned for killing his wife.", "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg", "https://www.youtube.com/watch?v=6hB3S9bIaco")
starwars = media.Movie("Star Wars Rouge One", "The seventh installment of an epic story.", "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Rogue_One%2C_A_Star_Wars_Story_poster.png/220px-Rogue_One%2C_A_Star_Wars_Story_poster.png", "https://www.youtube.com/watch?v=frdj1zb9sMY")
batman = media.Movie("The Dark Knight", "A story of Batman dealing with the Joker.", "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg", "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")

#all movies placed in array for distribution to fresh_tomatoes
movies=[toy_story, rocky, ferris, batman, starwars, shawshank]
#make call to fresh tomatoes, passing in movies.
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)
