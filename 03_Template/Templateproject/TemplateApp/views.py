from django.shortcuts import render

# Create your views here.
def index( request ):
    value = "Good Morning"
    return render( request, 'TemplateApp/index.html', context ={"value":value} )


#home関数を作る

def home(request):
    my_name = 'Yukiko Ishiguro'
    favorite_fruit = ['Apple', 'Banana', 'Orange']
    my_info = {'name': 'Yukiko Ishiguro', 'age': 25}
    
    
    status = 20
    
    return render(request, 'TemplateApp/home.html', 
                 context={'my_name': my_name, 'favorite_fruit': favorite_fruit, 'my_info': my_info, 'status': status})


#sample1関数を作る
def sample1(request):
    return render(request, 'TemplateApp/sample1.html')


#sample2関数を作る
def sample1(request):
    return render(request, 'TemplateApp/sample2.html')


#テンプレートフィルターの練習　sample関数を作る
def sample(request):
    name = 'Ichiro Yamada'
    height = 175.5
    weight = 72
    bmi = weight / (height / 100) ** 2  
    page_url = 'https://www.google.com/'
    favorite_fruits = ['Apple', 'Grape', 'Lemon'] 
    msg = """Hello, 
    I'm Ichiro
    Yamada.""" 
    msg2 = '12134567890'
    
   
    return render(request, 'TemplateApp/sample.html', context={
        'name': name,
        'bmi': bmi,
        'page_url': page_url,
        'favorite_fruits': favorite_fruits,
        'msg': msg,
        'msg2': msg2
    })