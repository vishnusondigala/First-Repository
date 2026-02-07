from django.http import HttpResponse
from django.shortcuts import render

#specifi url
def test(request):
    return HttpResponse("Hello")

# def AboutUs(request):
#     return HttpResponse("About")

def AboutUs(request):
    return render(request,"aboutus.html")

def contactUs(request):
    return render(request,"contactus.html")

def home(request):
    return render(request,"home.html")

def reacp(request):
    return render(request,"reacp.html")

def recipe(request):
    ingredient = ["maggie","tomato"]
    data = {"name":"maggie","time":20,"ingredient":ingredient} 
    return render(request,"recipe.html",data)

def teams(request):
    teams = [
        {"name": "Mumbai Indians", "trophy": 5},
        {"name": "chennai super kings", "trophy": 5},
        {"name": "royal challengers bangalore", "trophy": 0},
        {"name": "kolkata knight riders", "trophy": 3},
    ]
    return render(request,"teams.html", {"teams": teams})

