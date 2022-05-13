from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name='showmain'),
    path('show/',show, name="introduce"),
    path('Gangneung/',showgang, name="showgang"),
    path('<str:id>',detail, name='detail'),
    path('new/',new, name="new"),
    path('create/',create, name='create'),
    path('edit/<str:id>',edit, name="edit"),
    path('update/<str:id>', update, name="update"),

]