from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

    #HttpResponse("<h1 align='center' style='font-family:sans-serif;color:darkslategray'>Hello, Python DjANGO III World!!!</h1>")

def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('numbers'):
        characters.extend(list('012345678901234567890123456789'))

    if request.GET.get('specialchars'):
        characters.extend(list('!@#$%^&*()!@#$%^&*()!@#$%^&*()'))

    length = int(request.GET.get('length',12))

    the_password = ''

    for x in range(length):
            the_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password':the_password})

def about(request):

    return render(request, 'generator/about.html')
