from django.shortcuts import render
import os

# Create your views here.
ENROLLED_DATA = 'static/enrolled_data'

def door_page(request):
    return render(request, 'mainapp/home.html')

def cody_page(request):
    return render(request, 'mainapp/cody.html')

def cody_result(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        print(type(age))
        gender = request.POST.get('gender')
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        majorcategories = request.POST.get('majorcategories')
        subcategories = request.POST.get('subcategories')
        return render(request, 'mainapp/cody/result.html', context={'age': age, 'gender': gender, 'height': height, 'weight': weight, 'majorcategories': majorcategories, 'subcategories': subcategories})
    else:
        return render(request, 'mainapp/cody/result.html', context={'age': 'age'})

def reco_page(request):
    if request.method == "POST":
        if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest' :  #   ajax  
            if not os.path.exists(ENROLLED_DATA): #  settings            
                os.makedirs(ENROLLED_DATA,exist_ok=True) #     
            for k,file_obj in request.FILES.items(): #            
                with open('%s/%s'%(ENROLLED_DATA,file_obj.name),"wb") as f: #    
                    for chunk in file_obj.chunks():   
                        f.write(chunk)  #chunk      
    return render(request, 'mainapp/reco.html')