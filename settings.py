# Configure Django App for Heroku.
import django_heroku
import os

django_heroku.settings(locals(), staticfiles="orders/static")
