# CP3407 Movie Recommendation System

## GitHub Repository

GitHub link: https://github.com/MojunZheng/CP3407-Movie-Recommendation-System

---

## Project Overview

This project is a web-based movie recommendation system developed for CP3407 / CP5507 Advanced Software Engineering. The system helps users browse, search, rate, and discover movies more easily.

The current implementation is a **Python Django** web application. Users can register and log in, browse the movie list, search movies by keyword, filter movies by genre/tag, view movie details, rate and comment on movies, check their rating history, and receive automatic movie recommendations based on similar users and movie similarity data.

The system also provides a Django administrator backend for managing movie-related data, including movies, genres, users, ratings, popular movies, and movie similarity records.

---

## Objectives

- To develop a web-based movie recommendation system.
- To allow users to register and log in to the system.
- To help users browse and search movie information efficiently.
- To support tag/genre-based movie filtering.
- To allow users to rate movies and write comments.
- To provide movie recommendations based on user rating behaviour and movie similarity.
- To provide an administrator backend for managing movie data.
- To apply Agile iteration planning, GitHub tracking, Test-driven Development, automated testing, bug/error tracking, and system testing.

---

## Current Implemented Features

### User Features

- User registration
- User login and logout
- Movie list browsing
- Popular movie display
- Movie search by keyword
- Movie filtering by genre/tag
- Movie detail page
- Movie rating and comment submission
- Rating history page
- Delete rating record
- Automatic movie recommendation
- Similar movie display on the movie detail page

### Administrator Features

- Django admin backend
- Manage movie information
- Manage movie genres
- Manage user information
- Manage movie ratings and comments
- Manage movie similarity records
- Manage popular movie records

### Testing and Tracking Features

- Practical 7 automated testing
- Practical 8 mock object testing
- Practical 9 bug/error tracking
- GitHub Issues for bug reports and improvements
- GitHub Project Board for bug status tracking
- Week 10 demo system testing plan
- Bug report template with reproduce steps, expected result, actual result, severity, and priority

---

## Technology Stack

| Area | Technology |
|---|---|
| Front-end | HTML, CSS, JavaScript, Bootstrap, jQuery |
| Back-end | Python, Django |
| Database | MySQL |
| Testing | Django TestCase, SQLite in-memory test database, unittest.mock |
| Version Control | GitHub |
| IDE | PyCharm |

---

## Team Members and Roles

| Student Name | Role |
|---|---|
| Mojun Zheng | Project Manager and Documentation |
| Junfei Chen | Front-end Developer |
| Song Yuheng | Back-end Developer |
| Weng Yuchuan | Tester and UI/UX Designer |

---

## Initial Backlog Ideas

1. As a new user, I want to register an account, so that I can create my own profile in the movie recommendation system.

2. As a registered user, I want to log in to my account, so that the system can identify me and show my saved information.

3. As a user, I want to browse the movie list, so that I can view available movies and their basic ratings.

4. As a user, I want to search for movies by entering keywords, so that I can find specific movies more quickly.

5. As a user, I want to search for movies by tags or genres, so that I can quickly find movies that match my interests.

6. As a user, I want to view detailed movie information, so that I can decide whether a movie is suitable for me.

7. As a user, I want to rate and comment on movies, so that I can record my opinion and provide data for recommendations.

8. As a user, I want to view my rating history, so that I can check the movies I have rated before.

9. As a user, I want the system to recommend movies based on similar users and movie similarity, so that I can discover suitable movies more efficiently.

10. As an administrator, I want to manage movie, genre, rating, and user data in the backend, so that the movie database can remain organised and accurate.

---

## Iteration User Stories

### Iteration 1

| User Story | Priority | Effort | Status |
|---|---:|---:|---|
| User Registration and Login | 50 | 10 days | Completed |
| Search Movies by Tags | 50 | 8 days | Completed |
| View Landing Page | 40 | 10 days | Completed |
| Browse Movie List | 40 | 12 days | Completed |
| Search Movies by Keyword | 50 | 5 days | Completed |

Actual velocity of Iteration 1: **45 person-days**.

### Iteration 2

| User Story | Priority | Effort | Status |
|---|---:|---:|---|
| Admin Add Movie Information | 40 | 30 days | Completed |
| Favourite Movies | 40 | 30 days | Completed |
| Automatic Movie Recommendation | 50 | 20 days | Completed |

Actual velocity of Iteration 2: **80 person-days**.

### Iteration 3

| User Story | Priority | Effort | Status |
|---|---:|---:|---|
| Admin Delete Movie Information | 30 | 10 days | Todo |
| Admin Update Movie Information | 40 | 25 days | Todo |
| Edit User Personal Information | 30 | 15 days | Todo |

Planned effort of Iteration 3: **50 person-days**.

> Note: The current Django implementation mainly supports movie browsing, search, rating/comment history, recommendation, and backend data management. Some backlog items may be represented through the Django admin backend or iteration documentation.

