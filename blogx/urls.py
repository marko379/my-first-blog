""" BLOGx URLS

Here we're importing Django's function path and all of our views from the blogx application. 
This pattern will tell Django that views.post_list is the right place to go if someone enters your website
at the 'http://127.0.0.1:8000/' address

"""

from django.urls import path 
from .import views 

urlpatterns = [
	path('',views.post_list,name = 'post_list'),   
]