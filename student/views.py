from django.shortcuts import render,redirect
from .models import Service
from .forms import ServiceForm

# Create your views here.

def StudentHome(request):
    student={"Name":"Vishnu","Age":"20","City":"Ahmedabad"}
    return render(request,"student/StudentHome.html",student)


def serviceList(request):
    services = Service.objects.all()
    return render(request,"student/serviceList.html",{"services":services})

def createService(request):

    if request.method =="POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("serviceList")
        else:
            return render(request,"student/createService.html",{"form":form})    
    else:
        form = ServiceForm()
        return render(request,"student/createService.html",{"form":form})
    

def deleteService(request, id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect("serviceList")


