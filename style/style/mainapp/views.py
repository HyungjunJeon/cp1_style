from django.shortcuts import render
import os
import psycopg2

#아래 정보를 입력
user = 'fuusaujh'
password = 'KPbDgG1NtOXKVcU_rstsh0xMTFDChg0J'
host_product = 'jelani.db.elephantsql.com'
dbname = '	fuusaujh'
port='5432'

product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}"\
                            .format(dbname=dbname,
                                    user=user,
                                    host=host_product,
                                    password=password,
                                    port=port)    
try:
    conn = psycopg2.connect(product_connection_string)
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

# Create your views here.
ENROLLED_DATA = 'static/enrolled_data'

def door_page(request):
    return render(request, 'mainapp/home.html')

def cody_page(request):
    if request.method == 'POST':
        age = int(request.POST.get('age'))
        gender = request.POST.get('gender')
        height = float(request.POST.get('height'))
        weight = float(request.POST.get('weight'))
        majorcategories = request.POST.get('majorcategories')
        subcategories = request.POST.get('subcategories')
        cur.execute("""
            INSERT INTO mainapp_information_user VALUES(%s, %s, %s, %s, %s, %s)
        """,(gender, age, height, weight, majorcategories, subcategories))
        conn.commit()
        cur.close()
        return render(request, 'mainapp/cody.html', context={'age': age, 'gender': gender, 'height': height, 'weight': weight, 'majorcategories': majorcategories, 'subcategories': subcategories})
    else:
        return render(request, 'mainapp/cody.html', context={'age': 'age'})

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

def review_page(request):
    gender = request.POST.get('gender')
    recommend = request.POST.get('exampleRadios')
    what = request.POST.get('exampleRadios1')
    cur.execute("""
        INSERT INTO mainapp_review_user VALUES( %s, %s, %s)
    """, (gender, recommend, what))
    conn.commit()
    cur.close()
    return render(request, 'mainapp/review.html')