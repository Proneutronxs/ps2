from django.urls import path
from App.business import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #### WEB

    path('', views.index, name="index"),
    path('zetone/', views.business, name="business"),
    
    

    ### ADMINISTRACIÓN
    path('zetone/administracion/', views.administracion, name="administracion"),

    ### CALIDAD
    path('zetone/calidad/', views.calidad, name="calidad"),

    ### CARGAS
    path('zetone/cargas/', views.cargas, name="cargas"),

    ### EMPAQUE
    path('zetone/empaque/', views.empaque, name="empaque"),


    ### RONDIN

    path('zetone/empaque/rondin/', views.rondin, name="rondin"),
    path('zetone/empaque/rondin/newsereno', views.newSereno, name="newsereno"),
    path('zetone/empaque/rondin/viewRecords', views.verRegistros, name="viewrecords"),
    path('zetone/empaque/rondin/export', views.exportRondin, name="exportRondin"),


    ### DEPÓSITO
    path('zetone/deposito/', views.deposito, name="deposito"),

    ### CHACRAS
    path('zetone/chacras/', views.chacras, name="chacras"),

    ### SISTEMAS
    path('zetone/sistemas/', views.sistemas, name="sistemas"),

    ### API

    path('prueba', views.consulta, name="consulta"),
    path('save/point/sereno=<str:sereno>&planta=<str:planta>&punto=<str:punto>&fecha=<str:fecha>&hora=<str:hora>', views.insert_Punto, name="insert_point"),

]