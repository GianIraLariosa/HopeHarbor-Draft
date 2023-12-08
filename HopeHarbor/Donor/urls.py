from django.urls import path
from . import views

app_name = 'donor'

urlpatterns = [
    path('login/', views.donor_entry_request, name='login'),
    path('register/', views.registration, name='register'),
    path('', views.index, name='index'),
    path('DiKpage/', views.DiK, name='DiK'),
]