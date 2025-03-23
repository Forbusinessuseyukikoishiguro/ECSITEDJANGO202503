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
    
    return render(request, 'TemplateApp/home.html', 
                 context={'my_name': my_name, 'favorite_fruit': favorite_fruit, 'my_info': my_info})
