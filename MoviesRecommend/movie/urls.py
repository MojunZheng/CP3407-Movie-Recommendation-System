from django.urls import path

from . import views

app_name = 'movie'

# Sub-Routes
urlpatterns = [
    # Default Home Page
    path('', views.IndexView.as_view(), name='index'),
    # Popular Movies
    path('hot', views.PopularMovieView.as_view(), name='hot'),
    # Login
    path('login', views.LoginView.as_view(), name='login'),
    # Log Out
    path('logout', views.UserLogout, name='logout'),
    # Registration
    path('register', views.RegisterView.as_view(), name='register'),
    # Browse by Category
    path('tag', views.TagView.as_view(), name='tag'),
    # Search Function
    path('search', views.SearchView.as_view(), name='search'),
    # Movie Details Page
    path('detail/<int:pk>', views.MovieDetailView.as_view(), name='detail'),
    # Rating History Page
    path('history/<int:pk>', views.RatingHistoryView.as_view(), name='history'),
    # Delete Record
    path('del_rec/<int:pk>', views.delete_recode, name='delete_record'),
    # Recommendation Page
    path('recommend', views.RecommendMovieView.as_view(), name='recommend')
]
