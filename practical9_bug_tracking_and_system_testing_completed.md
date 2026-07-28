# Practical 9: Bug/Error Tracking and System Testing Plan

## Objective

The objective of Practical 9 is to examine and improve how the team reports and tracks bugs/errors from system testing. This practical also prepares a system testing plan that can be used for the Week 10 demo of the Hybrid Movie Recommendation System.

This document is based on Chapter 9: Ending an Iteration. The chapter explains that at the end of an iteration, the team should not only check completed user stories, but also perform system testing, track bugs properly, review the iteration, and improve the process for the next iteration.

---

## 1. Chapter 9 Summary and Application

Chapter 9 focuses on ending an iteration effectively. After the planned user stories are completed, the team should still check the system as a whole, perform system testing, report bugs clearly, and decide what should be fixed or improved next.

For this movie recommendation system project, Chapter 9 is useful because the project has completed several iterations and now needs a clearer way to record system-level problems. The team has automated tests from Practical 7 and Practical 8, but system testing is still needed because automated tests cannot fully cover every real user behaviour.

Chapter 9 explains that system testing should focus on the whole system from the user's perspective. This means testing the completed website through realistic user scenarios, such as registering, logging in, browsing movies, searching movies, rating movies, viewing recommendation results, and using the admin backend.

The chapter also explains that bugs should be recorded in a bug tracker, not only fixed informally. A bug report should include enough detail for another team member to understand, reproduce, fix, and verify the problem.

---

## 2. Current Bug/Error Tracking Approach

Before Practical 9, the team mainly used GitHub files, user story pages, and project board status to record project progress. This was useful for tracking normal user stories and tasks, but it was not detailed enough for bug/error reporting.

The previous approach had some weaknesses:

| Problem | Explanation |
|---|---|
| Bugs were not separated clearly from normal tasks | Bugs and improvements could be mixed with normal user stories. |
| Bug details were limited | Some problems did not include steps to reproduce, expected result, actual result, severity, priority, or evidence. |
| Parent issue status was not always updated | Some parent user stories still showed Todo even though sub-issues were completed. |
| Testing evidence was separated from bug records | Test screenshots and bug descriptions were not always linked together. |
| Bug verification was not clearly recorded | It was not always clear whether a bug was fixed, tested, or verified by another team member. |

To improve this, the team will use GitHub Issues, GitHub Project Board, labels, and Pull Requests to track bugs/errors more clearly.

---

## 3. Improved Bug/Error Tracking Tools

The team will use the following tools for Practical 9 and future bug/error tracking.

| Tool | How It Will Be Used |
|---|---|
| GitHub Issues | Record each bug, error, or improvement as a separate issue. |
| GitHub Labels | Mark issues with labels such as bug, testing, high-priority, medium-priority, low-priority, fixed, and verified. |
| GitHub Project Board | Track bug status using Todo, In Progress, Fixed, Verified, and Done. |
| Pull Requests | Review bug fixes before merging them into the main branch. |
| User Story Pages | Link bugs back to related user stories, such as login, search, recommendation, or admin management. |
| Test Result Screenshots | Provide evidence for automated tests and system testing results. |

This improves the process because bugs are no longer only written as text in user story pages. Each bug can have its own history, priority, status, discussion, testing evidence, and fix record.

---

## 4. Bug/Error Tracking Workflow

The team will use the following workflow for handling bugs/errors.

| Step | Action |
|---:|---|
| 1 | A tester or team member finds a bug during system testing. |
| 2 | The bug is recorded as a GitHub Issue using the bug report template. |
| 3 | The issue is linked to the related user story or feature. |
| 4 | The team adds labels such as bug, testing, priority, and status. |
| 5 | The bug is moved to the GitHub Project Board. |
| 6 | The team decides whether the bug should be fixed in the current iteration or a later iteration. |
| 7 | A developer fixes the bug and adds or updates a test if possible. |
| 8 | Another team member checks the fix. |
| 9 | The issue is marked as Fixed or Verified. |
| 10 | The bug report is closed after the tester confirms the fix. |

This workflow follows the Chapter 9 idea that a bug should be recorded, prioritised, fixed, checked, verified, and then closed.

---

## 5. Bug Report Template

The team will use the following bug report template in GitHub Issues.

