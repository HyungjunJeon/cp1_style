from django.shortcuts import render

# Create your views here.

def door_page(request):
    return render(request, 'mainapp/home.html')

def cody_page(request):
    return render(request, 'mainapp/cody.html')

def cody_result(request):
    if request.method == 'post':
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        return render(request, 'mainapp/cody/result.html', context={'age': age, 'gender': gender, 'height': height, 'weight': weight})
    else:
        return render(request, 'mainapp/cody/result.html', context={'age': 'age'})