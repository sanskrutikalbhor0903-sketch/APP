class Movie:
    def __init__(self, movie_name, rating, ticket_price):
        self.movie_name = movie_name
        self.rating = rating
        self.ticket_price = ticket_price
        
    def categorize(self):
        if self.rating >= 7:
            return "Hit"
        elif self.rating >= 5:
            return "Average"
        else:
            return "Flop"

    def display(self):
        print("Movie Name  :", self.movie_name)
        print("Rating      :", self.rating)
        print("Ticket Price:", self.ticket_price)
        print("Category    :", self.categorize())
        print("-" * 30)

class Cinema:
    def __init__(self, cinema_name):
        self.cinema_name = cinema_name
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def display_movies(self):
        print("\nCinema Name:", self.cinema_name)
        print("=" * 30)

        for movie in self.movies:
            movie.display()

# Creating Cinema object
cinema = Cinema("PVR Cinemas")

# Creating Movie objects
m1 = Movie("Avengers", 8.5, 250)
m2 = Movie("RRR", 7.5, 200)
m3 = Movie("Movie C", 5.5, 150)
m4 = Movie("Movie D", 3.5, 100)

# Adding movies to cinema
cinema.add_movie(m1)
cinema.add_movie(m2)
cinema.add_movie(m3)
cinema.add_movie(m4)

# Display movie details
cinema.display_movies()