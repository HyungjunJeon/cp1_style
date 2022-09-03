from django.shortcuts import render,HttpResponse

# Create your views here.

def door_page(request):
    return render(request, 'mainapp/home.html')
