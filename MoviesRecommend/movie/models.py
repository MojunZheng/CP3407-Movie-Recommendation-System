from django.db import models
from django.db.models import Avg


# Category Information Table
class Genre(models.Model):
    name = models.CharField(max_length=100, verbose_name="Genre")

    class Meta:
        db_table = 'Genre'
        verbose_name = 'Movie Genre'
        verbose_name_plural = 'Movie Genre'

    def __str__(self):
        return self.name


# Movie Information Table
class Movie(models.Model):
    name = models.CharField(max_length=256, verbose_name="Movie Title")
    imdb_id = models.IntegerField(verbose_name="imdb_id")
    time = models.CharField(max_length=256, blank=True, verbose_name="Runtime")
    genre = models.ManyToManyField(Genre, verbose_name="Genre")
    release_time = models.CharField(max_length=256, blank=True, verbose_name="Release Date")
    intro = models.TextField(blank=True, verbose_name="Synopsis")
    director = models.CharField(max_length=256, blank=True, verbose_name="Director")
    writers = models.CharField(max_length=256, blank=True, verbose_name="Writer")
    actors = models.CharField(max_length=512, blank=True, verbose_name="Cast")
    # Similarity Between Movies: The Similarity Between A and B Is the Same as That Between B and A, So symmetrical Is Set to True
    movie_similarity = models.ManyToManyField("self", through="Movie_similarity", symmetrical=False,
                                              verbose_name="Similar Movies")

    class Meta:
        db_table = 'Movie'
        verbose_name = 'Movie Information'
        verbose_name_plural = 'Movie Information'

    def __str__(self):
        return self.name

    # Method for Calculating the Average Rating
    def get_score(self):
        result_dct = self.movie_rating_set.aggregate(Avg('score'))  # Format: {'score__avg': 3.125}
        try:
            result = round(result_dct['score__avg'], 1)  # Round to One Decimal Place
        except TypeError:
            return 0
        else:
            return result

    # Retrieve the User's Rating Information
    def get_user_score(self, user):
        return self.movie_rating_set.filter(user=user).values('score')

    # Integer Average Rating
    def get_score_int_range(self):
        return range(int(self.get_score()))

    # Retrieve the Category List
    def get_genre(self):
        genre_dct = self.genre.all().values('name')
        genre_lst = []
        for dct in genre_dct.values():
            genre_lst.append(dct['name'])
        return genre_lst

    # Retrieve Movie Similarity
    def get_similarity(self, k=5):
        # Retrieve the IDs of the 5 Most Similar Movies by Default
        similarity_movies = self.movie_similarity.all()[:k]
        return similarity_movies


# Movie Similarity
class Movie_similarity(models.Model):
    movie_source = models.ForeignKey(Movie, related_name='movie_source', on_delete=models.CASCADE, verbose_name="来源电影")
    movie_target = models.ForeignKey(Movie, related_name='movie_target', on_delete=models.CASCADE, verbose_name="目标电影")
    similarity = models.FloatField(verbose_name="Similarity")

    class Meta:
        # Sort by Similarity in Descending Order
        verbose_name = 'Movie Similarity'
        verbose_name_plural = 'Movie Similarity'


# User Information Table
class User(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Username")
    password = models.CharField(max_length=256, verbose_name="Password")
    email = models.EmailField(unique=True, verbose_name="Email")
    rating_movies = models.ManyToManyField(Movie, through="Movie_rating")

    def __str__(self):
        return "<USER:( name: {:},password: {:},email: {:} )>".format(self.name, self.password, self.email)

    class Meta:
        db_table = 'User'
        verbose_name = 'User Information'
        verbose_name_plural = 'User Information'


# Movie Rating Information Table
class Movie_rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, verbose_name="User")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, unique=False, verbose_name="Movie")
    score = models.FloatField(verbose_name="Score")
    comment = models.TextField(blank=True, verbose_name="Review")

    class Meta:
        db_table = 'Movie_rating'
        verbose_name = 'Movie Rating Information'
        verbose_name_plural = 'Movie Rating Information'


# Top 100 Most Popular Movies
class Movie_hot(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Movie Title")
    rating_number = models.IntegerField(verbose_name="Number of Ratings")

    class Meta:
        db_table = 'Movie_hot'
        verbose_name = 'Most Popular Movies'
        verbose_name_plural = 'Most Popular Movies'

# python manage.py makemigrations
# python manage.py migrate
