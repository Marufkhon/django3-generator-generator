from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    character = list('')
    if request.GET.get('littleword'):
        character.extend(list('qwertyuioplkjhgfdsazxcvbnm'))

    if request.GET.get('Uppercase'):
        character.extend(list('ABSEDFGRTWQTYUIOPLMKJNHBGVFCXZ'))
    if request.GET.get('Special'):
        character.extend(list('!@#$%^&*()'))
    if request.GET.get('Numbers'):
        character.extend(list('1234567890'))

    length = int(request.GET.get('length'))
    thepassword = ''

    for x in range(length):
        thepassword += random.choice(character)

    return render(request, 'generator/password.html', {'password': thepassword})


def creator(request):
    return render(request, 'generator1/creator.html')
