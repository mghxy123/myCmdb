from django.shortcuts import render
from django.views.generic import View

# Create your views here.

def et(request):
    return render(request,'server/echartsExample.html')

