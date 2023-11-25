
# Bitpin Task

## Installation

### Local Installation

 1. Create a new python virtual environment: 
 - ```python3 -m virtualenv venv```
 2. Install Dependencies:
  - `pip install -r requirements.txt`
 3. Create a folder named 'data'. then run:
  - `python manage.py migrate` in order for the database to get created.
 4. start up a dev server :
 - `python manage.py runserver`

## Endpoints
1- /users/: list users, create user (POST)\
2- /blogposts/ : list blog posts (GET), Create Blog Post(POST)\
3- /ratings/: paginated list of ratings (Read Only)\
4- /rate/: lets the currently logged-in user rate a post. 

## Notes
1- you can login via `/api-auth/login/` .api shows data according to currently logged in user.\
2- user creation logic is not implemented (due to lack of time.). you can create users / super users via django shell.\
3- according to task instructions, 

> there is a large amount of ratings in the db.


My assumption was that this means we should use db-level aggregation functions (count & avg) instead of selecting all rows.\
also, I implemented pagination to enhance browsing large number of database records.Not to mention using prefetch_related() to fetch all the data and do the joining in python.