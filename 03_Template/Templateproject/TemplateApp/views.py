from django.shortcuts import render

# Create your views here.
def index( request ):
    return render( request, 'TemplateApp/index.html', context ={"value":"Hello"} )
