<h1>Requirements</h1>
The specifications was taken from https://shawandpartners.com/full-back-front-test/.

<h1>1 - [full-stack] [back-end]</h1>
Create an API that will proxy all client requests to the appropriate GitHub endpoint. The following endpoints must be provided:

GET - /api/users?since={number} This endpoint must return a list of GitHub users and the link for the next page.

GET - /api/users/:username/details This endpoint must return the details of a GitHub user

GET - /api/users/:username/repos This endpoint must return a list with all user repositories

<h1>2 - [full-stack (optional)] [back-end]</h1>
Create tests for your application covering all endpoints.

<h1>Endpoints</h1>
The endpoints that proxy the GitHub API (replace the params enclosed in {:param}):

GET - http://localhost:3000/api/users?since={:number} This endpoint must return a list of GitHub users and the link for the next page.

GET - http://localhost:3000/api/users/{:username}/details This endpoint must return the details of a GitHub user

GET - http://localhost:3000/api/users/{:username}/repos This endpoint must return a list with all user repositories

<h1>This project was generated with Django framework.</h1>

<h1>Dependencies</h1>
Check if you have a recent version of Django:
django-admin --version

<h1>Installation</h1>
pip install Django 

<h1>Running the app</h1>
python manage.py runserver

<h1>Test</h1>
python manage.py test

<h1>In live</h1>
https://web-production-7ba1.up.railway.app
