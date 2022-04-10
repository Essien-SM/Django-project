from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'Essien',
    'title': 'Blog Post 1',
    'content': 'First post content',
    'date_posted': 'April 24, 2022'
    },
    {
    'author': 'Stephen',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'April 25, 2022'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
    