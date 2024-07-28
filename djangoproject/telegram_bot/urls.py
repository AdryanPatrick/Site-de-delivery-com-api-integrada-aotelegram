
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('produto/<str:nome>/', views.produto_detalhe, name='produto_detalhe'),
    path('send_command', views.send_command, name='send_command'),
]
