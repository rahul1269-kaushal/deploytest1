from django.http import HttpResponse
from django.shortcuts import render 


def hello(request):
    return HttpResponse("Hello Welcome to App Patform Testing Page 1")

def default_page(request):
    return render(request, "app_platform_testing/homepage.html")
