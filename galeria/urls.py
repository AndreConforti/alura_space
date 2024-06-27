from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('imagem/<int:foto_id>', views.imagem, name='imagem'),
    path('buscar/', views.buscar, name='buscar'),
]

