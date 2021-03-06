from django.urls import path
from .views import *

app_name = "main"
urlpatterns = [
    path('', showmain, name='showmain'),
    path('show/',show, name="introduce"),
    path('Gangneung/',showgang, name="showgang"),
    path('<int:id>',detail, name='detail'),
    path('new/',new, name="new"),
    path('create/',create, name='create'),
    path('edit/<int:id>',edit, name="edit"),
    path('update/<int:id>', update, name="update"),
    path('delete/<int:id>', delete, name="delete"),

]