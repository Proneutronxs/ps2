from django.urls import path
from App.business import views

urlpatterns = [
    
    #### WEB

    path('', views.business, name="business"),

    ### APP ZETONE

    path('zetone/logIn', views.login, name="login"),

    ### RONDIN

    path('rondin/', views.rondin, name="rondin"),
    path('rondin/newsereno', views.newSereno, name="newsereno"),
    path('rondin/viewRecords', views.verRegistros, name="viewrecords"),
    path('rondin/export', views.exportRondin, name="exportRondin"),

    ### API

    path('prueba', views.consulta, name="consulta"),
    path('save/point/sereno=<str:sereno>&planta=<str:planta>&punto=<str:punto>&fecha=<str:fecha>&hora=<str:hora>', views.insert_Punto, name="insert_point"),

]