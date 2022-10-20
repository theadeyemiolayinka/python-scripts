# URL SHORTENER

###### It takes any URL as an input from user and if user prefers, one can also provide a custom short URL otherwise a random short URL will be generated(using shortuuid package).

## Technology Stack:
### Backend
* #### Django(Python3)
###### Django is used here because of it's powerful underlying code that makes it very convenient to use and focus on logic rather than boilerplate code and also because of Python's ease of use.

### Frontend
* #### HTML/CSS
* #### JavaScript
* #### Bootstrap
  ###### It is a frontend framework which makes it is easier to design elements in HTML without worrying much about CSS(Bootstrap uses it's own CSS, JS, jQuery). Easy to use and saves a lot of time when creating basic/minimal frontend

### Database
* #### SQLite
  ###### It is used(which comes bundled with Django). This is only used for development purpose and a more powerful datatbase should be used in production.

## How to Use?
* Create a python3 virtual environment, navigate to project directory on terminal and install dependencies(listed in requirements.txt file) using the command
`pip install requirements.txt` <br>
RUN `python manage.py makemigrations` and `python manage.py migrate` <br>to create tables in database. <br>
To run server, use command `python manage.py runserver`

* Open a browser and navigate to <b>localhost:8000</b> to use the website.
