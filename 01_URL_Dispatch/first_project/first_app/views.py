from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Good Bye</h1>')

def user_page(request, user_name):
    prin(type(user_name),user_name)
    return HttpResponse(f'<h1>{user_name}Page</h1>')

def number_page(request,user_name, number):
    # 受け取ったnumberパラメータの型と値をコンソールに出力（デバッグ用）
    print(type(number), number)
    
    # ブラウザに表示するHTMLレスポンスを返す
    return HttpResponse(f'<h1>{user_name}page Number: {number}</h1>')