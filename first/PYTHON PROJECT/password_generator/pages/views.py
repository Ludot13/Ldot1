from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def homepage(request):
    return render(request, 'pages/homepage.html')

def about_author_page(request):
    return render(request, 'pages/about_author.html')

def password_rules_page(request):
    return render(request, 'pages/password_rules.html')
