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

    #PS APP ZETONE
    path('permiso/app', views.permisoZetone, name="permisos_app"),
    path('permiso/app/actualizacion/estado=<str:estado>/detalle=<str:detalle>', views.actualizacionEstado, name="actualizacion_estado"),
    path('estado', views.estado, name="estado"),

    path('upload-apk/', views.subirApk, name="subir_apk"),

    path('upload-apk/apk/', views.recibir_apk, name='recibir_apk'),

    path('download-apk/', views.descargar_apk, name='descargar_apk'),

    path('obtener-version/', views.obtenerVersion, name='obtener_version'),

]