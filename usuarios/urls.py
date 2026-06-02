from django.urls import path
from . import views

urlpatterns = [

    path('', views.agregar_view, name='agregar'),

    path('alumnos/', views.alumnos_view, name='alumnos'),

    path('agregar/', views.agregar_view, name='agregar'),

    path('subir/', views.subir_view, name='subir'),

    path('login/', views.login_view, name= 'login'),

]