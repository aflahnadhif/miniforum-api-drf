# Django Rest Framework Mini-Forum API
This is a backend engine for a forum application. It provides:

1. CRUD endpoints for Forum Posts
2. CRUD endpoints for Post Comments
3. CRUD endpoint for User and Role
4. Authentication endpoint

With the condition of:

1. Only authenticated users can posts or comments
2. Only owner of those posts and comments can update or delete it
3. Admin (or superuser) can bypass ownership permission

## How To Setup

1) Copy env.template into .env and enters the appropriate values (leave it as it is for default values)
2) Run the docker compose file
```
docker-compose up -d
```
3) Or run the project using local virtual environment if docker is unavailable
```
# In the project root folder
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt

cd backend
python manage.py makemigrations
python manage.py migrate

python manage.py runserver
```
4) Create superuser for the project
```
# Inside the container terminal or inside the virtual environment
python manage.py createsuperuser
```

## API Documentation

The API documentation mainly uses Swagger with the help of a third party package named drf-yasg.

### Authentication Method

This project uses basic token authentication by adding it in the header of the request.

Add 'Authorization' key into the header with the values of 'Token [USER_TOKEN]'. The user token itself can be obtain through the login page by sending both username and password to log in ('/api/auth/login/').

To get the username and the password, user can register first by making use of the '/api/auth/user/' POST endpoint. Details and examples of both of these endpoints usage can be seen in the Swagger API documentation.

### Swagger API Documentation

The detailed documentation (including request and response details) for all endpoints can be found in the Swagger page of the site. After the project is ran, go into ('/swagger/').

### Testing Examples (Using Postman)

Please follow this steps using either CLI HTTP clients or Postman (or any other REST client like Insomnia)

For instance, you are user A who is one of the new user that discovers the forum.

1) User A views all the post and its comments on the homepage
```
curl --location 'localhost:8000/api/post/'
```

2) User A wants to see one of the post detail page
```
curl --location 'localhost:8000/api/post/3/'
```

3) User A wants to post something and decided to registers an account
```
curl --location 'localhost:8000/api/auth/user/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "AAAAAAAA",
    "first_name": "AAA",
    "last_name": "BBB",
    "email": "aaa@example.com",
    "password": "auserpassword",
    "password_confirmation": "auserpassword"
}'
```

4) User A logins and get the token
```
curl --location 'localhost:8000/api/auth/login/' \
--header 'Content-Type: application/json' \
--data '{
    "username": "AAAAAAAA",
    "password": "auserpassword"
}'
```

5) User A creates a new post by using the obtained token
```
curl --location 'localhost:8000/api/post/' \
--header 'Authorization: Token user_a_token_obtained_from_step_4' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Hello, this is my first post by user A"
}'
````

6)  User A wants to comment on a post
```
curl --location 'localhost:8000/api/comment/' \
--header 'Authorization: Token user_a_token_obtained_from_step_4' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Hello, this is a comment by user A",
    "post": 4
}'
```

7) User A wants to edit his/her own post
```
curl --location --request PUT 'localhost:8000/api/post/6/' \
--header 'Authorization: Token user_a_token_obtained_from_step_4' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Hello, this is an edited post by user A"
}'
```

8) User A wants to see his/her profile details
```
curl --location 'localhost:8000/api/auth/user/5/' \
--header 'Authorization: Token user_a_token_obtained_from_step_4'
```

9) User A wants to update his/her own profile
```
curl --location --request PUT 'localhost:8000/api/auth/user/3/' \
--header 'Authorization: Token user_a_token_obtained_from_step_4' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "ausername",
    "first_name": "afirstname",
    "last_name": "alastname",
    "email": "aemail@example.com"
}'
```