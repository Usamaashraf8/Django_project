from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    people = [
        {'name' : 'Usama', 'age':24},
        {'name' : 'Hamza', 'age':25},
        {'name' : 'Safwan', 'age':15},
        {'name' : 'Fezan', 'age':23},
    ]
    for p in people:
        print (p)
    
    return render(request, "home/index.html", context={'people': people})

def about(request):
    return render(request, "home/about.html")
def contact(request):
    return render(request, "home/contact.html")
def success_page(request):
    return HttpResponse("Hey this is sucess_page!")