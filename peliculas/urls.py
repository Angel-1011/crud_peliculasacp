#urls.py (peliculas)

from django.urls import path
from peliculas import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.pelicula_list, name='pelicula_list'),
    path('new/', views.create_pelicula, name='create_pelicula'),
    path('edit/<int:pk>/', views.update_pelicula, name='update_pelicula'),
    path('delete/<int:pk>/', views.delete_pelicula, name='delete_pelicula'),
    path('pdf/', views.generar_pdf, name='generar_pdf'),

    #Rutas para login
    path('login/', auth_views.LoginView.as_view(), name= 'login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.registro, name='registro'),
]