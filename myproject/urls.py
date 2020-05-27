
from django.contrib import admin
from django.urls import path, include
import myapp.views
import portfolio.views
import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('myphoto/',portfolio.views.myphoto, name="myphoto"),
    path('blog/<int:blog_id>', myapp.views.detail, name ="detail"), #detail.html 관련된 url #path converter : path('url 이름', 함수이름, path이름)
    path('new/', myapp.views.new, name="new"),
    path('create/', myapp.views.create, name="create"),
    path('blog/edit/<int:blog_id>', myapp.views.edit, name="edit"),
    path('blog/update/<int:blog_id>', myapp.views.update, name="update"),
    path('blog/delete/<int:blog_id>', myapp.views.delete, name="delete"),

    path('blog/detail/<int:pk>', myapp.views.read_blog_one, name="read_blog_one"),

     path('signup/', accounts.views.signup, name='signup'),
    ]
