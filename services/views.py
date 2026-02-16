from django.shortcuts import render,HttpResponse,redirect
from .models import Servicee
from .forms import serviceForm

# Create your views here.

def ListServicee(request):
    Servicee_list= Servicee.objects.all().order_by("id").values()
    print(Servicee_list)
    return render(request, 'services/Serviceelist.html',{"Servicee_list":Servicee_list})


#---------------------create service from-----------------------------------------------------

def createservice(request):
    if request.method == "POST":
        form = serviceForm(request.POST) 
        form.save() 
        return HttpResponse("SERVICES CREATED...")
    else:
        form = serviceForm()
        return render(request,"services/createservice.html",{"form":form})   
    


def deleteservice(request,id):
    
    print("id from url = ",id)
    Servicee.objects.filter(id=id).delete()
    
    return redirect("Serviceelist") 


def updateservice(request,id):
   
    Servicee_list = Servicee.objects.get(id=id) 
    if request.method == "POST":
        form = serviceForm(request.POST,instance=Servicee_list)
        form.save()
        return redirect("Serviceelist")
    else:
        form = serviceForm(instance=Servicee_list)    
        return render(request,"services/updateservice.html",{"form":form})
    