```markdown
## Bug Summary

Write one clear sentence that describes the bug or improvement.
Example: Movie list pagination may show inconsistent order.

## Related User Story / Feature

Write the related user story or feature.
Example: Browse Movie List / Search Movies by Keyword / User Login / Automatic Movie Recommendation.

## Steps to Reproduce

1. Open the related page or function.
2. Perform the action that triggers the bug.
3. Observe the incorrect result or warning message.

## Expected Result

Describe what should happen if the system works correctly.
Example: The movie list should display in a stable order without warning.

## Actual Result

Describe what actually happened.
Example: Django shows an UnorderedObjectListWarning during testing.

## Version / Platform / Location

- Browser: Microsoft Edge / Google Chrome
- Operating system: Windows
- URL or page: http://127.0.0.1:8000/movie/
- Test build / branch: main branch / local development build

## Severity

Low / Medium / High / Critical

## Priority

Low / Medium / High

## Evidence

Attach a screenshot, terminal output, test result, or link to the related file.

## Suggested Fix

Describe a possible fix.
Example: Add order_by() to the QuerySet before pagination.

## Status

Todo / In Progress / Fixed / Verified / Closed
```

This template helps the team record enough information for developers and testers to understand the bug later.

---

## 6. Example Bugs and Improvements for This Project

The following bugs/improvements can be created as GitHub Issues for Practical 9 evidence.

### Issue 1: Movie list pagination may show inconsistent order

| Item | Detail |
|---|---|
| Issue Title | `[Bug] Movie list pagination may show inconsistent order` |
| Related Feature | Browse Movie List |
| Severity | Low |
| Priority | Low |
| Status | Todo |
| Description | During automated testing, Django showed an `UnorderedObjectListWarning`. This warning means pagination may show inconsistent results if the movie QuerySet is not ordered. |
| Steps to Reproduce | 1. Open PowerShell in the project root folder. 2. Run `python manage.py test movie --settings=Movie_recommendation_system.test_settings`. 3. Check the terminal output and observe the `UnorderedObjectListWarning`. |
| Expected Result | Movie list pagination should show movies in a stable and consistent order. |
| Actual Result | Django shows a warning during testing. |
| Suggested Fix | Add an `order_by()` clause to the Movie QuerySet, such as ordering by `id`, `name`, or `release_time`. |

### Issue 2: Parent user story status not updated after sub-issues completed

| Item | Detail |
|---|---|
| Issue Title | `[Bug] Parent user story status not updated after sub-issues completed` |
| Related Feature | Iteration 2 project tracking |
| Severity | Medium |
| Priority | Medium |
| Status | Todo |
| Description | Some parent user stories still showed Todo even though all related sub-issues were completed. |
| Steps to Reproduce | 1. Open the GitHub Project Board or issue list. 2. Check the Iteration 2 parent user stories. 3. Compare the parent status with the sub-issue completion status. |
| Expected Result | When all sub-issues are completed, the parent user story should also be updated to Done. |
| Actual Result | Parent user story status was not updated consistently. |
| Suggested Fix | Check and update parent issue status during each iteration review. |

### Issue 3: Invalid login message should be clearer

| Item | Detail |
|---|---|
| Issue Title | `[Improvement] Add clearer error message for invalid login` |
| Related Feature | User Registration and Login |
| Severity | Low |
| Priority | Medium |
| Status | Todo |
| Description | The login page should clearly tell users when the username or password is incorrect. |
| Steps to Reproduce | 1. Open the login page. 2. Enter an incorrect username or password. 3. Click the Log In button and observe the feedback message. |
| Expected Result | The system should show a clear error message after invalid login. |
| Actual Result | The current login feedback needs to be checked and improved. |
| Suggested Fix | Add a visible validation message on the login page when login fails. |

### Issue 4: Admin update and delete functions need system testing

| Item | Detail |
|---|---|
| Issue Title | `[Testing] Verify admin update and delete movie functions` |
| Related Feature | Iteration 3 admin management |
| Severity | Medium |
| Priority | Medium |
| Status | Todo |
| Description | Iteration 3 includes Admin Delete Movie Information and Admin Update Movie Information. These functions need careful system testing because they change movie data. |
| Steps to Reproduce | 1. Log in to the Django admin backend. 2. Select an existing movie record. 3. Update or delete the movie record. 4. Check whether the change appears correctly in the movie list and detail page. |
| Expected Result | Admin users can update and delete movie information correctly, while normal users cannot access admin functions. |
| Actual Result | These features still need testing in Iteration 3. |
| Suggested Fix | Add manual system test cases and related automated tests where possible. |

