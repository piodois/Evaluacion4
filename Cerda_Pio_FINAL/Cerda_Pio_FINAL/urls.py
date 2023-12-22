from django.contrib import admin
from django.urls import path
from Cerda_Pio_FINAL_app import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.estudiante_list_render, name='index'),  # Ruta base para mostrar el index.html
    path('estudiante/', views.estudiante_list_render, name='estudiante_list'),
    path('estudiante_detalle/<int:id>/', views.estudiante_detalle_render, name='estudiante_detalle'),
    path('estudiante_class/', views.EstudianteListClass.as_view(), name='Estudiante_list_class'),
]