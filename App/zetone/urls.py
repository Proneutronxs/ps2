from django.urls import path
from App.zetone import views

urlpatterns = [

### sólo renderizado
path('', views.index, name="index_zetone"),
path('pears', views.pear, name="pear"),
path('apple', views.apple, name="apple"),

path('fecha', views.mandarFecha, name="fecha"),

##PERA

path('pears/lote', views.consultaLotesPera, name="lotes_pera"),
path('pears/proceso', views.procesoPera, name="proceso_pera"),
path('pears/cantidad/lotes', views.cantBinsPera, name="cantidad_pera"),
path('pears/cajas/calidad', views.consultaCajasCalidad, name="cajas_calidad_pera"),
path('pears/cajas/calibre', views.consultaCajasCalibre, name="cajas_calibre_pera"),
path('pears/cajas/marca', views.consultaCajasMarca, name="cajas_calidad_pera"),
path('pears/cajas/envase', views.consultaCajasEnvase, name="cajas_calidad_pera"),

path('pears/cantidad/embalado', views.cantCajas, name="cajas_cantidad_pera"),

##MANZANA

path('apple/lote', views.consultaLotesManzana, name="lotes_manzana"),
path('apple/proceso', views.procesoManzana, name="proceso_manzana"),
path('apple/cantidad/lotes', views.cantBinsManzana, name="cantidad_pera"),
path('apple/cajas/calidad', views.consultaCajasCalidadManzana, name="cajas_calidad_manzana"),
path('apple/cajas/calibre', views.consultaCajasCalibreManzana, name="cajas_calibre_manzana"),
path('apple/cajas/marca', views.consultaCajasMarcaManzana, name="cajas_calidad_manzana"),
path('apple/cajas/envase', views.consultaCajasEnvaseManzana, name="cajas_calidad_manzana"),

path('apple/cantidad/embalado', views.cantCajasManzana, name="cajas_cantidad_manzana"),


]