---

## 7. Labels and Statuses

The team will use these labels in GitHub Issues.

| Label | Meaning |
|---|---|
| `bug` | A system error or incorrect behaviour |
| `improvement` | A function or UI that works but can be improved |
| `testing` | Related to testing or test evidence |
| `high-priority` | Should be fixed as soon as possible |
| `medium-priority` | Should be fixed if there is enough time |
| `low-priority` | Can be fixed later |
| `fixed` | Developer has fixed the issue |
| `verified` | Tester has checked and confirmed the fix |

The Project Board status columns will be:

| Status | Meaning |
|---|---|
| Todo | Bug or task has been recorded but not started |
| In Progress | Bug fix or testing is currently being worked on |
| Fixed | Developer believes the bug has been fixed |
| Verified | Tester has checked the fix |
| Done | Issue is completed and closed |

---

## 8. System Testing Plan for Week 10 Demo

System testing will be completed before the Week 10 demo. The purpose is to test the whole movie recommendation system from the user's perspective.

### 8.1 Testing Scope

The system testing plan covers:

- Landing page
- User registration
- User login and logout
- Movie list browsing
- Popular movies page
- Movie category/tag search
- Keyword search
- Movie detail page
- Rating and comment function
- Rating history page
- Delete rating record
- Automatic movie recommendation
- Similar movie display
- Django admin backend
- Automated test suite

### 8.2 Test Environment

| Item | Detail |
|---|---|
| Project | Hybrid Movie Recommendation System |
| Framework | Python Django |
| Database | MySQL for normal development, SQLite in-memory database for automated tests |
| Browser | Microsoft Edge or Google Chrome |
| Operating System | Windows |
| Local URL | `http://127.0.0.1:8000/` |
| Movie page URL | `http://127.0.0.1:8000/movie/` |
| Admin URL | `http://127.0.0.1:8000/admin/` |
| Test command | `python manage.py test movie --settings=Movie_recommendation_system.test_settings` |

### 8.3 Test Data

| Data Type | Example |
|---|---|
| Test user | A normal registered user account |
| Admin user | A Django superuser account |
| Movies | Existing movie records from the database |
| Genres | Action, Comedy, Drama, Romance, Horror, Animation, and other categories |
| Ratings | 1 to 5 rating values |
| Comments | Short text comments for movies |

The team should start system testing with known data and record whether the ending state is correct after each test. For example, after deleting a rating record, the rating should no longer appear in the user's rating history.

---

## 9. Week 10 Demo System Test Cases

| Test ID | Test Area | Steps | Expected Result | Status |
|---|---|---|---|---|
| ST-01 | Landing Page | Open `http://127.0.0.1:8000/` and click "Go to Home Page". | User is taken to the movie home page. | Not Started |
| ST-02 | Registration | Open Register page, enter username, email, password, and confirm password. | User account is created successfully. | Not Started |
| ST-03 | Login | Open Login page and enter valid username and password. | User logs in successfully and session is created. | Not Started |
| ST-04 | Invalid Login | Enter wrong username or password. | System rejects login and shows an error message. | Not Started |
| ST-05 | Movie List | Open movie home page. | Movie posters, titles, years, and ratings are displayed. | Not Started |
| ST-06 | Popular Movies | Open Popular Movies page. | Popular movies are displayed correctly. | Not Started |
| ST-07 | Category Search | Open Movie Categories page and select a genre. | Movies from the selected genre are displayed. | Not Started |
| ST-08 | Keyword Search | Enter a movie keyword and click Search Movies. | Movies matching the keyword are displayed. | Not Started |
| ST-09 | Movie Detail | Click a movie title or poster. | Movie detail page opens with movie information. | Not Started |
| ST-10 | Rating and Comment | Log in, open a movie detail page, submit rating and comment. | Rating and comment are saved successfully. | Not Started |
| ST-11 | Rating History | Open user rating history page. | Previous ratings and comments are displayed. | Not Started |
| ST-12 | Delete Rating | Delete one rating record from history. | The selected rating record is removed. | Not Started |
| ST-13 | Recommendation | Log in and open recommendation page. | Recommended movies are displayed. | Not Started |
| ST-14 | Similar Movies | Open a movie detail page. | Similar movies are shown if similarity data exists. | Not Started |
| ST-15 | Admin Backend | Log in to Django admin backend. | Admin can view and manage movie-related models. | Not Started |
| ST-16 | Admin Add Movie | Add a new movie record through admin backend. | New movie is saved and appears in movie data. | Not Started |
| ST-17 | Admin Update Movie | Update existing movie information. | Updated movie information is saved correctly. | Not Started |
| ST-18 | Admin Delete Movie | Delete a test movie record. | Deleted movie record no longer appears. | Not Started |
| ST-19 | Automated Tests | Run Django automated tests. | Test result shows 16 tests passed. | Completed |
| ST-20 | Bug Reporting | Record any bug found during system testing as a GitHub Issue. | Bug is tracked with label, priority, status, and evidence. | Not Started |

