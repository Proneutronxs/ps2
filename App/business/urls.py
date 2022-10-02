from django.urls import path
from App.business import views
from django.contrib.auth.views import LogoutView

from App.business.vistas.vistaSistemas import viewsSistemas
from App.business.vistas.vistaEmpaque import viewsEmpaque
from App.business.vistas.vistaAdministracion import viewsAdministracion
from App.business.vistas.vistaCargas import viewsCargas
from App.business.vistas.vistaCalidad import viewsCalidad
from App.business.vistas.vistaDeposito import viewsDeposito
from App.business.vistas.vistaChacras import viewsChacras

    #### WEB
urlpatterns = [
    path('', views.index, name="index"),
    path('zetone/', views.business, name="business"),
    
    

    ### ADMINISTRACIÓN
    path('zetone/administracion/', viewsAdministracion.administracion, name="administracion"),

    ### CALIDAD
    path('zetone/calidad/', viewsCalidad.calidad, name="calidad"),

    ### CARGAS
    path('zetone/cargas/', viewsCargas.cargas, name="cargas"),

    ### EMPAQUE
    path('zetone/empaque/', viewsEmpaque.empaque, name="empaque"),


    ### RONDIN

    path('zetone/empaque/rondin/', viewsEmpaque.rondin, name="rondin"),
    path('zetone/empaque/rondin/newsereno', viewsEmpaque.newSereno, name="newsereno"),
    path('zetone/empaque/rondin/viewRecords', viewsEmpaque.verRegistros, name="viewrecords"),
    path('zetone/empaque/rondin/export', viewsEmpaque.exportRondin, name="exportRondin"),


    ### DEPÓSITO
    path('zetone/deposito/', viewsDeposito.deposito, name="deposito"),

    ### CHACRAS
    path('zetone/chacras/', viewsChacras.chacras, name="chacras"),

    ### SISTEMAS
    path('zetone/sistemas/', viewsSistemas.sistemas, name="sistemas"),

    
    
    ### API

    path('prueba', views.consulta, name="consulta"),
    path('save/point/sereno=<str:sereno>&planta=<str:planta>&punto=<str:punto>&fecha=<str:fecha>&hora=<str:hora>', views.insert_Punto, name="insert_point"),

]