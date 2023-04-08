from django.urls import path
from App.vikosur import views

urlpatterns = [
    ##/save/client/nombre=ZETONE&ciudad=ROCA&provincia=NEGRO&direccion=PUERTORICO&cuit=CUIT&telefono=2948657019
    path('save/client/nombre=<str:nombre>&ciudad=<str:ciudad>&provincia=<str:provincia>&direccion=<str:direccion>&cuit=<str:cuit>&telefono=<str:telefono>', views.insert_Cliente, name="insert_client"),
    path('listado/clientes', views.listado_Clientes, name="list_client"),
    path('save/remito/idCliente=<str:idCliente>&fecha=<str:fecha>', views.insert_Remito, name="insert_remito"),
    path('maximo/id', views.max_ID, name="max_id"),
    path('save/data/remito/idRemito=<str:idRemito>&cantidad=<str:cantidad>&descripcion=<str:descripcion>&precio=<str:precio>', views.insert_Data_Remito, name="data_remito"),
    path('download/remito/<str:idRemito>', views.download_remito, name="download_remito"),

    ####FLUTTER URLS
    path('listado/clientes/json', views.listado_Clientes_json, name="list_client_json"),
    path('data/cliente/json/id=<str:id>', views.data_Clientes_json, name="data_client_json"),

    

]