from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse("Hey i am django server!!")

def success_page(request):
    return HttpResponse("Hey this is sucess_page!")