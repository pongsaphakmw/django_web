from django.urls import path,include 
from .views import *


urlpatterns = [
    path('', Homepage,name='home-page'),
    path('about/', Aboutpage,name='about-page'),
    path('contact/', ContactUs,name='Contact-page'),
    path('score/', ShowScore, name='score-page'),
    path('register/', Register, name='register-page'),
    path('search/', Search,name='search-page')
]
