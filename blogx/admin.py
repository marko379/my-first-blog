# new 
from django.contrib import admin
from .models import Post    # here we import our post that we made in models, it show us how our admin page will look like 

admin.site.register (Post)  