from django.shortcuts import render,HttpResponse
from .models import Servicee
from .forms import serviceForm

# Create your views here.

def ListServicee(request):
    Servicee_list= Servicee.objects.all().values()
    print(Servicee_list)
    return render(request, 'services/Serviceelist.html',{"Servicee_list":Servicee_list})


#---------------------create service from-----------------------------------------------------

def createservice(request):
    if request.method == "POST":
        form = serviceForm(request.POST) 
        form.save() 
        return HttpResponse("service CREATED...")
    else:
        form = serviceForm()
        return render(request,"services/createservice.html",{"form":form})   