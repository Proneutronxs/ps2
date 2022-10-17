from django.urls import path
from App.ps import views

urlpatterns = [
    path('', views.index, name="indexps"),
    path('project', views.project, name="project"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('api', views.consumoApi, name="consumoApi"),
    path('about', views.about1, name="about"),
    path('contact', views.contact, name="contact"),


    #Prueba Rondin
    path('search', views.sqlQuery, name="search"),
]