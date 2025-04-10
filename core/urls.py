from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('deslikes', views.deslikes, name='home'),
    path('atualizar-mico/<int:deslike_id>/', views.atualizar_mico, name='atualizar_mico'),
]