from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    context={'home_res':'HOME_RES'}
    return render(request, 'app1/home.html', context)
