'''The dot before models means current directory or current application. 
Both views.py and models.py are in the same directory'''

from django.shortcuts import render
from .models import Post 
from django.utils import timezone 
from django.shortcuts import render, get_object_or_404




def  post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date') #posts. posts. Treat this as the name of our QuerySet. 
	return render (request,'blogx/post_list.html',{'posts': posts})
	
	
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blogx/post_detail.html', {'post': post})
	

'''As you can see, we created a function (def) called post_list that takes request and will return the value it gets from 
calling another function render that will render (put together) our template blog/post_list.html.'''

'''The last parameter, {}, is a place in which we can add some things for the template to use.
 We need to give them names (we will stick to 'posts' right now). :) It should look like this: {'posts': posts}. 
 Please note that the part before : is a string; you need to wrap it with quotes: '''