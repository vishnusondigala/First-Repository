from . import views
from django.urls import path
urlpatterns = [
    
    path('Serviceelist/', views.ListServicee),
     path('createservice/',views.createservice),
   
]