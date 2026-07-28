from django.shortcuts import render


# Home Page
def index(request):
    return render(request, 'index.html')


# Rating
def star(request):
    return render(request, 'movie/star.html')