---

## Project Structure

```text
MoviesRecommend/
├── manage.py
├── README.md
├── practical7_tdd_testing_plan.md
├── practical8_iteration3_tdd.md
├── practical8_test_result.png
├── practical9_bug_tracking_and_system_testing.md
├── practical9_bug_issues_screenshot.png
├── practical9_project_board_screenshot.png
├── practical9_instructor_access.png
├── movie/
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── test_practical8_mock.py
│   ├── urls.py
│   ├── views.py
│   ├── migrations/
│   └── static/
├── Movie_recommendation_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── test_settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
├── templates/
└── venv/
```

---

## Main Files

| File / Folder | Description |
|---|---|
| `manage.py` | Django management command file |
| `movie/models.py` | Defines movie, genre, user, rating, popular movie, and similarity models |
| `movie/views.py` | Handles page logic for index, login, register, search, tag filtering, detail, history, and recommendation pages |
| `movie/forms.py` | Defines registration, login, and comment/rating forms |
| `movie/urls.py` | Defines URL routes for the movie app |
| `movie/admin.py` | Registers movie-related models in the Django admin backend |
| `movie/tests.py` | Contains automated tests for Practical 7 |
| `movie/test_practical8_mock.py` | Contains the Practical 8 mock object login test |
| `practical9_bug_tracking_and_system_testing.md` | Contains the Practical 9 bug/error tracking process and Week 10 system testing plan |
| `Movie_recommendation_system/settings.py` | Main Django settings file |
| `Movie_recommendation_system/test_settings.py` | Test settings using SQLite in-memory database |
| `templates/` | HTML templates |
| `static/` | Global static resources |
| `movie/static/` | Movie app static resources, including movie data and posters |

---

## Database Models

| Model | Description |
|---|---|
| `Genre` | Stores movie genre/type information |
| `Movie` | Stores movie information such as name, IMDb ID, duration, genre, release time, introduction, director, writers, and actors |
| `Movie_similarity` | Stores similarity relationships between movies |
| `User` | Stores custom user account information |
| `Movie_rating` | Stores user ratings and comments for movies |
| `Movie_hot` | Stores popular movie records based on rating count |

---

## Main Routes

| Route | Description |
|---|---|
| `/` | Landing page |
| `/movie/` | Movie list page |
| `/movie/hot` | Popular movie page |
| `/movie/login` | User login page |
| `/movie/logout` | User logout |
| `/movie/register` | User registration page |
| `/movie/tag` | Movie genre/tag filtering page |
| `/movie/search` | Keyword search page |
| `/movie/detail/<id>` | Movie detail page |
| `/movie/history/<id>` | User rating history page |
| `/movie/del_rec/<id>` | Delete rating record |
| `/movie/recommend` | Recommendation page |
| `/admin/` | Django admin backend |

---

## Practical Documents

| File | Description |
|---|---|
| `practical5_iteration1_reflection.md` | Iteration 1 reflection, actual velocity, SRP/DRY check, and completed vs unfinished user stories |
| `practical6_iteration2_planning.md` | Iteration 2 planning, burndown chart, velocity usage, backlog update, and completed work |
| `practical7_tdd_testing_plan.md` | Practical 7 testing plan, selected user stories, 15 test cases, and automated testing summary |
| `practical8_iteration3_tdd.md` | Practical 8 Iteration 3 TDD plan, Iteration 2 reflection, velocity calculation, burndown chart, and mock object framework research |
| `practical8_test_result.png` | Evidence screenshot showing 16 automated tests passed |
| `practical9_bug_tracking_and_system_testing.md` | Practical 9 bug/error tracking process, bug report template, GitHub Issues tracking, and Week 10 demo system testing plan |
| `practical9_bug_issues_screenshot.png` | Evidence showing GitHub bug/improvement issues created for Practical 9 |
| `practical9_project_board_screenshot.png` | Evidence showing bugs tracked in the GitHub Project Board |
| `practical9_instructor_access.png` | Evidence showing instructor repository access invitation |

---

## Testing Summary

The project includes automated testing for Practical 7 and Practical 8.

### Practical 7 Testing

Five user stories were selected for testing:

- User Registration and Login
- Browse Movie List
- Search Movies by Keyword
- Search Movies by Tags
- Automatic Movie Recommendation

Each selected user story has 3 test cases, giving a total of **15 test cases**. The full test case table and testing discussion are documented in:

```text
practical7_tdd_testing_plan.md
```

The Practical 7 automated tests are implemented in:

```text
movie/tests.py
```

### Practical 8 Mock Object Testing

For Practical 8, the project includes one additional mock object test that simulates a user login process. This test uses Python's built-in mock object framework:

```python
from unittest.mock import Mock, patch
```

The Practical 8 mock test is implemented in:

```text
movie/test_practical8_mock.py
```

