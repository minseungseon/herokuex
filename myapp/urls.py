from django.contrib import admin
from django.urls import path
import myapp.views
#or from .import views
#. 은 현재 폴더를 의미함 

urlpatterns = [
    path('',myapp.views.home, name="home"),
    path('profile/',myapp.views.profile, name="profile"),
   
]