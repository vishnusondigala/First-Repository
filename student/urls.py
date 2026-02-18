from django.urls import path
from . import views

urlpatterns = [
    path("StudentHome/", views.StudentHome, name="StudentHome"),
    path("serviceList/", views.serviceList, name="serviceList"),
    path("createService/", views.createService, name="createService"),
]
