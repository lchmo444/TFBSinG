# --*-- coding: utf-8 --*--

from django.urls import path
from . import views

app_name = 'home_site'
urlpatterns = [
    #path('', views.index, name='index'),
    # new url definition
    #path('', views.form_function_2, name='form_function_2'),
    #path('home_site/', views.file_home, name='file_home'),
    #link proble ok, path a/
    path('', views.form_function, name='form_function'),
    path('human_long', views.form_function_2, name='form_function_2'),
    path('mouse_25bp', views.form_function_3, name='form_function_3'),
    path('mouse_long', views.form_function_4, name='form_function_4'),
    path('doc/', views.doc_home, name='doc_home'),
    path('contact/', views.contact_home, name='contact_home'),
]
