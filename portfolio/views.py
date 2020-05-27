from django.shortcuts import render

# Create your views here.
def myphoto(request):
    return render(request, 'myphoto.html')