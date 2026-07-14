from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.contrib.sessions.middleware import SessionMiddleware

from .forms import RegisterForm
from .models import Genre, Movie, Movie_similarity, User, Movie_rating
from .views import RecommendMovieView


class Practical7AutomatedTests(TestCase):
    """Automated tests for Practical 7 Test-driven Development."""

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.action = Genre.objects.create(name="Action")
        self.comedy = Genre.objects.create(name="Comedy")
        self.sci_fi = Genre.objects.create(name="Sci-Fi")

        self.movie1 = Movie.objects.create(
            name="Inception",
            imdb_id=1,
            time="148",
            release_time="2010",
            intro="A mind-bending action movie.",
            director="Christopher Nolan",
            writers="Christopher Nolan",
            actors="Leonardo DiCaprio",
        )
        self.movie1.genre.add(self.action, self.sci_fi)

        self.movie2 = Movie.objects.create(
            name="Toy Story",
            imdb_id=2,
            time="81",
            release_time="1995",
            intro="An animated comedy movie.",
            director="John Lasseter",
            writers="Joss Whedon",
            actors="Tom Hanks",
        )
        self.movie2.genre.add(self.comedy)

        self.movie3 = Movie.objects.create(
            name="Interstellar",
            imdb_id=3,
            time="169",
            release_time="2014",
            intro="A science fiction movie about space travel.",
            director="Christopher Nolan",
            writers="Jonathan Nolan",
            actors="Matthew McConaughey",
        )
        self.movie3.genre.add(self.sci_fi)

        self.movie4 = Movie.objects.create(
            name="The Matrix",
            imdb_id=4,
            time="136",
            release_time="1999",
            intro="A classic action science fiction movie.",
            director="The Wachowskis",
            writers="The Wachowskis",
            actors="Keanu Reeves",
        )
        self.movie4.genre.add(self.action, self.sci_fi)

        self.user = User.objects.create(
            name="alice",
            password="password123",
            email="alice@example.com",
        )
        self.similar_user = User.objects.create(
            name="bob",
            password="password123",
            email="bob@example.com",
        )
        self.other_user = User.objects.create(
            name="charlie",
            password="password123",
            email="charlie@example.com",
        )

        Movie_rating.objects.create(user=self.user, movie=self.movie1, score=5, comment="Excellent")
        Movie_rating.objects.create(user=self.similar_user, movie=self.movie1, score=5, comment="Excellent")
        Movie_rating.objects.create(user=self.similar_user, movie=self.movie3, score=4.5, comment="Great")
        Movie_rating.objects.create(user=self.other_user, movie=self.movie2, score=4, comment="Funny")
        Movie_rating.objects.create(user=self.other_user, movie=self.movie4, score=4.5, comment="Cool")

        Movie_similarity.objects.create(
            movie_source=self.movie1,
            movie_target=self.movie4,
            similarity=0.9,
        )

    def _request_with_session(self, user_id):
        request = self.factory.get(reverse("movie:recommend"))
        middleware = SessionMiddleware(lambda req: None)
        middleware.process_request(request)
        request.session["user_id"] = user_id
        request.session.save()
        return request

    # User Story 1: User Registration and Login

    def test_register_form_accepts_valid_user_data(self):
        form = RegisterForm(
            data={
                "name": "newuser",
                "password": "abc12345",
                "password_repeat": "abc12345",
                "email": "newuser@example.com",
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_form_rejects_mismatched_passwords(self):
        form = RegisterForm(
            data={
                "name": "newuser2",
                "password": "abc12345",
                "password_repeat": "different123",
                "email": "newuser2@example.com",
            }
        )
        self.assertFalse(form.is_valid())

    def test_login_view_sets_user_session_with_valid_credentials(self):
        response = self.client.post(
            reverse("movie:login"),
            {"name": "alice", "password": "password123", "remember": 1},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.client.session.get("user_id"), self.user.id)

    # User Story 2: Browse Movie List

    def test_index_view_returns_success_status(self):
        response = self.client.get(reverse("movie:index"))
        self.assertEqual(response.status_code, 200)

    def test_index_view_contains_movie_list_context(self):
        response = self.client.get(reverse("movie:index"))
        self.assertIn(self.movie1, list(response.context["movies"]))

    def test_movie_average_score_is_calculated_correctly(self):
        self.assertEqual(self.movie1.get_score(), 5.0)

    # User Story 3: Search Movies by Keyword

    def test_keyword_search_finds_matching_movie(self):
        response = self.client.get(reverse("movie:search"), {"keyword": "Inception"})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.movie1, list(response.context["movies"]))

    def test_keyword_search_is_case_insensitive(self):
        response = self.client.get(reverse("movie:search"), {"keyword": "inception"})
        self.assertIn(self.movie1, list(response.context["movies"]))

    def test_keyword_search_excludes_non_matching_movies(self):
        response = self.client.get(reverse("movie:search"), {"keyword": "Inception"})
        self.assertNotIn(self.movie2, list(response.context["movies"]))

    # User Story 4: Search Movies by Tags

    def test_tag_search_returns_movies_in_selected_genre(self):
        response = self.client.get(reverse("movie:tag"), {"genre": "Action"})
        movies = list(response.context["movies"])
        self.assertIn(self.movie1, movies)
        self.assertIn(self.movie4, movies)

    def test_tag_search_excludes_movies_from_other_genres(self):
        response = self.client.get(reverse("movie:tag"), {"genre": "Action"})
        self.assertNotIn(self.movie2, list(response.context["movies"]))

    def test_tag_search_without_genre_returns_success_status(self):
        response = self.client.get(reverse("movie:tag"))
        self.assertEqual(response.status_code, 200)

    # User Story 5: Automatic Movie Recommendation

    def test_movie_similarity_returns_related_movies(self):
        similar_movies = list(self.movie1.get_similarity(k=1))
        self.assertIn(self.movie4, similar_movies)

    def test_recommendation_returns_unrated_movie_from_similar_user(self):
        request = self._request_with_session(self.user.id)
        view = RecommendMovieView()
        view.request = request

        similar_users = view.get_user_sim()
        recommended_movies = [movie for movie, score in view.get_recommend_movie(similar_users)]

        self.assertIn(self.movie3, recommended_movies)

    def test_recommendation_excludes_movies_already_rated_by_current_user(self):
        request = self._request_with_session(self.user.id)
        view = RecommendMovieView()
        view.request = request

        similar_users = view.get_user_sim()
        recommended_movies = [movie for movie, score in view.get_recommend_movie(similar_users)]

        self.assertNotIn(self.movie1, recommended_movies)
