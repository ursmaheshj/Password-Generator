from django.shortcuts import render
from django.http import HttpResponse
import random
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')
    
def password(request):
    password=''
    char=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('numbers'):
        char.extend(list('0123456789'))
    if request.GET.get('uppercase'):
        char.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specials'):
        char.extend(list('!@#$%^&*'))
    len=int(request.GET.get('length'))
    for i in range(len):
        password+=random.choice(char)
    return render(request, 'generator/home.html',{'pass':password})