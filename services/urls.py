from . import views
from django.urls import path
urlpatterns = [
    
    path('Serviceelist/', views.ListServicee,name="Serviceelist"),
    path('createservice/',views.createservice,name="createservice"),
    path('deleteservice/<int:id>',views.deleteservice,name="deleteservice"),
    path("updateservice/<int:id>",views.updateservice,name="updateservice")
]