# Practical 7: Test-driven Development

## 1. Testing Discussion and Plan

The project is a Django-based movie recommendation system. Testing should cover user account functions, movie browsing, movie search, tag filtering, and automatic movie recommendation.

The purpose of this Practical 7 testing plan is to apply Test-driven Development by identifying expected system behaviours, writing clear test cases, and implementing automated tests that can be run repeatedly.

### Testing Areas

| Testing Area | What Should Be Tested |
|---|---|
| User registration and login | Valid registration, invalid registration, valid login |
| Browse movie list | Page loading, movie list display, movie rating calculation |
| Search movies by keyword | Matching keyword, case-insensitive keyword, non-matching movie exclusion |
| Search movies by tags | Selected genre filtering, excluding unrelated genres, no-genre request |
| Automatic movie recommendation | Similar movie retrieval, recommendation from similar users, excluding already-rated movies |

### Testing Approach

The project uses Django, so automated tests can be implemented with Django `TestCase`. The tests should create temporary test data, execute model methods or views, and compare the actual result with the expected result.

The automated tests are placed in:

```text
movie/tests.py
```

The tests can be run with:

```bash
python manage.py test movie --settings=Movie_recommendation_system.test_settings
```

---

## 2. Selected User Stories for Testing

| No. | User Story |
|---:|---|
| 1 | User Registration and Login |
| 2 | Browse Movie List |
| 3 | Search Movies by Keyword |
| 4 | Search Movies by Tags |
| 5 | Automatic Movie Recommendation |

---

## 3. Test Cases

### User Story 1: User Registration and Login

| Test Case ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC01 | Register with valid user information | Valid username, password, repeated password, and email | The registration form is valid |
| TC02 | Register with mismatched passwords | Password and repeated password are different | The registration form is invalid |
| TC03 | Login with valid credentials | Existing username and correct password | The system stores the user ID in the session |

### User Story 2: Browse Movie List

| Test Case ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC04 | Open movie list page | GET request to movie index page | The page returns HTTP 200 |
| TC05 | Check movie list context | Existing movie records | The movie list contains the expected movie |
| TC06 | Calculate movie average score | Existing ratings for one movie | The average rating is calculated correctly |

### User Story 3: Search Movies by Keyword

| Test Case ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC07 | Search with exact keyword | Keyword: `Inception` | Matching movie is returned |
| TC08 | Search with lowercase keyword | Keyword: `inception` | Matching movie is still returned |
| TC09 | Exclude non-matching movies | Keyword: `Inception` | Unrelated movies are not returned |

### User Story 4: Search Movies by Tags

| Test Case ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC10 | Search by selected genre | Genre: `Action` | Movies with the selected genre are returned |
| TC11 | Exclude unrelated genre movies | Genre: `Action` | Movies from other genres are not returned |
| TC12 | Open tag page without selecting genre | No genre parameter | The page returns HTTP 200 |

### User Story 5: Automatic Movie Recommendation

| Test Case ID | Test Case | Test Data | Expected Result |
|---|---|---|---|
| TC13 | Get similar movies | Existing movie similarity record | Similar movie is returned |
| TC14 | Recommend movie from similar user | Current user and similar user rating data | An unrated movie from the similar user is recommended |
| TC15 | Exclude already-rated movie | Current user already rated one movie | The already-rated movie is not recommended again |

---

## 4. Automated Test Implementation Summary

The automated tests are implemented in `movie/tests.py`.

| Automated Test | Related Test Case |
|---|---|
| `test_register_form_accepts_valid_user_data` | TC01 |
| `test_register_form_rejects_mismatched_passwords` | TC02 |
| `test_login_view_sets_user_session_with_valid_credentials` | TC03 |
| `test_index_view_returns_success_status` | TC04 |
| `test_index_view_contains_movie_list_context` | TC05 |
| `test_movie_average_score_is_calculated_correctly` | TC06 |
| `test_keyword_search_finds_matching_movie` | TC07 |
| `test_keyword_search_is_case_insensitive` | TC08 |
| `test_keyword_search_excludes_non_matching_movies` | TC09 |
| `test_tag_search_returns_movies_in_selected_genre` | TC10 |
| `test_tag_search_excludes_movies_from_other_genres` | TC11 |
| `test_tag_search_without_genre_returns_success_status` | TC12 |
| `test_movie_similarity_returns_related_movies` | TC13 |
| `test_recommendation_returns_unrated_movie_from_similar_user` | TC14 |
| `test_recommendation_excludes_movies_already_rated_by_current_user` | TC15 |

Total automated tests implemented: **15**.

---

## 5. How to Run the Tests

Copy the files into the project using this structure:

```text
MoviesRecommend/
├── practical7_tdd_testing_plan.md
├── .gitignore
├── movie/
│   └── tests.py
└── Movie_recommendation_system/
    └── test_settings.py
```

Then run this command from the project root folder:

```bash
python manage.py test movie --settings=Movie_recommendation_system.test_settings
```

Expected result:

```text
Ran 15 tests
OK
```

If the project is already connected to a working MySQL test database, the normal command can also be used:

```bash
python manage.py test movie
```

---

## 6. Reflection

These tests help the team confirm that the main user-facing functions work correctly. The tests also reduce the risk of breaking existing features when new functions are added in later iterations. In future iterations, more tests can be added for administrator movie management, favourite movie management, invalid input handling, and full end-to-end user workflows.
