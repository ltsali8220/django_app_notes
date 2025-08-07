from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    #return HttpResponse("Welcome to the blog index page.")
    return render(request, 'blog\index.html')


def detail(request, post_id):
    # return HttpResponse(f"This is the detail view of a blog post. id is {post_id}.")
    return render(request, 'blog\detail.html')

def old_url_redirect(request):
    # This is an example of a view that could be used to redirect old URLs
    return redirect("new_url")

def new_url_view(request):
    # This is an example of a view that could be used for the new URL
    return HttpResponse("This is the new URL view.")