The mock test checks whether a simulated successful login process stores the user ID in the session correctly.

### Running Tests

To run all automated tests:

```bash
python manage.py test movie --settings=Movie_recommendation_system.test_settings
```

Successful local test result after adding Practical 8 mock testing:

```text
Found 16 test(s).
Ran 16 tests
OK
```

---

## Practical 9 Bug/Error Tracking Summary

For Practical 9, the team improved bug/error tracking by using GitHub Issues, labels, and the GitHub Project Board instead of only editing user story pages. Each bug or improvement should be recorded with clear reproduction steps, expected result, actual result, severity, priority, evidence, suggested fix, and status.

### Practical 9 GitHub Issues

| Issue | Type | Related Feature | Priority | Status |
|---|---|---|---|---|
| `#54 [Bug] Movie list pagination may show inconsistent order` | Bug | Browse Movie List | Low | Todo |
| `#55 [Bug] Parent user story status not updated after sub-issues completed` | Bug | Iteration 2 project tracking | Medium | Todo |
| `#56 [Improvement] Add clearer error message for invalid login` | Improvement | User Registration and Login | Medium | Todo |

### Bug Tracking Tools

| Tool | Purpose |
|---|---|
| GitHub Issues | Record bugs, errors, and improvements |
| GitHub Labels | Mark issue type, priority, and testing status |
| GitHub Project Board | Track issue progress using Todo, In Progress, Fixed, Verified, and Done |
| Pull Requests | Review bug fixes before merging |
| Screenshots | Provide evidence for testing and tracking |

---

## Week 10 Demo System Testing Plan

The Practical 9 system testing plan is prepared for the Week 10 demo. The plan tests the whole movie recommendation system from the user's perspective, including registration, login, movie browsing, searching, tag filtering, rating/commenting, rating history, recommendations, and Django admin management.

The detailed test cases are documented in:

```text
practical9_bug_tracking_and_system_testing.md
```

System testing will cover:

- Landing page and movie home page
- User registration and login
- Movie list, popular movies, and movie details
- Keyword search and genre/tag filtering
- Rating, comment, rating history, and delete rating record
- Automatic movie recommendation and similar movie display
- Django admin add, update, and delete movie records
- Automated test command result

Success criteria for the Week 10 demo include:

- Main pages load successfully without server errors.
- Core user functions work correctly.
- Recommendation and rating functions work correctly.
- Admin backend can manage movie-related data.
- Automated tests pass successfully.
- Bugs found during system testing are recorded in GitHub Issues.
- No critical bug remains unresolved before the demo.

---

## Instructor Access

For Practical 9, the instructor should be added as a collaborator/team member so that the GitHub repository and project records can be viewed.

| Instructor | Email | Access Purpose |
|---|---|---|
| Dasheng LIU | `dasheng.liu@jcu.edu.au` | View repository, project board, issues, and practical evidence |

Evidence should be saved as:

```text
practical9_instructor_access.png
```

---

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/MojunZheng/CP3407-Movie-Recommendation-System.git
cd CP3407-Movie-Recommendation-System
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install django pymysql
```

### 4. Configure MySQL Database

The project uses MySQL for normal development.

Create a MySQL database:

```sql
CREATE DATABASE db_movie_recommend CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

Then update the database connection in:

```text
Movie_recommendation_system/settings.py
```

Example configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db_movie_recommend",
        "USER": "root",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

### 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open the website:

```text
http://127.0.0.1:8000/
```

Movie pages are available under:

```text
http://127.0.0.1:8000/movie/
```

---

## Running Automated Tests

To run all Practical 7 and Practical 8 tests without changing the MySQL database:

```bash
python manage.py test movie --settings=Movie_recommendation_system.test_settings
```

The `test_settings.py` file uses an in-memory SQLite database, so the test data is temporary and is removed after the test run.

---

## GitHub Upload Notes

Do not upload the following folders/files:

```text
venv/
.idea/
__pycache__/
*.pyc
db.sqlite3
```

Recommended files/folders to upload:

```text
manage.py
README.md
movie/
Movie_recommendation_system/
templates/
static/
practical5_iteration1_reflection.md
practical6_iteration2_planning.md
practical7_tdd_testing_plan.md
practical8_iteration3_tdd.md
practical8_test_result.png
practical9_bug_tracking_and_system_testing.md
practical9_bug_issues_screenshot.png
practical9_project_board_screenshot.png
practical9_instructor_access.png
```

---

## Notes

- The project is implemented with Django, not PHP.
- The current implementation uses a custom `User` model instead of Django's default authentication model.
- Normal development uses MySQL.
- Automated tests use SQLite in-memory database through `test_settings.py`.
- Practical 7 automated tests passed locally with 15 tests.
- Practical 8 added one mock object test, and all 16 automated tests passed locally.
- Practical 9 added bug/error tracking through GitHub Issues, labels, Project Board status, and a Week 10 system testing plan.
