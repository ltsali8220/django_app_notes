from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging


posts = [
        {'id':1, 'title':'post 1', 'content':'This is the content of post 1.'},
        {'id':2, 'title':'post 2', 'content':'This is the content of post 2.'},
        {'id':3, 'title':'post 3', 'content':'This is the content of post 3.'},
        {'id':4, 'title':'post 4', 'content':'This is the content of post 4.'},
       
    ]


# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the blog index page.")
    blog_title = "Latest Posts"
        
    return render(request, 'blog\index.html', {'blog_title': blog_title, 'posts': posts})


def detail(request, post_id):
    # return HttpResponse(f"This is the detail view of a blog post. id is {post_id}.")
    post = next((post for post in posts if post['id'] == int(post_id)), None)
    # logger=logging.getLogger('TESTING')
    # logger.debug(f'post variable: {post}')
    return render(request, 'blog\detail.html', {'post': post})

def old_url_redirect(request):
    # This is an example of a view that could be used to redirect old URLs
    return redirect("new_url")

def new_url_view(request):
    # This is an example of a view that could be used for the new URL
    return HttpResponse("This is the new URL view.")
