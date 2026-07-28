import os.path
import time

from django.contrib import messages
from django.db.models import Max, Count
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, ListView, DetailView

from .forms import RegisterForm, LoginForm, CommentForm
from .models import User, Movie, Movie_rating, Movie_hot

BASE = os.path.dirname(os.path.abspath(__file__))


# Home Page View
class IndexView(ListView):
    model = Movie
    template_name = 'movie/index.html'
    paginate_by = 15
    context_object_name = 'movies'
    ordering = 'imdb_id'
    page_kwarg = 'p'

    # Return the First 1,000 Movies
    def get_queryset(self):
        return Movie.objects.filter(imdb_id__lte=1000)

    # Retrieve Context Data
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data(*kwargs)
        paginator = context.get('paginator')  # Paginator Object
        page_obj = context.get('page_obj')  # Current Page Object
        pagination_data = self.get_pagination_data(paginator, page_obj)  # Retrieve Paginated Data
        context.update(pagination_data)  # Return the Updated Context Data
        return context

   # Retrieve Paginated Data
    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
            left_has_more = False
        else:
            left_pages = range(current_page - around_count, current_page)
            left_has_more = True

        if current_page >= paginator.num_pages - around_count - 1:
            right_pages = range(current_page + 1, paginator.num_pages + 1)
            right_has_more = False
        else:
            right_pages = range(current_page + 1, current_page + 1 + around_count)
            right_has_more = True
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }


# Popular Movies View
class PopularMovieView(ListView):
    model = Movie_hot
    template_name = 'movie/hot.html'
    paginate_by = 15
    context_object_name = 'movies'
    page_kwarg = 'p'

    def get_queryset(self):
        # Initialization: Calculate the 100 Movies with the Most Ratings and Save Them to the Database
        movies = Movie.objects.annotate(nums=Count('movie_rating__score')).order_by('-nums')[:100]
        for movie in movies:
            record = Movie_hot(movie=movie, rating_number=movie.nums)
            record.save()

        hot_movies = Movie_hot.objects.all().values("movie_id")
        movies = Movie.objects.filter(id__in=hot_movies).annotate(nums=Max('movie_hot__rating_number')).order_by(
            '-nums')
        return movies

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PopularMovieView, self).get_context_data(*kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
            left_has_more = False
        else:
            left_pages = range(current_page - around_count, current_page)
            left_has_more = True

        if current_page >= paginator.num_pages - around_count - 1:
            right_pages = range(current_page + 1, paginator.num_pages + 1)
            right_has_more = False
        else:
            right_pages = range(current_page + 1, current_page + 1 + around_count)
            right_has_more = True
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }


# Movie Category View
class TagView(ListView):
    model = Movie
    template_name = 'movie/tag.html'
    paginate_by = 15
    context_object_name = 'movies'
    page_kwarg = 'p'

    # Retrieve Data
    def get_queryset(self):
        # No Category Selected
        if 'genre' not in self.request.GET.dict().keys() or self.request.GET.dict()['genre'] == "":
            movies = Movie.objects.all()
            return movies[100:200]
        # Category Selected
        else:
            movies = Movie.objects.filter(genre__name=self.request.GET.dict()['genre'])
            print(movies)
            return movies[:100]

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TagView, self).get_context_data(*kwargs)
        if 'genre' in self.request.GET.dict().keys():
            genre = self.request.GET.dict()['genre']
            context.update({'genre': genre})
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
            left_has_more = False
        else:
            left_pages = range(current_page - around_count, current_page)
            left_has_more = True

        if current_page >= paginator.num_pages - around_count - 1:
            right_pages = range(current_page + 1, paginator.num_pages + 1)
            right_has_more = False
        else:
            right_pages = range(current_page + 1, current_page + 1 + around_count)
            right_has_more = True
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }


# Movie Search View
class SearchView(ListView):
    model = Movie
    template_name = 'movie/search.html'
    paginate_by = 15
    context_object_name = 'movies'
    page_kwarg = 'p'

    def get_queryset(self):
        movies = Movie.objects.filter(name__icontains=self.request.GET.dict()['keyword'])
        return movies

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(SearchView, self).get_context_data(*kwargs)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        context.update({'keyword': self.request.GET.dict()['keyword']})
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
            left_has_more = False
        else:
            left_pages = range(current_page - around_count, current_page)
            left_has_more = True

        if current_page >= paginator.num_pages - around_count - 1:
            right_pages = range(current_page + 1, paginator.num_pages + 1)
            right_has_more = False
        else:
            right_pages = range(current_page + 1, current_page + 1 + around_count)
            right_has_more = True
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }


