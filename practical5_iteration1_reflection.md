# Practical 5: Iteration 1 Reflection

## Completed vs Unfinished User Stories

In Iteration 1, our team planned five user stories for the movie recommendation system. By the end of Iteration 1, all planned user stories were completed. Therefore, there were no unfinished user stories in Iteration 1.

| User Story                  | Priority |  Effort | Status    | Comment                                                                                         |
| --------------------------- | -------: | ------: | --------- | ----------------------------------------------------------------------------------------------- |
| User Registration and Login |       50 | 10 days | Completed | Users can register and log in to access the movie recommendation system with their own account. |
| Search Movies by Tags       |       50 |  8 days | Completed | Users can search for movies by selecting tags that match their interests.                       |
| View Landing Page           |       40 | 10 days | Completed | Users can view the landing page and enter the movie recommendation system easily.               |
| Browse Movie List           |       40 | 12 days | Completed | Users can browse the movie list on the home page and view basic movie information.              |
| Search Movies by Keyword    |       50 |  5 days | Completed | Users can search for specific movies by entering keywords.                                      |

## Summary

All planned Iteration 1 user stories were completed successfully. No user stories were left unfinished.

## Actual Velocity

The actual velocity of Iteration 1 is calculated by adding the effort of all completed user stories.

| Completed User Story        |             Effort |
| --------------------------- | -----------------: |
| User Registration and Login |            10 days |
| Search Movies by Tags       |             8 days |
| View Landing Page           |            10 days |
| Browse Movie List           |            12 days |
| Search Movies by Keyword    |             5 days |
| **Actual Velocity**         | **45 person-days** |

The actual velocity of Iteration 1 is **45 person-days**.

## Actual Velocity of Iteration 1

The actual velocity of Iteration 1 is 45 person-days.

This is calculated by adding the effort of all completed user stories in Iteration 1:

| Completed User Story | Effort |
|---|---:|
| User Registration and Login | 10 days |
| Search Movies by Tags | 8 days |
| View Landing Page | 10 days |
| Browse Movie List | 12 days |
| Search Movies by Keyword | 5 days |
| **Actual Velocity** | **45 person-days** |

Since all planned Iteration 1 user stories were completed, the actual velocity is equal to the total completed effort.

## SRP and DRY Check

| Class / Component | SRP Check | DRY Check | Finding |
|---|---|---|---|
| User | Mostly satisfies SRP | Mostly satisfies DRY | The User class handles registration, login, profile update and preference tags. These functions are related to user account management. |
| Movie | Satisfies SRP | Satisfies DRY | The Movie class focuses on storing and managing movie information only. |
| Tag | Satisfies SRP | Satisfies DRY | The Tag class focuses on movie category and tag-based filtering. |
| Favourite | Satisfies SRP | Mostly satisfies DRY | The Favourite class handles saving and removing favourite movies. It should reuse user and movie validation logic. |
| RecommendationService | Needs improvement | Needs improvement | This service handles scoring, ranking and generating recommendations. It may become too complex, so the scoring logic could be separated later. |
| Administrator | Mostly satisfies SRP | Needs improvement | The Administrator class handles adding, updating and deleting movie information. Some validation logic may be repeated. |
| MovieCatalogService | Satisfies SRP | Mostly satisfies DRY | This service handles movie browsing, keyword search and tag search. Repeated search query logic should be reduced. |

Overall, most classes satisfy SRP because each class has a clear responsibility. However, RecommendationService may become too complex if all recommendation logic stays in one class. For DRY, repeated validation and database query logic should be refactored into reusable methods in future iterations.
