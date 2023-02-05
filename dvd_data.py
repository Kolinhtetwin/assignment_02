class DvdData:
    def __init__(self, movie_name, movie_stars, producers, production_company, director, copies):
        self.movie_name = movie_name
        self.movie_stars = movie_stars
        self.producers = producers
        self.production_company = production_company
        self.director = director
        self.copies = copies

    def __str__(self):
        output = f"{self.movie_name} is starred by{self.movie_stars} and directed by{self.director} with "
