# --*-- coding: utf-8 --*--

from django.urls import path
from . import views

app_name = 'home_site'
urlpatterns = [
    #path('', views.index, name='index'),
    # new url definition
    path('', views.form_function, name='form_function'),
    #link proble ok
    path('home_site/', views.doc_home, name='doc_home'),
    path('home_site/', views.file_home, name='file_home'),
]
