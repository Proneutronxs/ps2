from django.urls import path
from App.business import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #### WEB

    path('', views.index, name="index"),
    path('zetone/', views.business, name="business"),
    
    

    ### ZETONE

    ### EMPAQUE
    path('zetone/empaque/', views.empaque, name="empaque"),


    ### RONDIN

    path('zetone/empaque/rondin/', views.rondin, name="rondin"),
    path('zetone/empaque/rondin/newsereno', views.newSereno, name="newsereno"),
    path('zetone/empaque/rondin/viewRecords', views.verRegistros, name="viewrecords"),
    path('zetone/empaque/rondin/export', views.exportRondin, name="exportRondin"),

    ### API

    path('prueba', views.consulta, name="consulta"),
    path('save/point/sereno=<str:sereno>&planta=<str:planta>&punto=<str:punto>&fecha=<str:fecha>&hora=<str:hora>', views.insert_Punto, name="insert_point"),

]