from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('doctors/', views.doctors, name='doctors'),
    path('patients/', views.patients, name='patients'),
    path('appointments/', views.appointments, name='appointments'),
]
