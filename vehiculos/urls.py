from django.urls import path
from .views import lista_vehiculos, create_vehiculo, delete_vehiculo, edit_vehiculo

urlpatterns = [
    path('', lista_vehiculos),
    path('new/', create_vehiculo, name='create_vehiculo'),
    path('del/<str:num_bastidor>/', delete_vehiculo, name='delete_vehiculo'),
    path('edit/<str:num_bastidor>/', edit_vehiculo, name='edit_vehiculo'),
]