---

## 10. Success Criteria for Week 10 Demo

The system is ready for the Week 10 demo if the following criteria are met:

| Criterion | Expected Result |
|---|---|
| Main pages load successfully | Landing page, home page, categories page, popular movies page, login page, and registration page load without server errors. |
| Core user functions work | Users can register, log in, browse movies, search movies, and view movie details. |
| Rating functions work | Logged-in users can submit ratings/comments and view rating history. |
| Recommendation function works | Logged-in users can view movie recommendations. |
| Admin backend works | Admin can manage movie-related data through Django admin. |
| Automated tests pass | Django test command runs successfully with 16 tests passed. |
| Bugs are tracked | Bugs found during testing are recorded in GitHub Issues. |
| Critical bugs are not open | No critical bug remains unresolved before the demo. |

---

## 11. Testing Roles

| Team Member | Role in System Testing |
|---|---|
| Mojun Zheng | Prepare documentation, testing plan, bug tracking records, and demo evidence |
| Junfei Chen | Check front-end pages, layout, navigation, and UI display problems |
| Song Yuheng | Check back-end functions, database operations, and bug fixes |
| Weng Yuchuan | Perform tester and UI/UX checking from the user perspective |

The tester should not only check their own work. The team should cross-check each other's functions so that system testing is closer to real user testing.

---

## 12. Instructor Access

The instructor should be added as a team member/collaborator so that the project can be viewed.

| Item | Detail |
|---|---|
| Instructor | Dasheng LIU |
| Email | `dasheng.liu@jcu.edu.au` |
| Access Purpose | Allow instructor to view the GitHub repository and project records |
| Repository | `https://github.com/MojunZheng/CP3407-Movie-Recommendation-System` |
| Current Status | Pending confirmation after GitHub invitation is sent |

After adding the instructor, the team should take a screenshot as evidence and save it as:

```text
practical9_instructor_access.png
```

The status can be updated to `Completed` after the invitation is sent or accepted.

---

## 13. Evidence to Upload

For Practical 9, the team should upload or prepare the following evidence:

| Evidence File / Item | Purpose |
|---|---|
| `practical9_bug_tracking_and_system_testing.md` | Main Practical 9 documentation |
| `practical9_instructor_access.png` | Evidence that the instructor was invited to the GitHub repository |
| `practical9_bug_issues_screenshot.png` | Evidence of GitHub Issues created for bug/error tracking |
| `practical9_project_board_screenshot.png` | Evidence that bugs/errors are monitored with labels and statuses |
| GitHub Issues | Actual bug/improvement records |
| GitHub Project Board | Bug/error monitoring status |

Suggested commit message:

```text
Add Practical 9 bug tracking and system testing plan
```

---

## 14. Summary

In Practical 9, the team improved the bug/error tracking process for the Hybrid Movie Recommendation System. Instead of only editing user story pages, the team will use GitHub Issues, labels, Project Board, and Pull Requests to track bugs more clearly.

The team also prepared a system testing plan for the Week 10 demo. The testing plan covers the main user functions, administrator functions, recommendation functions, and automated tests. Any bugs found during testing will be recorded using the bug report template and tracked until they are fixed and verified.
