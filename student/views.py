from django.shortcuts import render

# Create your views here.

def StudentHome(request):
    student={"Name":"Vishnu","Age":"20","City":"Ahmedabad"}
    return render(request,"student/StudentHome.html",student)
