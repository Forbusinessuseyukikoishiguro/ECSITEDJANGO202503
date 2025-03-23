from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#足し算

def add(request, num1, num2):
    return HttpResponse(f'<h1>Sum: {num1} + {num2} = {num1 + num2}</h1>')


#引き算
def minus(request, num1, num2):
    return HttpResponse(f'<h1>{float(num1)-float(num2)}</h1>')

#割り算
def div(request, num1, num2):
    float_num1 = float(num1)
    float_num2 = float(num2)
    #四捨五入
    return HttpResponse(f'<h1>{round(float(num1)/float(num2))}</h1>')