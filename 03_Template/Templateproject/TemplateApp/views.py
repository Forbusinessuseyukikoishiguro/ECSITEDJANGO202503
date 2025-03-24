from django.shortcuts import render

# Create your views here.
def index( request ):
    value = "Good Morning"
    return render( request, 'TemplateApp/index.html', context ={"value":value} )


#home関数を作る

def home(request, first_name, last_name):
    my_name = f'{first_name} {last_name}'
  
    favorite_fruit = ['Apple', 'Banana', 'Orange']
    my_info = {'name': first_name, 'age': 25}
    
    
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
    
    

# クラスを作る
class Country:
    def __init__(self, name, population, capital):
        self.name = name
        self.population = population
        self.capital = capital  # 引数はcapitalですが、attributeはareaになっています。修正しました


    def __str__(self):
        return f'{self.name} {self.population} {self.capital}'

    def capital_and_population(self):
        return f'capital: {self.capital},population:{self.population}'


# sample3関数を作る
def sample3(request):
    country = Country('Japan', 126800000, 'Tokyo')
    return render(request, 'TemplateApp/sample3.html', context={
        'country': country
    })