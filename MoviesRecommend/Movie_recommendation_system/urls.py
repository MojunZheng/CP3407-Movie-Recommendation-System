from django.contrib import admin
from django.urls import path, include

from .views import index, star

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin Management System
    path('', index),  # Home Page
    path('movie/', include('movie.urls')),  # Movie Recommendation System Sub-Routes
]
