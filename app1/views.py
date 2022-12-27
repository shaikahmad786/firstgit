from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inthiyaz(request):
    return HttpResponse('inthiyaz is good boy')

def taj(request):
    return HttpResponse('taj is good girl')