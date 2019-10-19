from django.db import models                           #	MODELS IN BLOGX
from django.conf import settings
from django.utils import timezone 

class Post(models.Model):  # post is name of our  model , models.Model means that the Post is a Django Model
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	title = models.CharField(max_length = 200)                                                                                                                               # PROPERTIES 
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True , null = True)
	
	
	def publish(self):    # METHODS,  IT RETURNS DATE 
		self.published_date = timezone.now()
		self.save()
		
	def __str__(self): # IT RETURNS TITLE to be visible on post page 
		return self.title
		
	
#Methods often return something. There is an example of that in the __str__ method. In this scenario, 
#when we call __str__() we will get a text (string) with a Post title.