# Registration View
class RegisterView(View):
    def get(self, request):
        return render(request, 'movie/register.html')

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('movie:index'))
        else:
            # If Form Validation Fails, Redirect to the Registration Page
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            print(form.errors.get_json_data())
            return redirect(reverse('movie:register'))


# Login View
class LoginView(View):
    def get(self, request):
        return render(request, 'movie/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            pwd = form.cleaned_data.get('password')
            remember = form.cleaned_data.get('remember')
            user = User.objects.filter(name=name, password=pwd).first()
            if user:
                if remember:
                    # Set to None to Use the Global Expiration Time
                    request.session.set_expiry(None)
                else:
                    # Expire Immediately
                    request.session.set_expiry(0)
                # Login Successful: Store the Current User's ID in the Session as an Identifier
                request.session['user_id'] = user.id
                return redirect(reverse('movie:index'))

            else:
                messages.info(request, 'Incorrect username or password!')
                return redirect(reverse('movie:login'))
        else:
            errors = form.get_errors()
            for error in errors:
                messages.info(request, error)
            return redirect(reverse('movie:login'))


# Log Out and Immediately Destroy the Session
def UserLogout(request):
    request.session.set_expiry(-1)
    return redirect(reverse('movie:index'))


# Movie Details View
class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie/detail.html'
    # Context Object Name
    context_object_name = 'movie'

    # Override the Context Retrieval Method to Include the Rating Parameter
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Used to Check Whether the User Is Logged In
        login = True
        try:
            user_id = self.request.session['user_id']
        except KeyError as e:
            login = False  # Not Logged In

        # Get the Movie ID
        pk = self.kwargs['pk']
        movie = Movie.objects.get(pk=pk)

        if login:
            # If Logged In, Retrieve the Current User's Rating History
            user = User.objects.get(pk=user_id)

            rating = Movie_rating.objects.filter(user=user, movie=movie).first()
            # Default Value
            score = 0
            comment = ''
            if rating:
                score = rating.score
                comment = rating.comment
            context.update({'score': score, 'comment': comment})

        similarity_movies = movie.get_similarity()
        # Retrieve Movies Most Similar to the Current Movie
        context.update({'similarity_movies': similarity_movies})
        # Check Whether the User Is Logged In; Hide the Rating Page If Not Logged In
        context.update({'login': login})

        return context

    # Accept the Rating Form; pk Is the Database Primary Key ID of the Current Movie
    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            # Retrieve the Rating and Review
            score = form.cleaned_data.get('score')
            comment = form.cleaned_data.get('comment')
            # Retrieve the User and Movie
            user_id = request.session['user_id']
            user = User.objects.get(pk=user_id)
            movie = Movie.objects.get(pk=pk)

            # Update a Record
            rating = Movie_rating.objects.filter(user=user, movie=movie).first()
            if rating:
                # Update If It Exists
                # print(rating)
                rating.score = score
                rating.comment = comment
                rating.save()
            else:
                # Add If It Does Not Exist
                rating = Movie_rating(user=user, movie=movie, score=score, comment=comment)
                rating.save()
            messages.info(request, "Review submitted successfully!")
        else:
            # Form Validation Failed
            messages.info(request, "Rating cannot be empty!")
        return redirect(reverse('movie:detail', args=(pk,)))


# Rating History View
class RatingHistoryView(DetailView):
    model = User
    template_name = 'movie/history.html'
    # Context Object Name
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        # Object to Add Here: Movie Rating History of the Current User
        context = super().get_context_data(**kwargs)
        user_id = self.request.session['user_id']
        user = User.objects.get(pk=user_id)
        # Retrieve Ratings Only
        ratings = Movie_rating.objects.filter(user=user).order_by('-score')
        context.update({'ratings': ratings})
        return context


# Delete Rating and Review Data
def delete_recode(request, pk):
    movie = Movie.objects.get(pk=pk)
    user_id = request.session['user_id']
    user = User.objects.get(pk=user_id)
    rating = Movie_rating.objects.get(user=user, movie=movie)
    rating.delete()
    messages.info(request, f"Delete {movie.name} Rating saved successfully!")
    # Redirect Back to Rating History
    return redirect(reverse('movie:history', args=(user_id,)))


# Movie Recommendation View
class RecommendMovieView(ListView):
    model = Movie
    template_name = 'movie/recommend.html'
    paginate_by = 15
    context_object_name = 'movies'
    ordering = 'movie_rating__score'
    page_kwarg = 'p'

    def __init__(self):
        super().__init__()
        # Top 20 Most Similar Users
        self.K = 20
        # Recommend 10 Books
        self.N = 10
        # QuerySet Containing Movies Rated by the Current User
        self.cur_user_movie_qs = None

    # Retrieve User Similarity
    def get_user_sim(self):
        # User Similarity Dictionary, Format: {user_id1: val, user_id2: val, ...}
        user_sim_dct = dict()
        '''Calculate the Similarity Between Users and Store It in user_sim_dct'''
        # Retrieve the Current User
        cur_user_id = self.request.session['user_id']
        cur_user = User.objects.get(pk=cur_user_id)
        # Retrieve Other Users
        other_users = User.objects.exclude(pk=cur_user_id)  # All Users Except the Current User
        
        # Movies Rated by the Current User
        self.cur_user_movie_qs = Movie.objects.filter(user=cur_user)

        # Calculate the Number of Movies Rated by Both the Current User and Other Users
        for user in other_users:
            # Record the Number of Common Interests
            user_sim_dct[user.id] = len(Movie.objects.filter(user=user) & self.cur_user_movie_qs)

        # Sort by Value and Return the K Most Similar Users
        print("user similarity calculated!")
        # Format: [(user, value), (user, value), ...]
        return sorted(user_sim_dct.items(), key=lambda x: -x[1])[:self.K]

    # Retrieve Recommended Movies (Sorted by the Total Ratings from Similar Users)
    def get_recommend_movie(self, user_lst):
        # Movie Interest Value Dictionary: {movie: value, movie: value, ...}
        movie_val_dct = dict()
        # User and Similarity
        for user, _ in user_lst:
            # Retrieve Movies Rated by Similar Users but Not Rated by the Current User, and Include the Score Field for Calculating Interest Values
            movie_set = Movie.objects.filter(user=user).exclude(id__in=self.cur_user_movie_qs).annotate(
                score=Max('movie_rating__score'))
            for movie in movie_set:
                movie_val_dct.setdefault(movie, 0)
                # Accumulate User Ratings
                movie_val_dct[movie] += movie.score
        return sorted(movie_val_dct.items(), key=lambda x: -x[1])[:self.N]

    # Retrieve Data
    def get_queryset(self):
        s = time.time()
        # Get the List of the K Most Similar Users
        user_lst = self.get_user_sim()
        # Get the List of the K Most Similar Users
        movie_lst = self.get_recommend_movie(user_lst)
        # print(movie_lst)
        result_lst = []
        for movie, _ in movie_lst:
            result_lst.append(movie)
        e = time.time()
        print(f"Get the Recommended Movie IDs. Algorithm Execution Time: {e - s} Seconds!")
        return result_lst

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RecommendMovieView, self).get_context_data(*kwargs)
        print(context)
        paginator = context.get('paginator')
        page_obj = context.get('page_obj')
        pagination_data = self.get_pagination_data(paginator, page_obj)
        context.update(pagination_data)
        return context

    def get_pagination_data(self, paginator, page_obj, around_count=2):
        current_page = page_obj.number

        if current_page <= around_count + 2:
            left_pages = range(1, current_page)
            left_has_more = False
        else:
            left_pages = range(current_page - around_count, current_page)
            left_has_more = True

        if current_page >= paginator.num_pages - around_count - 1:
            right_pages = range(current_page + 1, paginator.num_pages + 1)
            right_has_more = False
        else:
            right_pages = range(current_page + 1, current_page + 1 + around_count)
            right_has_more = True
        return {
            'left_pages': left_pages,
            'right_pages': right_pages,
            'current_page': current_page,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more
        }
