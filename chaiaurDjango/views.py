from django.http import HttpResponse
from django.shortcuts import render

 
def home(request):
    #return HttpResponse("Hello, World! You are at the chaiaurDjango home page.")
    return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello, World! You are at the chaiaurDjango about page.")
    
def contact(request):
    return HttpResponse("Hello, World! You are at the chaiaurDjango contact page.")

# def home(request):
#     return HttpResponse("Hello, World! You are at the chaiaurDjango home page.")