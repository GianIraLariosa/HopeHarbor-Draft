from django.urls import path
from . import views

app_name = 'donor'

urlpatterns = [
    path('login/', views.donor_entry_request, name='login'),
    path('register/', views.registration, name='register'),
    path('DiK', views.DiK.as_view(), name='DiK'),
    path('goods', views.InsertGoods.as_view(), name='goods'),
    path('goodstracker', views.displayGoodsTracker.as_view(), name='goodstracker')
]