from django.shortcuts import render, redirect, get_object_or_404
from .models import Myapp
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
# request가 들어왔을 때, home이라는 html을 갔다줘! :
def home(request):
    blogs = Myapp.objects.all()
    paginator = Paginator(blogs,5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'home.html', {'posts':posts})

def profile(request):
    return render(request, 'profile.html')

def detail(request, blog_id):
    blog = get_object_or_404(Myapp, pk = blog_id)
    return render(request, 'detail.html', {'blogs':blog})            

def new(request):
    return render(request, 'new.html')     

def create(request):
    blog = Myapp()
    blog.title = request.GET['title']
    blog.body = request.GET['body']      
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리 메소드
    return redirect('home')                 

def edit(request, blog_id):
    blog = get_object_or_404(Myapp, pk= blog_id)
    return render(request, 'edit.html', {'blog': blog})

def update(request, blog_id):
    blog = get_object_or_404(Myapp, pk= blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']      
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리 메소드
    return redirect('home')   

def delete(request, blog_id):
    blog = get_object_or_404(Myapp, pk = blog_id)
    blog.delete()
    return redirect('home')

def read_blog_one(request, pk):
    blog= Myapp.objects.get(pk=pk)
    return render(request, 'detail.html', {'blogs':blog})