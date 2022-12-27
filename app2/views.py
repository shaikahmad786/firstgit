from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rose(request):
    return HttpResponse('rose is beautiful')