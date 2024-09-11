from django.http import HttpResponse
from django.shortcuts import render

 
def home(request):
    # return HttpResponse("Hello, World! You are at the chaiaurDjango home page.")
    return render(request, 'website/index.html')

def about(request):
    # return HttpResponse("Hello, World! You are at the chaiaurDjango about page.")
    return render(request, 'website/about.html')
    
def contact(request):
    # return HttpResponse("Hello, World! You are at the chaiaurDjango contact page.")
    return render(request, 'website/contact.html')

# def home(request):
#     return HttpResponse("Hello, World! You are at the chaiaurDjango home page.")