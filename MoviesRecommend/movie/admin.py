from django.contrib import admin

from movie.models import User, Movie, Genre, Movie_hot, Movie_rating, Movie_similarity

admin.site.site_title = "Hybrid Movie Recommendation System Admin Panel"
admin.site.site_header = "Movie Recommendation System - Admin Panel"
admin.site.index_title = "Hybrid Algorithm Movie Recommendation System"


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Set the Fields Displayed in the List
    list_display = ['id', 'name', 'password', 'email']
    # Search
    search_fields = ['name', 'email']
    # Filter
    # list_filter = ['name']
    # Set the Number of Items Displayed per Page
    list_per_page = 12
    # Configure Sorting
    ordering = ['id']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Configure Fields Displayed in the List
    list_display = ['id', 'name']
    # Search
    search_fields = ['name']
    # Filter
    # list_filter = ['name']
    # Set the Number of Items Displayed per Page
    list_per_page = 12
    # Configure Sorting
    ordering = ['id']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # Configure Fields Displayed in the List
    list_display = ['id', 'name', 'imdb_id', 'time', 'release_time', 'intro', 'director', 'writers', 'actors', ]
    # Search
    search_fields = ['name', 'intro', 'writers', 'actors']
    # # Filter
    # list_filter = ['name', 'writers']
    # Set the Number of Items Displayed per Page
    list_per_page = 6
    # Configure Sorting
    ordering = ['id']


@admin.register(Movie_hot)
class Movie_hotAdmin(admin.ModelAdmin):
    # Configure Fields Displayed in the List
    list_display = ['id', 'movie', 'rating_number']
    # Search
    search_fields = ['movie__name']
    # # Filter
    # list_filter = ['name', 'writers']
    # Set the Number of Items Displayed per Page
    list_per_page = 6
    # Configure Sorting
    ordering = ['-rating_number']


@admin.register(Movie_rating)
class Movie_ratingAdmin(admin.ModelAdmin):
    # Configure Fields Displayed in the List
    list_display = ['id', 'user', 'movie', 'score', 'comment']
    # Search
    search_fields = ['user__name', 'movie__name']
    # # Filter
    # list_filter = ['name', 'writers']
    # Set the Number of Items Displayed per Page
    list_per_page = 6
    # Configure Sorting
    ordering = ['-score']


@admin.register(Movie_similarity)
class Movie_similarityAdmin(admin.ModelAdmin):
    # Configure Fields Displayed in the List
    list_display = ['id', 'movie_source', 'movie_target', 'similarity']
    # Search
    search_fields = ['movie_source__name', 'movie_source__name']
    # # Search
    # list_filter = ['name', 'writers']
    # Set the Number of Items Displayed per Page
    list_per_page = 6
    # Configure Sorting
    ordering = ['-similarity']
