from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about_author_page, name='about_author'),
    path('rules/', views.password_rules_page, name='password_rules'),
]
